# 浏览器复核证据

执行时间：2026-10-15T15:59:14.658600+08:00 至 2026-10-15T16:04:23.032580+08:00。浏览器 Chromium 153.0.8010.12，Windows，1366 × 900。Playwright 通过真实页面控件完成登录、浏览、加购和结算；未修改网站业务数据或模拟成功响应。

[results.json](results.json) 保存断言结果、实际读取的商品字段、页面地址、表单值和订单概览。部分主用例的 actual 为 null，表示断言函数无返回值；status 为断言结果，并有对应截图与 trace。可读操作和预期见 [用例清单](../../docs/test-cases.md)。

| 文件 | 含义 |
|---|---|
| TC-001～TC-020.png | 20 条主用例执行状态截图 |
| TC-001～TC-006.zip | 登录用例独立操作追踪 |
| baseline-products.zip | TC-007～TC-014、TC-016～TC-020 连续操作追踪 |
| normal-account-comparison.zip | TC-015 商品数据跨账号对照 |
| EXT-001～EXT-003.png / .zip | 错误后重试、姓氏及邮编必填校验 |
| 账号-轮次-list.png / -detail-序号.png / .zip | 三个账号、每个账号两轮、每轮 6 件商品的列表和详情对照 |
| 账号-轮次-flow-cart.png / -flow-checkout.png / -flow.zip | 重新等待页面稳定后记录的两件商品购物车及结算结果 |
| empty-confirmed-轮次-before.png / -after.png / .zip | 标准账号空购物车结算前后截图和完整追踪，两轮 |
| 账号-odd-item-轮次.png / .zip | 标准账号与问题账号的 Bolt T-Shirt 加购对照，两轮 |

判定以 results.json 中引用的最终截图为准。初步观察中尚未等待页面切换稳定的购物车和结算快照已移出交付范围；商品对照 trace 中的后续结算部分也不作为最终结算结论，最终结算以独立 flow trace 为准。

全部 trace 是 Playwright ZIP 格式，可使用 `playwright show-trace 文件路径` 查看，需要本地已安装 Playwright。CI 仅校验记录与压缩包完整性，不连接网站重跑。

上级目录的 BUG-001.png、BUG-002.png、BUG-003.png 是原学习资料的历史截图，不作为本次执行证据。[历史快照](../../docs/history.json) 保留原记录与当前拆分关系。
