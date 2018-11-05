// const title ='https://daaiti.cn/';
const title ='https://weidian.daaiti.cn/';
// const title ='https://dsn.apizza.net/mock/e4811e0cd9658bcb8efa01d13fee5608/';

const api={
  login: title + 'super/login',       // 管理员登录

  get_all_task_level: title + 'task/get_all_task_level',    // 获取所有任务等级
  edit_task_level: title + 'task/add_or_update_task_level', // 添加或更新任务等级
  get_all_task_type: title + 'task/get_all_task_type',      // 获取任务类型
  get_all_task: title + 'task/get_all_task',                // 获取所有任务
  // get_all_raward: title + 'task/get_all_raward',         // 获取所有奖励
  add_task: title + 'task/add_task',                        // 添加或更新任务
  del_task: title + 'task/del_task',                        // 删除任务
  del_task_level: title + 'task/del_task_level',            // 删除任务等级

  get_bigactivitys: title + 'bigactivity/get_bigactivitys', // 获取专题列表-后台
  get_all_hot_message: title + 'hotmessage/get_all',        // 获取全部热文 - 首页
  add_one_hot_message: title + 'hotmessage/add_one',        // 添加热文 - 首页
  update_one_hot_message: title + 'hotmessage/update_one',  // 编辑热文 - 首页
  get_activity_list_by_actitle: title + 'activity/get_activity_list_by_actitle',  // 模糊搜索公告/教程
  create_hbact: title + 'bigactivity/create_hbact',         // 添加首页专题（轮播图）
  create_dbact: title + 'bigactivity/create_dbact',         // 添加发现页专题（轮播图）
  update_bact: title + 'bigactivity/update_bact',           // 修改专题/删除轮播图（测试）
  get_home: title + 'topnav/get_home',                      // 获取上部导航 - 首页
  get_dp: title + 'topnav/get_dp',                          // 获取上部导航 - 发现页
  get_all_topnav: title + 'topnav/get_all_topnav',          // 获取所有导航
  get_all_activity: title + 'activity/get_all',             // 获取首页/发现页活动/推文内容列表
  add_one_activity: title + 'activity/add_one',             // 添加首页活动/推文（测试）
  update_act: title + 'activity/update_act',                // 修改/删除活动/推文 - 首页/发现页
  get_search: title + 'searchfield/get_search',             // 搜索推文内容
  add_to_bigact: title + 'bigactivity/add_to_bigact',       // 将推文批量添加到专题
  get_info: title + 'recommend/get_info',                   // 获取每日推荐商品部分 - 发现页
  update: title + 'recommend/update',                       // 添加/修改/删除每日推荐商品 - 发现页
  get_comment_with_apply: title + 'activitycomment/get_comment_with_apply',   // 获取推文下的评论-嵌套回复
  add_comment: title + 'activitycomment/add_comment',       // 回复评论
  del_comment: title + 'activitycomment/del_comment',       // 删除评论

  hand_out_reward: title + 'reward/hand_out_reward',        // 平台内发放优惠券
  admin_giving_reward: title + 'reward/admin_giving_reward',// 运营给用户赠送优惠券
  get_grant_record: title + 'reward/get_grant_record',      // 运营赠券记录
  search_user: title + 'user/search_user',                  // 通过手机号或昵称查找用户
  get_all_raward: title + 'task/get_all_raward',            // 获取所有奖励 - 获取所有优惠券
  create_reward: title + 'reward/create_reward',            // 创建优惠券
  update_reward: title + 'reward/update_reward',            // 编辑优惠券所属集合或删除
  get_reward_packets: title + 'reward/get_reward_packets',  // 获取所有优惠券集合名
  create_rewardpacket: title + 'reward/create_rewardpacket',// 新建优惠券集合
  del_rewardpacket: title + 'reward/del_rewardpacket',      // 删除优惠券集合名
  get_r_p_detail: title + 'reward/get_reward_packet_detail',// 查看券集合具体包含

  get_order_count: title + 'order/admin_get_order_count',   // 后台获取订单数量
  get_order_list: title + 'order/admin_get_order_list',     // 后台获取各状态下的订单
  get_kd_list: title + 'order/get_kd_list',                 // 获取快递列表
  send_order: title + 'order/send_order',                   // 商品发货
  agree_refund: title + 'order/agree_refund',               // 同意退货/退款的申请
  solder_confirm: title + 'order/solder_confirm',           // 卖家确认收货(订单)
  solder_change_send: title + 'order/solder_change_send',   // 卖家退货(换货)发货(订单)
  delete_order: title + 'order/delete_order',               // 删除订单
  cancle_order: title + 'order/cancle_order',               // 取消订单

  update_info: title + 'super/update_info',                 // 修改管理员自身基本信息
  get_all_suser: title + 'super/get_all_suser',             // 获取管理员列表
  add_admin: title + 'super/add_admin',                     // 添加普通管理员
  update_admin: title + 'super/update_other_admin',         // 超管管理其他管理
  get_all_user: title + 'user/get_all_user',                // 获取所有用户信息
  get_user_sub: title + 'user/get_user_sub',                // 获取用户下级

  set_show_type: title + 'activity/set_show_type',          // 控制中心 - 设置首页专题默认的过滤类型
  get_show_type: title + 'activity/get_show_type',          // 控制中心 - 获取首页默认的过滤类型
  get_schedual: title + 'mycenter/get_schedual_show',       // 控制中心 - 获取控制中心显隐
  set_schedual: title + 'mycenter/set_schedual_show',       // 控制中心 - 设置控制中心显隐
  get_share_params: title + 'mycenter/get_share_params',    // 控制中心 - 获取微信分享参数
  set_share_params: title + 'mycenter/set_share_params',    // 控制中心 - 设置微信分享参数

  // upload_task_img: title + 'task/upload_task_img',       // 上传任务图标-上传图片
  upload_task_img: title + 'activity/upload_home_images',   // 上传图片
  add_image: title + 'adimage/add_image',                   // 弹框管理的添加图片
  get_img_by_aitype: title + 'adimage/get_image_by_aitype', // 通过类型获取弹框图

  get_all_tags: title + 'activity/get_all_tags',            // 获取推文角标
  upload_tags: title + 'activity/upload_tags',              // 上传角标
  del_exist_tags: title + 'activity/del_exist_tags',        // 删除角标

  get_all_complain: title + 'complain/get_all',             // 查看投诉记录
  update_status: title + 'complain/update_status',          // 更新投诉状态

  get_product: title + 'product/get_all',                   // 模糊搜索商品 - 全部商品
  get_list: title + 'product/get_list',                     // 获取商品池商品list
  get_one: title + 'product/get_one',                       // 获取单条商品--商品详情页
  get_p_b: title + 'product/get_product_bigactivity',       // 获取所在专题详情 - 商品池
  update_p_b: title + 'product/update_product_bigactivity', // 更新商品所在专题 - 商品池
  update_p_p: title + 'product/update_product_prtarget',    // 更新商品所在模块 - 商品池
  get_product_record: title + 'product/get_product_record', // 获取商品操作记录
  shelf_product_or_claim_act: title + 'product/shelf_product_or_claim_act', // 商品上下架 / 认领推文 - 商品池
  update_sku_price: title + 'product/update_sku_price',     // 更新sku里的价格 - 商品池
};

export default api
