# Sauce Demo 手工测试

覆盖登录、商品、购物车和结算的测试设计与执行资料，包含验收标准、需求追踪、可复现问题、浏览器证据和回归结果。

2026-10-15 已对在线站点重新执行浏览器操作，使用 Playwright 辅助校验、截图及录制追踪。20 条正常主流程、3 条补充用例均通过。5 条问题记录均已完成确认：4 条属于特殊演示账号预设行为，1 条为空购物车结算的业务规则建议。空购物车负向用例相对项目建议规则为 Fail，独立统计。

| 内容 | 入口 |
|---|---|
| 测试计划与环境 | [plan.md](docs/plan.md) |
| 用户故事与验收标准 | [stories.md](docs/stories.md) |
| 用例、操作步骤及证据 | [test-cases.md](docs/test-cases.md) |
| 需求追踪 | [trace.md](docs/trace.md) |
| 已确认问题及分类依据 | [defects.md](docs/defects.md) |
| 回归记录 | [regression.md](docs/regression.md) |
| 当前测试总结 | [test-summary.md](docs/test-summary.md) |
| 浏览器原始结果与截图 | [证据说明](evidence/recheck-2026-10-15/README.md) |
| 结构化问题与验证记录 | [findings.json](docs/findings.json)、[verification.json](docs/verification.json) |
| 历史记录与来源 | [history.json](docs/history.json)、[provenance.json](docs/provenance.json) |

被测站点：[Sauce Demo](https://www.saucedemo.com/)。默认账号 standard_user，公开演示密码 secret_sauce。其他账号仅用于指定对照，不把预设异常混入普通账号主流程。

查看资料无需安装第三方依赖。在项目根目录运行：

```bash
python scripts/check_consistency.py
```

该命令校验文档统计、需求映射、实际执行数据、证据文件及追踪压缩包。GitHub Actions 执行相同检查；它不重新访问被测站点。人工复核可依照用例表和问题记录中的具体步骤执行。

“Confirmed”表示现象及适用条件已经验证。网站由第三方维护，此项目没有修改站点或宣称问题已修复。
