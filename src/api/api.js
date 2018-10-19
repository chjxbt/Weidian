// const title ='https://daaiti.cn/';
const title ='https://weidian.daaiti.cn/';

const api={
  login: title + 'super/login',       // 管理员登录

  get_all_task_level: title + 'task/get_all_task_level',    // 获取所有任务等级
  edit_task_level: title + 'task/add_or_update_task_level', // 添加或更新任务等级
  get_all_task_type: title + 'task/get_all_task_type',      // 获取任务类型
  get_all_task: title + 'task/get_all_task',                // 获取所有任务
  // get_all_raward: title + 'task/get_all_raward',            // 获取所有奖励
  add_task: title + 'task/add_task',                        // 添加或更新任务
  del_task: title + 'task/del_task',                        // 删除任务
  del_task_level: title + 'task/del_task_level',            // 删除任务等级

  get_bigactivitys: title + 'bigactivity/get_bigactivitys', //获取专题列表-后台
  get_all_hot_message: title + 'hotmessage/get_all',        //获取全部热文 - 首页
  add_one_hot_message: title + 'hotmessage/add_one',        //添加热文 - 首页
  update_one_hot_message: title + 'hotmessage/update_one',  //编辑热文 - 首页
  get_product: title + 'product/get_all',                   //模糊搜索商品
  get_activity_list_by_actitle: title + 'activity/get_activity_list_by_actitle',  //模糊搜索公告/教程
  create_hbact: title + 'bigactivity/create_hbact',         // 添加首页专题（轮播图）
  create_dbact: title + 'bigactivity/create_dbact',         // 添加发现页专题（轮播图）
  update_bact: title + 'bigactivity/update_bact',           // 修改专题/删除轮播图（测试）
  get_home: title + 'topnav/get_home',                      // 获取上部导航 - 首页
  get_dp: title + 'topnav/get_dp',                          // 获取上部导航 - 发现页
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

  get_all_raward: title + 'task/get_all_raward',            // 获取所有奖励 - 获取所有优惠券
  create_reward: title + 'reward/create_reward',            // 创建优惠券
  hand_out_reward: title + 'reward/hand_out_reward',        // 平台内发放优惠券

  get_order_count: title + 'order/admin_get_order_count',   // 后台获取订单数量
  get_order_list: title + 'order/admin_get_order_list',     // 后台获取各状态下的订单
  get_kd_list: title + 'order/get_kd_list',                 // 获取快递列表
  send_order: title + 'order/send_order',                   // 商品发货

  update_info: title + 'super/update_info',                 // 修改管理员自身基本信息
  get_all_suser: title + 'super/get_all_suser',             // 获取管理员列表
  add_admin: title + 'super/add_admin',                     // 添加普通管理员
  update_admin: title + 'super/update_other_admin',         // 超管管理其他管理

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

};

export default api
