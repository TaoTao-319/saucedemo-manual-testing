# 用户故事与验收标准

正常功能验收以 standard_user 为基线。商品数据跨账号比较限定为 standard_user 与 performance_glitch_user；problem_user 和 visual_user 用于预设异常探索，不直接决定普通流程是否通过。

| 用户故事 | 用户价值 | 验收标准 | 当前结论 |
|---|---|---|---|
| US-LOGIN-001 | 能登录并纠正错误输入 | AC-LOGIN-001：正确凭据进入列表；AC-LOGIN-002：错误用户名被拒绝；AC-LOGIN-003：错误密码被拒绝；AC-LOGIN-004：空用户名或密码有必填提示；AC-LOGIN-005：错误密码后改正可重新登录 | TC-001～TC-006、EXT-001 均 Pass |
| US-PRODUCT-001 | 能查看一致的商品信息 | AC-PRODUCT-001：显示 6 件商品；AC-PRODUCT-002：名称非空、图片加载、价格为正、列表与详情信息相符；AC-PRODUCT-003：可打开对应详情；AC-PRODUCT-004：指定对照账号商品数据一致；AC-PRODUCT-005：可返回列表；AC-PRODUCT-006：刷新后商品仍可用 | TC-007～TC-015 均 Pass；特殊账号现象见 BUG-001、BUG-002 |
| US-CART-001 | 能增删并查看购物车商品 | AC-CART-001：加入后角标增加；AC-CART-002：角标与两件商品数量一致；AC-CART-003：删除后商品行消失；AC-CART-004：购物车名称与所加入商品一致 | TC-016～TC-018 均 Pass；特殊账号限制见 BUG-005 |
| US-CHECKOUT-001 | 能校验必填信息并完成购物 | AC-CHECKOUT-001：名字为空时不能继续；AC-CHECKOUT-002：姓氏或邮编为空时不能继续；AC-CHECKOUT-003：有效信息可完成订单；AC-CHECKOUT-004：显示订单完成提示 | TC-019、TC-020、EXT-002、EXT-003 均 Pass；特殊账号字段异常见 BUG-004 |
| US-CHECKOUT-002 | 避免生成没有商品的订单 | AC-CHECKOUT-005：购物车为空时禁止提交订单（项目提出的业务规则建议） | NC-001 为 Fail，行为已确认，见 BUG-003 |

验收标准均有对应执行记录。AC-CHECKOUT-002 仅针对两个字段的空值，不表示验证了非空无效邮编。建议规则与普通功能分开统计；需求映射见 [追踪表](trace.md)。
