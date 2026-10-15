# 需求与用例追踪

执行日期：2026-10-15。主流程、补充验证和业务规则负向检查分别统计；特殊账号观察不覆盖普通账号的执行结果。

| 用例 | 用户故事 | 验收标准 | 状态 | 关联问题 |
|---|---|---|---|---|
| TC-001 | US-LOGIN-001 | AC-LOGIN-001 | Pass | — |
| TC-002 | US-LOGIN-001 | AC-LOGIN-002 | Pass | — |
| TC-003 | US-LOGIN-001 | AC-LOGIN-003 | Pass | — |
| TC-004 | US-LOGIN-001 | AC-LOGIN-004 | Pass | — |
| TC-005 | US-LOGIN-001 | AC-LOGIN-004 | Pass | — |
| TC-006 | US-LOGIN-001 | AC-LOGIN-004 | Pass | — |
| TC-007 | US-PRODUCT-001 | AC-PRODUCT-001 | Pass | — |
| TC-008 | US-PRODUCT-001 | AC-PRODUCT-002 | Pass | — |
| TC-009 | US-PRODUCT-001 | AC-PRODUCT-002 | Pass | — |
| TC-010 | US-PRODUCT-001 | AC-PRODUCT-002 | Pass | — |
| TC-011 | US-PRODUCT-001 | AC-PRODUCT-003 | Pass | — |
| TC-012 | US-PRODUCT-001 | AC-PRODUCT-002 | Pass | — |
| TC-013 | US-PRODUCT-001 | AC-PRODUCT-005 | Pass | — |
| TC-014 | US-PRODUCT-001 | AC-PRODUCT-006 | Pass | — |
| TC-015 | US-PRODUCT-001 | AC-PRODUCT-004 | Pass | — |
| TC-016 | US-CART-001 | AC-CART-001 | Pass | — |
| TC-017 | US-CART-001 | AC-CART-003 | Pass | — |
| TC-018 | US-CART-001 | AC-CART-002、AC-CART-004 | Pass | — |
| TC-019 | US-CHECKOUT-001 | AC-CHECKOUT-001 | Pass | — |
| TC-020 | US-CHECKOUT-001 | AC-CHECKOUT-003、AC-CHECKOUT-004 | Pass | — |
| EXT-001 | US-LOGIN-001 | AC-LOGIN-005 | Pass | — |
| EXT-002 | US-CHECKOUT-001 | AC-CHECKOUT-002 | Pass | — |
| EXT-003 | US-CHECKOUT-001 | AC-CHECKOUT-002 | Pass | — |
| NC-001 | US-CHECKOUT-002 | AC-CHECKOUT-005 | Fail | BUG-003 |

| 专项观察 | 账号 | 已确认问题 |
|---|---|---|
| 图片与正常基线对照，各两轮 | problem_user、visual_user | BUG-001 |
| 逐个打开 6 件商品详情，各两轮 | problem_user、visual_user | BUG-002 |
| 空购物车完成订单，两轮 | standard_user | BUG-003 |
| 姓氏输入与正常结算对照，各两轮 | problem_user、standard_user | BUG-004 |
| Bolt T-Shirt 加入购物车对照，各两轮 | problem_user、standard_user | BUG-005 |

用例操作和证据见 [test-cases.md](test-cases.md)，问题复现步骤见 [defects.md](defects.md)。
