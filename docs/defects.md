# 已确认问题

确认日期：2026-10-15。5 条记录均为 Confirmed，均有两轮独立会话证据，无待确认条目。4 条属于公开源码中的特殊演示账号行为；1 条为基于实测的业务规则建议。“确认”不等于“修复”，本项目没有修改第三方网站。

原历史 BUG-002 的购物车现象拆为 BUG-005；原 BUG-003 的姓名输入异常拆为 BUG-004。历史编号、截图与统计保存在 [history.json](history.json)，当前结构化记录见 [findings.json](findings.json)。

| 编号 | 现象 | 分类 | 复现 | 状态 |
|---|---|---|---|---|
| BUG-001 | 特殊账号商品图片被替换 | 演示账号预设行为 | 每个适用账号 2/2 会话 | Confirmed |
| BUG-002 | 特殊账号详情跳转和列表价格异常 | 演示账号预设行为 | 每个适用账号 2/2 会话 | Confirmed |
| BUG-003 | 空购物车可以完成零金额订单 | 业务规则建议 | 每个适用账号 2/2 会话 | Confirmed |
| BUG-004 | problem_user 填写姓氏覆盖名字，无法继续结算 | 演示账号预设行为 | 每个适用账号 2/2 会话 | Confirmed |
| BUG-005 | problem_user 点击部分商品加入按钮后购物车仍为空 | 演示账号预设行为 | 每个适用账号 2/2 会话 | Confirmed |

<a id="bug-001"></a>

## BUG-001：特殊账号商品图片被替换

账号：problem_user、visual_user；密码：secret_sauce。每轮使用新的浏览器会话，避免购物车状态相互影响。

1. 以 standard_user 登录，保存 6 件商品图片作为对照。
2. 退出后分别用 problem_user、visual_user 登录，逐项对照列表图片。
3. 使用新的浏览器会话重复操作。

预期：按普通购物场景，图片与对应商品一致。

实际：problem_user 的 6/6 张列表图片被替换为同一异常图片；visual_user 的首件商品图片被替换（1/6）。标准账号为 0/6。两轮结果一致。

结论：公开源码明确按账号替换图片，归类为演示预设行为；确认完成，保留为测试样例。

截图：[standard_user-1-list](../evidence/recheck-2026-10-15/standard_user-1-list.png)、[standard_user-2-list](../evidence/recheck-2026-10-15/standard_user-2-list.png)、[problem_user-1-list](../evidence/recheck-2026-10-15/problem_user-1-list.png)、[problem_user-2-list](../evidence/recheck-2026-10-15/problem_user-2-list.png)、[visual_user-1-list](../evidence/recheck-2026-10-15/visual_user-1-list.png)、[visual_user-2-list](../evidence/recheck-2026-10-15/visual_user-2-list.png)。

操作追踪：[standard_user-1](../evidence/recheck-2026-10-15/standard_user-1.zip)、[standard_user-2](../evidence/recheck-2026-10-15/standard_user-2.zip)、[problem_user-1](../evidence/recheck-2026-10-15/problem_user-1.zip)、[problem_user-2](../evidence/recheck-2026-10-15/problem_user-2.zip)、[visual_user-1](../evidence/recheck-2026-10-15/visual_user-1.zip)、[visual_user-2](../evidence/recheck-2026-10-15/visual_user-2.zip)。

源码依据：[pages/Inventory.jsx](https://github.com/saucelabs/sample-app-web/blob/009b7a5b9db78488b014e689258840a6a7d7741f/src/pages/Inventory.jsx#L116-L122)。

<a id="bug-002"></a>

## BUG-002：特殊账号详情跳转和列表价格异常

账号：problem_user、visual_user；密码：secret_sauce。每轮使用新的浏览器会话，避免购物车状态相互影响。

1. 分别登录 standard_user、problem_user、visual_user，记录每件商品的列表信息。
2. 依次点击全部 6 件商品名称，比较名称、价格、图片地址和描述，再返回列表。
3. 在新会话重复全量对照。

预期：按普通购物场景，列表与详情指向同一商品且价格一致。

实际：problem_user 的 6/6 次详情名称与所选商品不一致；visual_user 的 6/6 件商品列表价格与详情不一致，名称对应正常。标准账号 6/6 件商品四项均一致；两轮结果一致。

结论：源码对 problem_user 的详情商品编号加 1，对 visual_user 的列表价格随机化。两种表现作为本条的独立子场景，不泛称所有账号商品错误。

截图：[standard_user-1-detail-0](../evidence/recheck-2026-10-15/standard_user-1-detail-0.png)、[standard_user-2-detail-0](../evidence/recheck-2026-10-15/standard_user-2-detail-0.png)、[problem_user-1-detail-0](../evidence/recheck-2026-10-15/problem_user-1-detail-0.png)、[problem_user-2-detail-0](../evidence/recheck-2026-10-15/problem_user-2-detail-0.png)、[visual_user-1-detail-0](../evidence/recheck-2026-10-15/visual_user-1-detail-0.png)、[visual_user-2-detail-0](../evidence/recheck-2026-10-15/visual_user-2-detail-0.png)。

操作追踪：[standard_user-1](../evidence/recheck-2026-10-15/standard_user-1.zip)、[standard_user-2](../evidence/recheck-2026-10-15/standard_user-2.zip)、[problem_user-1](../evidence/recheck-2026-10-15/problem_user-1.zip)、[problem_user-2](../evidence/recheck-2026-10-15/problem_user-2.zip)、[visual_user-1](../evidence/recheck-2026-10-15/visual_user-1.zip)、[visual_user-2](../evidence/recheck-2026-10-15/visual_user-2.zip)。

源码依据：[components/InventoryListItem.jsx](https://github.com/saucelabs/sample-app-web/blob/009b7a5b9db78488b014e689258840a6a7d7741f/src/components/InventoryListItem.jsx#L73-L77)、[pages/Inventory.jsx](https://github.com/saucelabs/sample-app-web/blob/009b7a5b9db78488b014e689258840a6a7d7741f/src/pages/Inventory.jsx#L122)。

<a id="bug-003"></a>

## BUG-003：空购物车可以完成零金额订单

账号：standard_user；密码：secret_sauce。每轮使用新的浏览器会话，避免购物车状态相互影响。

1. 在新会话登录 standard_user，不加入任何商品，进入购物车，确认商品行数为 0。
2. 点击 Checkout，依次填写 Learner、Tester、100000，点击 Continue。
3. 确认订单概览没有商品且 Item total: $0，点击 Finish。
4. 在另一新会话重复操作。

预期：按本项目提出的业务规则建议，购物车为空时应阻止提交订单；此规则不作为官方既有规格。

实际：两轮均以 0 件商品、Item total: $0 进入概览并完成订单，页面显示 Thank you for your order!。

结论：可观察行为已确认。NC-001 相对本项目业务规则为 Fail，保留为改进建议；没有官方空订单限制规格，不认定为违反官方已承诺功能。

截图：[empty-confirmed-1-before](../evidence/recheck-2026-10-15/empty-confirmed-1-before.png)、[empty-confirmed-1-after](../evidence/recheck-2026-10-15/empty-confirmed-1-after.png)、[empty-confirmed-2-before](../evidence/recheck-2026-10-15/empty-confirmed-2-before.png)、[empty-confirmed-2-after](../evidence/recheck-2026-10-15/empty-confirmed-2-after.png)。

操作追踪：[empty-confirmed-1](../evidence/recheck-2026-10-15/empty-confirmed-1.zip)、[empty-confirmed-2](../evidence/recheck-2026-10-15/empty-confirmed-2.zip)。

<a id="bug-004"></a>

## BUG-004：problem_user 填写姓氏覆盖名字，无法继续结算

账号：problem_user；密码：secret_sauce。每轮使用新的浏览器会话，避免购物车状态相互影响。

1. 用 problem_user 登录，加入 Sauce Labs Backpack 和 Sauce Labs Bike Light。
2. 进入 Checkout，依次在 First Name、Last Name、Zip/Postal Code 填写 Learner、Tester、100000。
3. 读取三个字段，再点击 Continue；使用 standard_user 对照，并在新会话重复。

预期：三个字段分别保留输入值，可以进入订单概览并完成订单。

实际：problem_user 的 First Name 变成 Tester，Last Name 为空，邮编为 100000；Continue 后提示 Error: Last Name is required，不能进入概览。标准账号相同输入完成订单；两轮结果一致。

结论：从历史 BUG-003 的混合描述拆分；源码的 problem_user 姓氏变更分支调用 setFirstName，属于演示预设行为。

截图：[problem_user-1-flow-checkout](../evidence/recheck-2026-10-15/problem_user-1-flow-checkout.png)、[problem_user-2-flow-checkout](../evidence/recheck-2026-10-15/problem_user-2-flow-checkout.png)、[standard_user-1-flow-checkout](../evidence/recheck-2026-10-15/standard_user-1-flow-checkout.png)、[standard_user-2-flow-checkout](../evidence/recheck-2026-10-15/standard_user-2-flow-checkout.png)。

操作追踪：[problem_user-1-flow](../evidence/recheck-2026-10-15/problem_user-1-flow.zip)、[problem_user-2-flow](../evidence/recheck-2026-10-15/problem_user-2-flow.zip)、[standard_user-1-flow](../evidence/recheck-2026-10-15/standard_user-1-flow.zip)、[standard_user-2-flow](../evidence/recheck-2026-10-15/standard_user-2-flow.zip)。

源码依据：[pages/CheckOutStepOne.jsx](https://github.com/saucelabs/sample-app-web/blob/009b7a5b9db78488b014e689258840a6a7d7741f/src/pages/CheckOutStepOne.jsx#L25-L30)、[pages/CheckOutStepOne.jsx](https://github.com/saucelabs/sample-app-web/blob/009b7a5b9db78488b014e689258840a6a7d7741f/src/pages/CheckOutStepOne.jsx#L47-L49)。

<a id="bug-005"></a>

## BUG-005：problem_user 点击部分商品加入按钮后购物车仍为空

账号：problem_user；密码：secret_sauce。每轮使用新的浏览器会话，避免购物车状态相互影响。

1. 在空购物车的新会话登录 problem_user。
2. 点击 Sauce Labs Bolt T-Shirt 的 Add to cart，进入购物车查看商品。
3. 用 standard_user 对同一商品执行相同操作；各自在新会话重复。

预期：购物车出现 Sauce Labs Bolt T-Shirt。

实际：problem_user 两轮购物车均为 0 件；standard_user 两轮均包含该 T-Shirt。已确认是未加入商品，不是加入了错误商品。

结论：从历史 BUG-002 的购物车描述拆分；源码对 problem_user 的奇数编号商品提前返回。实测针对编号为 1 的 Bolt T-Shirt，不外推所有商品都不能加入。

截图：[problem_user-odd-item-1](../evidence/recheck-2026-10-15/problem_user-odd-item-1.png)、[problem_user-odd-item-2](../evidence/recheck-2026-10-15/problem_user-odd-item-2.png)、[standard_user-odd-item-1](../evidence/recheck-2026-10-15/standard_user-odd-item-1.png)、[standard_user-odd-item-2](../evidence/recheck-2026-10-15/standard_user-odd-item-2.png)。

操作追踪：[problem_user-odd-item-1](../evidence/recheck-2026-10-15/problem_user-odd-item-1.zip)、[problem_user-odd-item-2](../evidence/recheck-2026-10-15/problem_user-odd-item-2.zip)、[standard_user-odd-item-1](../evidence/recheck-2026-10-15/standard_user-odd-item-1.zip)、[standard_user-odd-item-2](../evidence/recheck-2026-10-15/standard_user-odd-item-2.zip)。

源码依据：[components/InventoryListItem.jsx](https://github.com/saucelabs/sample-app-web/blob/009b7a5b9db78488b014e689258840a6a7d7741f/src/components/InventoryListItem.jsx#L33-L38)。

源码参考固定到提交 `009b7a5b9db78488b014e689258840a6a7d7741f`。源码用于解释账号分支，在线现象由独立浏览器证据确认；没有宣称该提交就是线上部署版本。
