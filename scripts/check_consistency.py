import hashlib
import json
import re
import zipfile
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def read_json(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def table_rows(path, prefix):
    return {
        cells[0]: cells
        for line in (ROOT / path).read_text(encoding="utf-8").splitlines()
        if re.match(r"\| " + prefix + r"-\d+ \|", line)
        for cells in [[cell.strip() for cell in line.strip("|").split("|")]]
    }


def check_local_file(relative):
    path = (ROOT / relative).resolve()
    require(path.is_relative_to(ROOT), "Path outside project: " + relative)
    require(path.is_file(), "Missing evidence: " + relative)
    return path


def check_evidence_references(value):
    if isinstance(value, dict):
        for nested in value.values():
            check_evidence_references(nested)
    elif isinstance(value, list):
        for nested in value:
            check_evidence_references(nested)
    elif isinstance(value, str) and value.startswith("evidence/"):
        check_local_file(value)


def main():
    verification = read_json("docs/verification.json")
    raw = read_json(verification["raw_results"])
    findings_record = read_json(verification["findings_record"])
    findings = findings_record["findings"]
    require(verification["current_site_reexecution"] is True, "Current execution flag missing")
    require(raw["started_at"] == verification["started_at"] and raw["finished_at"] == verification["finished_at"], "Execution time mismatch")
    require(raw["started_at"] <= raw["finished_at"], "Invalid execution timestamps")
    require(verification["browser"].endswith(raw["browser_version"]), "Browser mismatch")
    stories = (ROOT / "docs/stories.md").read_text(encoding="utf-8")
    all_trace = {}
    for prefix, raw_key, summary_key, total, status_index, story_index, criterion_index in [
        ("TC", "baseline", "cases", 20, 5, 6, 7),
        ("EXT", "extensions", "extensions", 3, 4, 5, 6),
    ]:
        items = raw[raw_key]
        expected_ids = {f"{prefix}-{number:03}" for number in range(1, total + 1)}
        require(len(items) == total and {item["id"] for item in items} == expected_ids, "Missing or duplicate executed cases: " + prefix)
        rows = table_rows("docs/test-cases.md", prefix)
        case_lines = re.findall(r"^\| " + prefix + r"-\d+ \|", (ROOT / "docs/test-cases.md").read_text(encoding="utf-8"), re.M)
        require(len(case_lines) == total and set(rows) == expected_ids, "Document case set mismatch: " + prefix)
        trace_rows = table_rows("docs/trace.md", prefix)
        require(set(trace_rows) == expected_ids, "Missing trace: " + prefix)
        counts = Counter(item["status"] for item in items)
        require(verification[summary_key] == {"total": total, "pass": counts["Pass"], "fail": counts["Fail"]}, "Summary counts mismatch: " + prefix)
        for item in items:
            require(item["status"] == "Pass", "Unexpected baseline failure: " + item["id"])
            cells, traced = rows[item["id"]], trace_rows[item["id"]]
            require(cells[status_index] == item["status"] == traced[3], "Status mismatch: " + item["id"])
            require(cells[story_index] == traced[1] and cells[criterion_index] == traced[2], "Requirement mapping mismatch: " + item["id"])
            require(cells[story_index] in stories, "Unknown user story")
            for criterion in cells[criterion_index].split("、"):
                require(criterion in stories, "Unknown criterion: " + criterion)
            require(item["screenshot"] in cells[-1], "Screenshot mapping mismatch: " + item["id"])
            all_trace[item["id"]] = traced
    declared_criteria = set(re.findall(r"AC-[A-Z]+-\d+", stories))
    traced_criteria = set(re.findall(r"AC-[A-Z]+-\d+", (ROOT / "docs/trace.md").read_text(encoding="utf-8")))
    require(declared_criteria == traced_criteria, "Uncovered or unknown acceptance criteria")
    references = raw["reference_products"]
    accounts = raw["accounts"]
    require(len(references) == 6, "Expected six reference products")
    expected_sessions = {(user, repetition) for user in ["standard_user", "problem_user", "visual_user"] for repetition in [1, 2]}
    require(len(accounts) == 6 and {(a["user"], a["repetition"]) for a in accounts} == expected_sessions, "Account session coverage mismatch")
    for account in accounts:
        user = account["user"]
        require(len(account["list"]) == len(account["details"]) == 6, "Incomplete product comparison")
        image_differences = sum(item["image"] != reference["image"] for item, reference in zip(account["list"], references))
        require(image_differences == {"standard_user": 0, "problem_user": 6, "visual_user": 1}[user], "Image observation changed")
        for item, detail in zip(account["list"], account["details"]):
            require(item["name"] == detail["selected"], "Incomplete selection mapping")
            differences = {key: {"list": item[key], "detail": detail["actual"][key]} for key in item if item[key] != detail["actual"][key]}
            require(differences == detail["mismatch"], "Product mismatch data inconsistent")
            if user == "standard_user":
                require(not differences, "Normal account product mismatch")
            elif user == "problem_user":
                require("name" in differences, "Problem account navigation finding missing")
            else:
                require("price" in differences and "name" not in differences, "Visual account price finding missing")
        require(account["cart"]["actual"] == account["cart"]["requested"], "Two-item cart mismatch")
        checkout = account["checkout"]
        if user == "problem_user":
            require(checkout["fields"] == {"firstName": "Tester", "lastName": "", "postalCode": "100000"}, "Problem account input observation changed")
            require(checkout["complete"] is False and checkout["overview"] is None and checkout["error"] == ["Error: Last Name is required"], "Problem account checkout observation changed")
        else:
            require(checkout["complete"] is True and not checkout["error"], "Normal/visual checkout incomplete")
            require(checkout["overview"]["names"] == account["cart"]["requested"] and checkout["overview"]["subtotal"] == "Item total: $39.98", "Order overview mismatch")
        if user in {"standard_user", "problem_user"}:
            restricted = account["restricted_add"]
            require(restricted["requested"] == "Sauce Labs Bolt T-Shirt", "Wrong targeted item")
            require(restricted["actual"] == (["Sauce Labs Bolt T-Shirt"] if user == "standard_user" else []), "Targeted add finding mismatch")
    require(len(raw["empty_cart"]) == 2 and {item["repetition"] for item in raw["empty_cart"]} == {1, 2}, "Empty-cart repetitions missing")
    for empty in raw["empty_cart"]:
        require(empty["user"] == "standard_user" and empty["empty_before"] and empty["complete"], "Empty-cart completion not established")
        require(empty["overview"] == {"names": [], "subtotal": "Item total: $0"}, "Empty-cart overview mismatch")
    negative = table_rows("docs/test-cases.md", "NC")
    require(set(negative) == {"NC-001"} and negative["NC-001"][4] == "Fail", "Negative rule outcome mismatch")
    require(table_rows("docs/trace.md", "NC")["NC-001"][3] == "Fail", "Negative rule trace mismatch")
    require(verification["negative_rule_checks"] == {"total": 1, "pass": 0, "fail": 1, "repetitions": 2, "rule_authority": "project-recommendation"}, "Negative rule summary mismatch")
    require(len(findings) == 5 and {f["id"] for f in findings} == {f"BUG-{number:03}" for number in range(1, 6)}, "Finding IDs mismatch")
    defect_rows = table_rows("docs/defects.md", "BUG")
    require(set(defect_rows) == {f["id"] for f in findings}, "Defect document set mismatch")
    for finding in findings:
        require(finding["status"] == defect_rows[finding["id"]][4] == "Confirmed", "Unconfirmed finding")
        require(finding["reproduced_sessions"] == finding["attempted_sessions"] == 2, "Finding repetitions inconsistent")
        require(finding["remediation"] == "not-performed", "Unsupported remediation claim")
        require(finding["screenshots"] and finding["traces"], "Missing finding evidence")
        require(finding["classification"] == "business-rule-recommendation" if finding["id"] == "BUG-003" else finding["classification"] == "demo-account-behavior", "Finding classification mismatch")
    require(verification["findings"] == {"total": 5, "confirmed": 5, "pending_confirmation": 0, "demo_account_behavior": 4, "business_rule_recommendation": 1}, "Finding totals mismatch")
    regression = table_rows("docs/regression.md", "REG")
    require(len(regression) == 11 and Counter(cells[3] for cells in regression.values()) == {"Pass": 8, "Reproduced": 3}, "Regression totals mismatch")
    require(verification["regression"] == {"total": 11, "pass": 8, "reproduced": 3, "independent_case_count": False}, "Regression summary mismatch")
    for cells in regression.values():
        for code in re.findall(r"(?:TC|BUG)-\d+", cells[4]):
            require(code in all_trace or code in defect_rows, "Unknown regression reference: " + code)
    check_evidence_references(raw)
    check_evidence_references(findings_record)
    markdown_files = [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md")), *sorted((ROOT / "evidence").rglob("*.md"))]
    for path in markdown_files:
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#")):
                continue
            relative, _, anchor = target.partition("#")
            resolved = (path.parent / unquote(relative)).resolve()
            require(resolved.is_relative_to(ROOT) and resolved.is_file(), "Missing document link: " + str(path) + ": " + target)
            if anchor:
                require(f'id="{anchor}"' in resolved.read_text(encoding="utf-8"), "Missing document anchor: " + target)
    index = read_json("docs/evidence-index.json")
    actual_files = {path.relative_to(ROOT).as_posix() for path in (ROOT / "evidence").rglob("*") if path.is_file()}
    require({item["path"] for item in index["files"]} == actual_files, "Evidence manifest file set mismatch")
    for item in index["files"]:
        path = check_local_file(item["path"])
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], "Evidence hash mismatch: " + item["path"])
        if path.suffix == ".png":
            require(path.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"), "Invalid PNG: " + item["path"])
        if path.suffix == ".zip":
            with zipfile.ZipFile(path) as archive:
                require(archive.testzip() is None and any(name.endswith(".trace") for name in archive.namelist()), "Invalid Playwright trace: " + item["path"])
    for source in read_json("docs/provenance.json")["sources"]:
        require(hashlib.sha256(check_local_file(source["target"]).read_bytes()).hexdigest() == source["source_sha256"] == source["target_sha256"], "Historical evidence changed")
    require(read_json("docs/history.json")["current_results"] is False, "History must remain historical")
    print("Verified: 20 baseline + 3 supplemental Pass; 1 negative-rule Fail (2 repetitions); 5 Confirmed findings; 8 Pass + 3 Reproduced regression items; requirement coverage, links and evidence integrity.")


if __name__ == "__main__":
    main()
