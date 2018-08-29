
const title = 'http://120.79.182.43:7443';

const api={
  login: title + '/user/login',//用户登录
  get_all_banner: title + '/banner/get_all',//获取首页轮播图
  get_all_hotmessage: title + '/hotmessage/get_all',//获取首页热文
  get_all_activity: title + '/activity/get_all',//获取首页/发现页活动
  get_all_topnav:title + '/topnav/get_all',//获取导航
}

export default api
