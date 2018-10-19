<template>
  <div class="weidian-data">
    <page-title :list="list"></page-title>
    <div class="weidian-content">
      <w-tab :list="tab_list"  @wTabClick="wTabClick"></w-tab>

      <div class="time-outside" style="margin-top: 0.2rem">
        <div class="time-text">时间段：</div>
        <div class="time-box">
          <el-date-picker v-model="time" type="daterange" start-placeholder="开始日期" range-separator="至" end-placeholder="结束日期"></el-date-picker>
        </div>
        <!--<div class="outside-btn">下载报表</div>-->
      </div>

      <div v-if="page == '总PV'">
        <div class="content-row">
          <div class="content-box width-25">
            <div class="box-row-a title-text row-2-1">总PV</div>
            <div class="box-row-b hex-text row-2-2">29</div>
          </div>
          <div class="content-box width-25">
            <div class="box-row-a title-text row-2-1">内部页面PV</div>
            <div class="box-row-b hex-text row-2-2">12</div>
          </div>
          <div class="content-box width-25">
            <div class="box-row-a title-text row-2-1">二维码PV</div>
            <div class="box-row-b hex-text row-2-2">80</div>
          </div>
          <div class="content-box width-25">
            <div class="box-row-a title-text row-2-1">邀请相关PV</div>
            <div class="box-row-b hex-text row-2-2">150</div>
          </div>
        </div>

        <div class="content-row">
          <div class="content-box width-25">
            <div class="box-row-a title-text row-2-1">跳失率</div>
            <div class="box-row-b hex-text row-2-2">29%</div>
          </div>
          <div class="content-box width-25">
            <div class="box-row-a title-text row-2-1">人均浏览时长（小时）</div>
            <div class="box-row-b hex-text row-2-2">12</div>
          </div>
          <div class="content-box width-25">
            <div class="box-row-a title-text row-2-1">人均浏览页面量（页）</div>
            <div class="box-row-b hex-text row-2-2">56</div>
          </div>
        </div>
      </div>

      <div v-if="page == '店主数据'">
        <div>
          <div class="hex-title">店主</div>
          <div class="content-row">
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">外部流量</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">商品流量</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">推广流量</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">页面流量</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
          </div>
        </div>

        <div>
          <div class="hex-title">店主外部流量</div>
          <div class="content-row">
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">TOP10页面</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">搜索引擎</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">微信</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">链接</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">pv</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
          </div>
        </div>

        <div>
          <div class="hex-title">店主商品流量</div>
          <div class="content-row">
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">商品总PV</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">商品转发总PV</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">识别二维码进入总PV</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">店主标识链接进入总PV</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">商品加入收藏夹总次数</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">从收藏夹点击进入的商品总PV</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">购物车停留平均时间</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
          </div>
        </div>

        <div>
          <div class="hex-title">大礼包商品概况</div>
          <div class="table-box">
            <el-table :data="giftBagList" border style="width: 100%" v-loading="giftBagLoading">
              <el-table-column prop="cotype" label="礼包名称"></el-table-column>
              <el-table-column prop="cotype" label="商品PV"></el-table-column>
              <el-table-column prop="cotype" label="直接购买订单提交次数"></el-table-column>
              <el-table-column prop="cotype" label="未付款失效订单数"></el-table-column>
              <el-table-column prop="cotype" label="用券购买订单数"></el-table-column>
              <el-table-column prop="cotype" label="购买转化率"></el-table-column>
            </el-table>
          </div>
        </div>

        <div>
          <div class="hex-title">店主推广流量</div>
          <div>
            <div class="white-title">一、店主商品转发PV</div>
            <div class="content-row">
              <div class="content-box width-20">
                <div class="box-row-a title-text row-2-3">用户点击进入PV</div>
                <div class="box-row-b hex-text row-2-4">29</div>
              </div>
              <div class="content-box width-20">
                <div class="box-row-a title-text row-2-3">商品销售订单数（笔）</div>
                <div class="box-row-b hex-text row-2-4">12</div>
              </div>
              <div class="content-box width-20">
                <div class="box-row-a title-text row-2-3">商品销售件数（件）</div>
                <div class="box-row-b hex-text row-2-4">29</div>
              </div>
            </div>
          </div>

          <div>
            <div class="white-title">二、我的-邀请开店PV</div>
            <div class="content-row">
              <div class="content-box width-20">
                <div class="box-row-a title-text row-2-3">店主发出邀请按钮PV</div>
                <div class="box-row-b hex-text row-2-4">29</div>
              </div>
              <div class="content-box width-20">
                <div class="box-row-a title-text row-2-3">普通用户打开PV</div>
                <div class="box-row-b hex-text row-2-4">12</div>
              </div>
              <div class="content-box width-20">
                <div class="box-row-a title-text row-2-3">普通用户领取PV</div>
                <div class="box-row-b hex-text row-2-4">29</div>
              </div>
              <div class="content-box width-20">
                <div class="box-row-a title-text row-2-3">普通用户放弃PV</div>
                <div class="box-row-b hex-text row-2-4">29</div>
              </div>
              <div class="content-box width-20">
                <div class="box-row-a title-text row-2-3">优惠券过期提示PV</div>
                <div class="box-row-b hex-text row-2-4">29</div>
              </div>
            </div>
          </div>

          <div class="white-title">三、我的-邀请专粉PV</div>
          <div>
            <div class="white-title">1、店主发出邀请页面邀请</div>
            <div class="content-row">
              <div class="content-box width-20">
                <div class="box-row-a title-text row-2-3">店主发出邀请页面邀请PV</div>
                <div class="box-row-b hex-text row-2-4">29</div>
              </div>
              <div class="content-box width-20">
                <div class="box-row-a title-text row-2-3">普通用户打开PV</div>
                <div class="box-row-b hex-text row-2-4">12</div>
              </div>
              <div class="content-box width-20">
                <div class="box-row-a title-text row-2-3">普通用户领取优惠券PV</div>
                <div class="box-row-b hex-text row-2-4">29</div>
              </div>
              <div class="content-box width-20">
                <div class="box-row-a title-text row-2-3">普通用户放弃优惠券PV</div>
                <div class="box-row-b hex-text row-2-4">29</div>
              </div>
            </div>
          </div>
          <div>
            <div class="white-title">2、店主发出海报</div>
            <div class="content-row">
              <div class="content-box width-20">
                <div class="box-row-a title-text row-2-3">店主发出海报PV</div>
                <div class="box-row-b hex-text row-2-4">29</div>
              </div>
              <div class="content-box width-20">
                <div class="box-row-a title-text row-2-3">普通用户打开PV</div>
                <div class="box-row-b hex-text row-2-4">12</div>
              </div>
              <div class="content-box width-20">
                <div class="box-row-a title-text row-2-3">普通用户领取优惠券PV</div>
                <div class="box-row-b hex-text row-2-4">29</div>
              </div>
              <div class="content-box width-20">
                <div class="box-row-a title-text row-2-3">普通用户放弃优惠券PV</div>
                <div class="box-row-b hex-text row-2-4">29</div>
              </div>
            </div>
          </div>
        </div>

        <div>
          <div class="hex-title">店主页面流量</div>
          <div class="white-title">店主任务</div>
          <div class="table-box">
            <el-table :data="taskList" border style="width: 100%" v-loading="taskLoading">
              <el-table-column prop="cotype" label="任务等级"></el-table-column>
              <el-table-column prop="cotype" label="弹框展示数"></el-table-column>
              <el-table-column prop="cotype" label="完成人数"></el-table-column>
              <el-table-column prop="cotype" label="所用小时平均值"></el-table-column>
              <el-table-column prop="cotype" label="1PV"></el-table-column>
              <el-table-column prop="cotype" label="1完成人数"></el-table-column>
              <el-table-column prop="cotype" label="2PV"></el-table-column>
              <el-table-column prop="cotype" label="2完成人数"></el-table-column>
              <el-table-column prop="cotype" label="3PV"></el-table-column>
              <el-table-column prop="cotype" label="3完成人数"></el-table-column>
              <el-table-column prop="cotype" label="4PV"></el-table-column>
              <el-table-column prop="cotype" label="4完成人数"></el-table-column>
            </el-table>
          </div>
        </div>

        <div>
          <div class="white-title">首页</div>
          <div class="content-row">
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">上新</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">特卖</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">爆款</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">预售</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">首页banner1</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">首页banner2</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">首页banner3</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">首页banner4</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">活动弹框PV</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">活动弹框二跳PV</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
          </div>
        </div>

        <div>
          <div class="white-title">客服</div>
          <div class="content-row">
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">客服</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
          </div>
        </div>

        <div>
          <div class="white-title">发现</div>
          <div class="content-row">
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">每日十荐</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">素材圈-精选</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">素材圈-心灵鸡汤</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">素材圈-店主招募</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">素材圈-新手必发</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">公告</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">教程</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
          </div>
        </div>

        <div>
          <div class="white-title">我的PV</div>
          <div class="content-row">
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">我的收益二跳PV</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">额外奖励PV</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">额外奖励弹框点击PV</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">销售订单查看更多PV</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">自买订单查看更多PV</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">我的收藏PV</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">赚钱学院PV</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">我的导师PV</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
          </div>
        </div>
      </div>

      <div v-if="page == '非店主数据'">
        <div>
          <div class="hex-title">普通用户</div>
          <div class="content-row">
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">外部流量</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">商品流量</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">页面流量</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
          </div>
        </div>

        <div>
          <div class="hex-title">普通用户外部流量</div>
          <div class="content-row">
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">TOP10页面</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">搜索引擎</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">微信</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">链接</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">pv</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
          </div>
        </div>

        <div>
          <div class="hex-title">普通用户商品流量</div>
          <div class="content-row">
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">商品总PV</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">商品转发（普通转普通）</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">商品加入收藏夹次数</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">从收藏夹点击进入的商品PV</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">购物车停留平均时间</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
          </div>
        </div>

        <div>
          <div class="hex-title">普通用户页面流量</div>
          <div class="white-title">首页</div>
          <div class="content-row">
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">上新</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">特卖</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">爆款</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">预售</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">首页banner1</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">首页banner2</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">首页banner3</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">首页banner4</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">活动弹框PV</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">活动弹框二跳PV</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
          </div>
        </div>

        <div>
          <div class="white-title">客服</div>
          <div class="content-row">
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">客服</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
          </div>
        </div>

        <div>
          <div class="white-title">发现</div>
          <div class="content-row">
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">每日十荐</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">发现弹框（我要成为店主二跳）</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
          </div>
        </div>

        <div>
          <div class="white-title">我的PV</div>
          <div class="content-row">
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">收藏夹</div>
              <div class="box-row-b hex-text row-2-4">29</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">快速投诉通道</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">关注公众号</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">最下方bannerPV</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
            <div class="content-box width-20">
              <div class="box-row-a title-text row-2-3">最下方banner二跳中购买礼包按钮点击次数</div>
              <div class="box-row-b hex-text row-2-4">12</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import wTab from '../../components/common/wTab';
  import api from '../../api/api';
  import axios from 'axios';

  export default {
    data() {
      return {
        name: '流量概况',
        list: [                   // 标题list
          { name: "首页", url: "index", active: false },
          { name: "交易概况", url: "trading", active: false },
          { name: "流量概况", url: "flow", active: true },
          { name: "转化概况", url: "conversion", active: false },
          { name: "会员概况", url: "user", active: false },
          { name: "佣金概况", url: "commission", active: false },
          { name: "优惠券概况", url: "coupons", active: false }
        ],
        tab_list: [               // 顶部导航的list
          { id: "", name: "总PV", active: true },
          { id: "", name: "店主数据", active: false },
          { id: "", name: "非店主数据", active: false }
        ],
        time: "",                 // 时间段
        page: "总PV",             // 默认页面
        giftBagList: [],          // 礼包list
        giftBagLoading: false,    // 礼包表格加载中
        taskList: [],             // 店主任务list
        taskLoading: false,       // 店主任务表格加载中
      }
    },
    components:{ pageTitle, wTab },
    methods: {
      // 顶部导航的点击事件
      wTabClick(i){
        let arr = [].concat(this.tab_list);
        for(let a = 0; a < arr.length; a ++){
          arr[a].active = false;
        }
        arr[i].active = true;
        this.page = arr[i].name;
        this.tab_list = [].concat(arr);
      },
    },
    mounted() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/data.less";

</style>
