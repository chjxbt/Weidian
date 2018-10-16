
// const title = 'http://10.0.0.63:7443';
// const title = 'http://120.79.182.43:7443';
const title = 'https://weidian.daaiti.cn';

const api={
  login: title + '/user/login',//用户登录
  wx_login:title + '/user/wx_login',//微信登录
  get_accesstoken : title + '/user/get_accesstoken',
  get_config: title + '/user/get_wx_config',//
  get_all_banner: title + '/banner/get_all',//获取首页轮播图
  get_home_banner: title + '/bigactivity/get_home_banner',//获取首页轮播图(测试)
  get_all_hotmessage: title + '/hotmessage/get_all',//获取首页热文
  get_all_activity: title + '/activity/get_all',//获取首页/发现页活动
  get_home_topnav:title + '/topnav/get_home',//获取首页导航
  ac_like: title +'/activitylike/ac_like',//首页点赞
  get_search: title + '/searchfield/get_search',//首页搜索

  get_dp_topnav: title + '//topnav/get_dp',//获取上部导航 - 发现页
  get_info_recommend: title + '/recommend/get_info',//获取每日推荐内容 - 发现页
  get_all_recommendbanner: title + '/recommendbanner/get_all',//获取上部轮播图 - 发现页
  get_discover_banner: title + '/bigactivity/get_discover_banner',//获取上部轮播图 - 发现页(测试)
  re_like: title +'/recommendlike/re_like',//每日推荐的点赞 - 发现页
  add_comment: title +'/activitycomment/add_comment',//添加评论-教程/公告 - 发现页
  get_list: title +'/activitycomment/get_list',//获取活动下的评论(包括回复) - 首页/发现页
  share_qrcode: title +'/activity/share_qrcode',//分享二维码
  generate_poster: title + '/activity/generate_poster',//合成图片

  get_order_count: title + '/order/get_count',//获取订单数
  get_more_order: title + '/order/get_more',//获取所有订单
  get_list_order: title + '/order/get_list',//获取各状态订单
  get_info_mycenter: title + '/mycenter/get_info',//获取基本信息
  get_account_info: title + '/mycenter/get_account_info',//获取个人信息
  add_one_complain: title + '/complain/add_one',//投诉
  get_prlike_productlike: title + '/productlike/get_prlike',//收藏
  batch_del_productlike:title + '/productlike/batch_del',//删除收藏
  // get_myimg_adimage: title + '/adimage/get_myimg',//获取我的底部图片
  get_image_by_aitype: title +'/adimage/get_image_by_aitype',//获取弹框图片

  get_address : title +'/mycenter/get_address',//获取收获地址
  add_address: title +'/mycenter/add_address',//添加地址
  del_address: title +'/mycenter/del_address',//删除地址
  update_address: title +'/mycenter/update_address',//更新地址
  get_bank_list: title +'/mycenter/get_bank_list',//获取银行卡
  add_bankcard: title +'/mycenter/add_bankcard',//添加银行卡
  get_mybankcard: title +'/mycenter/get_mybankcard',//获取银行卡
  get_province: title +'/mycenter/get_province',//获取省
  get_city: title +'/mycenter/get_city',//获取市
  get_area: title +'/mycenter/get_area',//获取区
  get_inforcode: title +'/mycenter/get_inforcode',//获取验证码
  verify_inforcode: title +'/mycenter/verify_inforcode',//验证验证码
  update_bankcard:title +'/mycenter/update_bankcard',//修改银行卡
  del_bankcard: title +'/mycenter/del_bankcard',//解除
  get_user_task: title + '/task/get_user_task',//获取任务
  do_task: title +'/task/do_task',//做任务
  get_bigactivity : title + '/bigactivity/get_bigactivity',//专题页
  get_one_product: title + '/product/get_one',//获取商品详情
  add_one_productlike:title + '/productlike/add_one',//商品点赞
  get_list_shoppingcart: title + '/shoppingcart/get_list',//获取购物车
  delete_shoppingcart: title +'/shoppingcart/delete',//删除购物车
  update_shoppingcart: title + '/shoppingcart/update',///更新购物车
  get_share_params: title + '/mycenter/get_share_params',//获取分享参数
};

export default api
