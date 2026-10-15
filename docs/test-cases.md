# 测试用例

执行日期：2026-10-15。以下均为本次真实浏览器操作结果。除特别标明账号的 TC-015 及登录无效输入外，使用 standard_user / secret_sauce。商品操作前按步骤准备购物车，结算固定输入 Learner / Tester / 100000。

| 编号 | 场景 | 具体操作 | 预期 | 实际 | 状态 | 用户故事 | 验收标准 | 证据 |
|---|---|---|---|---|---|---|---|---|
| TC-001 | 正确账号登录 | 输入 standard_user / secret_sauce，点击 Login | 进入 Products，显示 6 件商品 | 进入商品列表，标题 Products | Pass | US-LOGIN-001 | AC-LOGIN-001 | [截图](../evidence/recheck-2026-10-15/TC-001.png) |
| TC-002 | 错误用户名 | 输入 unknown_recheck_user / secret_sauce，点击 Login | 停留登录页并提示账号密码不匹配 | 显示 Username and password do not match | Pass | US-LOGIN-001 | AC-LOGIN-002 | [截图](../evidence/recheck-2026-10-15/TC-002.png) |
| TC-003 | 错误密码 | 输入 standard_user / wrong_password，点击 Login | 拒绝登录并提示账号密码不匹配 | 显示 Username and password do not match | Pass | US-LOGIN-001 | AC-LOGIN-003 | [截图](../evidence/recheck-2026-10-15/TC-003.png) |
| TC-004 | 用户名为空 | 用户名留空，密码填 secret_sauce，点击 Login | 提示 Username is required | 出现用户名必填提示 | Pass | US-LOGIN-001 | AC-LOGIN-004 | [截图](../evidence/recheck-2026-10-15/TC-004.png) |
| TC-005 | 密码为空 | 用户名填 standard_user，密码留空，点击 Login | 提示 Password is required | 出现密码必填提示 | Pass | US-LOGIN-001 | AC-LOGIN-004 | [截图](../evidence/recheck-2026-10-15/TC-005.png) |
| TC-006 | 账号密码都为空 | 两个输入框都留空，点击 Login | 提示 Username is required | 出现用户名必填提示 | Pass | US-LOGIN-001 | AC-LOGIN-004 | [截图](../evidence/recheck-2026-10-15/TC-006.png) |
| TC-007 | 商品列表 | 登录后统计列表商品卡片 | 存在 6 件商品 | 商品卡片数量为 6 | Pass | US-PRODUCT-001 | AC-PRODUCT-001 | [截图](../evidence/recheck-2026-10-15/TC-007.png) |
| TC-008 | 商品名称 | 读取列表中全部商品名称 | 6 个名称非空且不重复 | 6 个名称均非空且互不相同 | Pass | US-PRODUCT-001 | AC-PRODUCT-002 | [截图](../evidence/recheck-2026-10-15/TC-008.png) |
| TC-009 | 商品图片 | 检查 6 张商品图片是否加载完成及自然宽度 | 图片加载完成，naturalWidth 大于 0 | 6 张图片均成功加载 | Pass | US-PRODUCT-001 | AC-PRODUCT-002 | [截图](../evidence/recheck-2026-10-15/TC-009.png) |
| TC-010 | 商品价格 | 读取 6 件商品的价格，去除货币符号后比较 | 价格可以转换为大于 0 的数值 | 6 个价格均为正数 | Pass | US-PRODUCT-001 | AC-PRODUCT-002 | [截图](../evidence/recheck-2026-10-15/TC-010.png) |
| TC-011 | 打开商品详情 | 点击 Sauce Labs Backpack 名称 | 详情名称为 Sauce Labs Backpack | 打开对应背包详情 | Pass | US-PRODUCT-001 | AC-PRODUCT-003 | [截图](../evidence/recheck-2026-10-15/TC-011.png) |
| TC-012 | 列表与详情一致 | 比较背包列表与详情的名称、价格、图片地址、描述 | 四项信息完全一致 | 四项一致；另有正常账号全部 6 件商品各两次对照证据 | Pass | US-PRODUCT-001 | AC-PRODUCT-002 | [截图](../evidence/recheck-2026-10-15/TC-012.png) |
| TC-013 | 返回列表 | 从背包详情点击 Back to products | 返回列表，显示 6 件商品 | 列表显示 6 件商品 | Pass | US-PRODUCT-001 | AC-PRODUCT-005 | [截图](../evidence/recheck-2026-10-15/TC-013.png) |
| TC-014 | 刷新列表 | 在商品列表刷新页面，等待加载完成 | 仍显示 6 件商品 | 刷新后显示 6 件商品 | Pass | US-PRODUCT-001 | AC-PRODUCT-006 | [截图](../evidence/recheck-2026-10-15/TC-014.png) |
| TC-015 | 同等商品数据账号对照 | 分别用 standard_user、performance_glitch_user 登录，读取全部商品信息 | 名称、价格、图片地址及描述一致 | 两账号的 6 件商品数据一致；此用例不判定响应速度 | Pass | US-PRODUCT-001 | AC-PRODUCT-004 | [截图](../evidence/recheck-2026-10-15/TC-015.png) |
| TC-016 | 加入商品 | 空购物车下点击背包的 Add to cart | 购物车角标变为 1 | 角标为 1 | Pass | US-CART-001 | AC-CART-001 | [截图](../evidence/recheck-2026-10-15/TC-016.png) |
| TC-017 | 删除商品 | 进入购物车，点击背包的 Remove | 购物车商品行数变为 0 | 商品行数为 0 | Pass | US-CART-001 | AC-CART-003 | [截图](../evidence/recheck-2026-10-15/TC-017.png) |
| TC-018 | 购物车数量和名称 | 加入背包和车灯，进入购物车，核对名称及角标 | 显示对应两件商品，角标为 2 | 名称为背包、车灯，角标为 2 | Pass | US-CART-001 | AC-CART-002、AC-CART-004 | [截图](../evidence/recheck-2026-10-15/TC-018.png) |
| TC-019 | 名字必填 | 购物车有商品时进入结算，三个字段留空并点击 Continue | 提示 Error: First Name is required | 出现名字必填提示，不能进入订单概览 | Pass | US-CHECKOUT-001 | AC-CHECKOUT-001 | [截图](../evidence/recheck-2026-10-15/TC-019.png) |
| TC-020 | 正常订单完成 | 保留背包和车灯，填写 Learner / Tester / 100000，点击 Continue、Finish | 显示 Thank you for your order! | 成功进入 checkout-complete.html，显示订单完成提示 | Pass | US-CHECKOUT-001 | AC-CHECKOUT-003、AC-CHECKOUT-004 | [截图](../evidence/recheck-2026-10-15/TC-020.png) |

主用例 20 条：20 Pass、0 Fail。正常账号全部商品的额外对照见 [原始结果](../evidence/recheck-2026-10-15/results.json)，特殊账号差异见 [问题记录](defects.md)。

## 补充用例

| 编号 | 场景 | 具体操作 | 预期及实际 | 状态 | 用户故事 | 验收标准 | 证据 |
|---|---|---|---|---|---|---|---|
| EXT-001 | 错误密码后重试 | 先用 wrong_password 登录，出现错误后改为 secret_sauce 再登录 | 成功进入 Products | Pass | US-LOGIN-001 | AC-LOGIN-005 | [截图](../evidence/recheck-2026-10-15/EXT-001.png) |
| EXT-002 | 姓氏必填 | 购物车有背包；填写 Learner，姓氏留空，邮编填 100000，点击 Continue | Error: Last Name is required | Pass | US-CHECKOUT-001 | AC-CHECKOUT-002 | [截图](../evidence/recheck-2026-10-15/EXT-002.png) |
| EXT-003 | 邮编必填 | 购物车有背包；填写 Learner / Tester，邮编留空，点击 Continue | Error: Postal Code is required | Pass | US-CHECKOUT-001 | AC-CHECKOUT-002 | [截图](../evidence/recheck-2026-10-15/EXT-003.png) |

补充用例 3 条：3 Pass、0 Fail。它们不计入 20 条主用例总数。非空无效邮编不在上述必填校验的结论内。

## 空购物车负向检查

| 编号 | 前置与操作 | 项目建议预期 | 实际 | 状态 | 验收标准 | 问题 |
|---|---|---|---|---|---|---|
| NC-001 | 新会话登录，购物车保持 0 件，Checkout 后填 Learner / Tester / 100000，Continue 后点击 Finish | 空购物车不能提交订单 | 两次均出现零商品、$0 概览并成功进入订单完成页 | Fail | AC-CHECKOUT-005 | BUG-003 |

此预期是本项目提出的业务规则建议，没有据此宣称官方规格被违反。1 条负向用例重复 2 次，失败 2 次，不计为 2 条用例。证据见 [BUG-003](defects.md#bug-003)。
