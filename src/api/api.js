// const title ='https://daaiti.cn/';
const title ='https://weidian.daaiti.cn/';

const api={
  login: title + 'super/login',       // 管理员登录

  get_all_task_level: title + 'task/get_all_task_level',    // 获取所有任务等级
  get_all_task_type: title + 'task/get_all_task_type',      // 获取任务类型
  get_all_task: title + 'task/get_all_task',                // 获取所有任务
  add_task: title + 'task/add_task',                        // 添加或更新任务

  get_bigactivitys: title + 'bigactivity/get_bigactivitys', //获取专题列表-后台
  get_all_hot_message: title + 'hotmessage/get_all',        //获取全部热文 - 首页
  add_one_hot_message: title + 'hotmessage/add_one',        //添加热文 - 首页
  update_one_hot_message: title + 'hotmessage/update_one',  //编辑热文 - 首页
  get_product: title + 'product/get_all',                   //模糊搜索商品
  get_activity_list_by_actitle: title + 'activity/get_activity_list_by_actitle',//模糊搜索公告/教程
  create_hbact: title + 'bigactivity/create_hbact',   // 添加首页专题（轮播图）
  create_dbact: title + 'bigactivity/create_dbact',   // 添加发现页专题（轮播图）
  update_bact: title + 'bigactivity/update_bact',     // 修改专题/删除轮播图（测试）
  get_home: title + 'topnav/get_home',                // 获取上部导航 - 首页
  get_dp: title + 'topnav/get_dp',                    // 获取上部导航 - 发现页
  get_all_activity: title + 'activity/get_all',       // 获取首页/发现页活动/推文内容列表
  add_one_activity: title + 'activity/add_one',       // 添加首页活动/推文（测试）
  update_act: title + 'activity/update_act',          // 修改/删除活动/推文 - 首页/发现页
  add_to_bigact: title + 'bigactivity/add_to_bigact', // 将推文批量添加到专题
  get_info: title + 'recommend/get_info',             // 获取每日推荐商品部分 - 发现页
  update: title + 'recommend/update',                 // 添加/修改/删除每日推荐商品 - 发现页

  update_info: title + 'super/update_info',           // 修改管理员自身基本信息
  get_all_suser: title + 'super/get_all_suser',       // 获取管理员列表
  add_admin: title + 'super/add_admin',               // 添加普通管理员
  update_admin: title + 'super/update_other_admin',   // 超管管理其他管理

  set_show_type: title + 'activity/set_show_type',    // 控制中心 - 设置首页专题默认的过滤类型
  get_show_type: title + 'activity/get_show_type',    // 控制中心 - 获取首页默认的过滤类型
  get_schedual: title + 'mycenter/get_schedual_show', // 控制中心 - 获取控制中心显隐
  set_schedual: title + 'mycenter/set_schedual_show', // 控制中心 - 设置控制中心显隐

  // upload_task_img: title + 'task/upload_task_img',         // 上传任务图标-上传图片
  upload_task_img: title + 'activity/upload_home_images',     // 上传图片
  add_image: title + 'adimage/add_image',                     // 弹框管理的添加图片
  get_image_by_aitype: title + 'adimage/get_image_by_aitype', // 通过类型获取弹框图









/*  changePwd: title + 'user/update_user',//修改密码
  get_inforcode:title + 'user/get_inforcode',//获取验证码
  forget_password:title + 'user/forget_password',//忘记密码
  get_approval: title + 'approval/get_approval',//获取审批信息
  update_approval:title + 'approval/update_approval',//同意/拒绝
  get_userIndex: title + 'user/get_situation',//获取用户首页

  get_order_situation: title + 'order/get_order_situation',//获取订单概况
  get_all_order: title + 'order/order_list',//获取所有订单
  get_order_by_LOid: title + 'order/order_abo',//获取订单详情
  get_omfilter: title + 'order/get_omfilter',//获取订单filter
  update_order_status: title + 'order/update_order_status',//更新订单状态

  get_managers: title + 'user/get_managers',//获取管理员列表
  update_manager_by_matel: title + 'user/update_manager_by_matel',//封禁/取消封禁管理员
  get_users: title + 'user/get_users',//获取用户信息列表
  update_users: title + 'user/update_users',//封禁/取消封禁用户

  get_all_product: title + 'product/get_all',//获取所有商品
  release_product: title + 'product/release',//发布商品商品
  update_pro_info:title + 'product/update_pro_info',//更新商品
  update_product : title + 'product/update_product',//上下架商品
  upload_files: title +'other/upload_files',//上传图片
  get_prid: title + 'product/get_prid',//获取商品id
  get_abo:title + 'product/get_abo',//获取商品详情

  get_first_category: title + 'category/get_first',//获取类目
  get_child_category:title + 'category/get_child',//获取子类目
  get_categorybrands: title + 'category/get_categorybrands',//根据类目id获取商品属性
  get_category_by_prname: title + 'category/get_category_by_prname',//搜索商品对应的类目
  get_ctlist_by_ctid: title + 'category/get_ctlist_by_ctid',//根据最后一层CTid获取对应的类目

  create: title + 'card/create',//创建活动/优惠券
  get_all_card: title + 'card/get_all',//获取优惠券/活动
  get_situation:title + 'card/get_situation',//获取活动或优惠券概况
  update_active_status:title +'card/update_active_status',//更新优惠券状态
  get_acabo:title + 'card/get_acabo',//获取活动和优惠券详情
  */

};

export default api
