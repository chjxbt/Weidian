# -*- coding:utf8 -*-
from datetime import datetime

from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy import Column, create_engine, Integer, String, Text, Float, Boolean, orm, DateTime, DECIMAL
from WeiDian.config import dbconfig as cfg
from WeiDian.models.base_model import BaseModel, auto_createtime
import json


DB_PARAMS = "{0}://{1}:{2}@{3}/{4}?charset={5}".format(
    cfg.sqlenginename,
    cfg.username,
    cfg.password,
    cfg.host,
    cfg.database,
    cfg.charset)
mysql_engine = create_engine(DB_PARAMS, echo=False, pool_size=10, max_overflow=20, pool_pre_ping=True)


class Activity(BaseModel):
    """
    活动
    """
    __tablename__ = 'activity'
    ACid = Column(String(64), primary_key=True)
    BAid = Column(String(64))  # 该推文所属专题id
    SUid = Column(String(64), nullable=False)  # 发布者(超级用户才可以发布)
    ACtype = Column(Integer, default=0)  # 活动分类, 具体分类如下
    # {0 普通动态, 1 满减, 2 满赠, 3 优惠券, 4 砍价, 5 拼团, 6 单品优惠券, 7 一元秒杀, 8 前几分钟半价, 9 限时抢, 10 X元X件}
    TopnavId = Column(String(64))  # 对应上层导航栏
    ACtext = Column(Text, nullable=False)  # 活动文字详情
    AClikenum = Column(Integer, default=0)  # 喜欢数
    AClikeFakeNum = Column(Integer)  # 可编辑的喜欢数量, 如果留空, 则使用实际的喜欢数量
    ACbrowsenum = Column(Integer, default=0)  # 浏览数
    ACforwardFakenum = Column(Integer, default=0)  # 虚假转发数
    ACProductsSoldFakeNum = Column(Integer)  # 可编辑的商品销量, 如果留空,  则使用实际的销量
    ACcreatetime = Column(String(14))  # 活动的创建时间
    ACupdatetime = Column(String(14))  # 活动的修改时间
    ACstarttime = Column(String(14))  # 活动开始时间
    ACendtime = Column(String(14))  # 活动结束时间
    ACisended = Column(Boolean, default=False)  # 是否被手动截止
    ACisdelete = Column(Boolean, default=False)  # 是否删除
    ACistop = Column(Boolean, default=False)  # 是否置顶
    ACtitle = Column(Text)  # 活动标题（公告、教程页）
    ACeditstatus = Column(Integer, default=0)  # 推文状态{0:草稿, 1:上架, 2:下架}
    AClinkvalue = Column(String(64), default=0)  # 具体跳转的id
    ACSkipType = Column(Integer, default=0)  # 跳转类型{0:无跳转类型, 1:专题, 2:商品}


    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = [
            'ACid',
            'ACtype',
            'ACtext',
            'ACbrowsenum',
            'ACcreatetime',
            'ACstarttime',
            'ACendtime',
            'ACistop',
            'ACisended',
            'TopnavId',
            'ACtitle',
            'ACSkipType',
            'ACeditstatus'
        ]


class ActivityComment(BaseModel):
    """
    活动评论, 以及评论回复
    """
    __tablename__ = 'activitycomment'
    ACOid = Column(String(64), primary_key=True)
    ACid = Column(String(64), nullable=False)  # 评论对应的活动)
    ACOparentid = Column(String(64))  # 所回复的评论(可以为空, 为空代表是评论)
    USid = Column(String(64), nullable=False)  # 发布评论(回复)的用户(管理员)
    ACtext = Column(String(255), nullable=False)  # 评论内容
    ACOcreatetime = Column(String(14))  # 时间
    ACisdelete = Column(Boolean, default=False)  # 是否删除
    ACOrobot = Column(String(16), comment=u'评论小马甲')

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['ACOid', 'USid', 'ACOcreatetime', 'ACtext']


class ActivityLike(BaseModel):
    """
    点赞
    """
    __tablename__ = 'like'
    ALid = Column(String(64), primary_key=True)
    ACid = Column(String(64), nullable=False)  # 活动
    USid = Column(String(64), nullable=False)  # 用户
    ALcreatetime = Column(String(14))  # 时间

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['ACid', 'ALcreatetime']


class ActivityMedia(BaseModel):
    """
    活动图片/视频
    """
    __tablename__ = 'activatymedia'
    AMid = Column(String(64), primary_key=True)
    ACid = Column(String(64), nullable=False)  # 商品图片对应的活动
    AMimage = Column(String(255))  # 图片对应的路径
    AMvideo = Column(String(255))  # 视频地址
    AMvideothumbnail = Column(String(255))  # 视频缩略图
    AMsort = Column(Integer)  # 图片的顺序, 用于表明图片的位置

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['AMid']


class ActivityTag(BaseModel):
    """
    活动右上角标
    """
    __tablename__ = 'activitytag'
    ATid = Column(String(64), primary_key=True)
    ACid = Column(String(64), nullable=False)  # 活动
    ATname = Column(String(255), nullable=False)  # 角标(后期确认改为图片)
    ATstate = Column(Integer, default=1)  # 显示状态: {1 显示, 0 隐藏}

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['ATid', 'ATname', 'ATstate']


class ActivityFoward(BaseModel):
    """
    活动转发
    """
    __tablename__ = 'activityfoward'
    AFid = Column(String(64), primary_key=True)
    USid = Column(String(64))  # 用户
    ACid = Column(String(64))  # 活动


class Product(BaseModel):
    """
    商品
    """
    __tablename__ = 'product'
    PRid = Column(String(64), primary_key=True)
    PRdetail = Column(LONGTEXT)  # 商品详情, 大文本
    PRmainpic = Column(String(255), nullable=False)  # 商品主图
    PRactivityid = Column(String(64))  # 活动id, 可能不需要
    Maketlias = Column(String(64))  # 店铺别名
    PRalias = Column(String(64))  # 别名
    PRimporturl = Column(String(255))  # 外部导入商品的url
    PRishot = Column(Boolean, default=False)  # 是否热卖
    PRtitle = Column(String(255))  # 商品标题
    PRname = Column(String(64), nullable=False)  # 名称
    # 商品编辑状态: {1 完成商品信息, 2 完成产品详情信息, 3, 完成??}
    PReditstate = Column(Integer, default=1)
    PRoldprice = Column(Float)  # 原价
    PRchannelname = Column(String(64))  # 渠道商名称, 暂未设置, 默认空
    PRchannelid = Column(String(64))  # 渠道商id, 暂未设置, 默认空
    PRsalesvolume = Column(Integer, default=0)  # 商品销量
    PRvipprice = Column(Float)  # 会员价格
    PRishhare = Column(Boolean, default=True)  # 是否共享
    SUid = Column(String(64))  # 发布者, 创建人
    PRcreatetime = Column(String(14))  # 创建时间
    SUmodifyid = Column(String(64))  # 认领推文运营id
    PRmodifytime = Column(String(14))  # 修改时间
    PRstatus = Column(Integer, default=1)  # 商品状态: {0 下架, 1 正常, 2 禁用}
    PRprice = Column(Float, nullable=False)  # 显示价格
    PRisdelete = Column(Boolean, default=False)  # 删除
    PRviewnum = Column(Integer, default=0)  # 浏览量
    PRfakeviewnum = Column(Integer)  # 虚拟浏览数
    PRfakelikenum = Column(Integer, default=0)  # 虚拟收藏数量
    PRsalefakenum = Column(Integer)  # 商品自定义销量
    PAid = Column(String(64))  # 类目id
    PRlogisticsfee = Column(Float)  # 物流费
    PRstock = Column(Integer)  # 商品详情页库存
    PRsalestatus = Column(String(64))  #我的-收藏夹
    PRoductId = Column(Integer)  # 微点系统商品id
    PRtarget = Column(String(64))  # {101: 首页, 102: 发现页}
    PRpushCode = Column(String(16))  # 微点推送人的标识
    # 新改动, 对应三级合伙人的佣金, 待定
    # PRdevideRate = Column(String(64), comment=u'佣金三级分成比例, json, ')  # {'one': 0.1, 'two': 0.2,..}

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = [
            'PRid',
            'PRmainpic',
            'PRimporturl',
            'PRishot',
            'PRtitle',
            'PRname',
            'PRprice',
            'PRoldprice',
            'PRchannelname',
            'PRchannelid',
            'SUid',
            'PRstock',
            'PRsalestatus',
            'PRtarget',
            'PRpushCode',
            'PRoductId'
        ]


class ProductSkuKey(BaseModel):
    """sku属性名"""
    __tablename__ = 'productskukey'
    PSKid = Column(String(64), primary_key=True)
    PRid = Column(String(64), nullable=False)  # 商品id
    PSVid = Column(String(64), nullable=False)  # 商品sku属性的value
    _PSKproperkey = Column(Text, nullable=False)  # 商品sku属性的key, json
    PSKproductnum = Column(Integer, nullable=False)  # 库存
    PSKalias = Column(String(64), nullable=False)  # 商品别名
    PSKprice = Column(DECIMAL(precision=28, scale=2), default=0.00)  # 价格
    PSKprofict = Column(Float, default=5, comment=u'利润')
    PSKpurchase = Column(Float, comment=u'进货价')
    PSKpostfee = Column(Float, nullable=False)  # 物流费
    PSKactiviyid = Column(String(64))  # 活动id, 不知用处
    PSskuid = Column(Integer)  # 微点商品sku id
    PSisdelete = Column(Integer, default=1)  # 属性是否删除 {0:删除, 1：正常}

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = self.all
        self.hide('_PSKproperkey', 'PRid').add('PSKproperkey')

    @property
    def PSKproperkey(self):
        return json.loads(self._PSKproperkey)

    @PSKproperkey.setter
    def PSKproperkey(self, raw):
        self._PSKproperkey = json.dumps(raw)


class ProductSkuValue(BaseModel):
    """sku属性值, 每一个商品对应一个此表"""
    __tablename__ = 'productskuvalue'
    PSVid = Column(String(64), primary_key=True)
    PRid = Column(String(64), nullable=False)  # 关联商品
    _PSVpropervalue = Column(Text, nullable=False)  # 商品sku的属性, json

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = self.all
        self.add('PSVpropervalue').hide('_PSVpropervalue')

    @property
    def PSVpropervalue(self):
        return json.loads(self._PSVpropervalue)

    @PSVpropervalue.setter
    def PSVpropervalue(self, raw):
        self._PSVpropervalue = json.dumps(raw)


class ProductImage(BaseModel):
    """商品展示图片"""
    __tablename__ = 'productimage'
    PIid = Column(String(64), primary_key=True)
    PRid = Column(String(64), nullable=False)    # 商品id
    PIurl = Column(String(255), nullable=False)  # 图片链接(七牛云)
    PIsort = Column(Integer)                     # 图片顺序
    PIexist = Column(Boolean, default=True)   # 图片是否存在 {0:不存在， 1:存在}

    @orm.reconstructor
    def __init__(self):
        self.fields = self.all


class ProductOperationRecord(BaseModel):
    """商品操作记录"""
    __tablename__ = 'productoperationrecord'
    PORid = Column(String(64), primary_key=True)
    PRid = Column(String(64), nullable=False)     # 商品id
    PORcreatetime = Column(String(14))            # 修改时间
    SUid = Column(String(64), nullable=False)     # 运营id
    PORtarget = Column(String(64))                # 操作对象id
    PORaction = Column(String(64))                # 具体操作

    @orm.reconstructor
    def __init__(self):
        self.fields = ['PRid', 'PORcreatetime', 'SUid', 'PORaction']


class ProductTarget(BaseModel):
    """商品关联模块"""
    __tablename__ = 'producttarget'
    PTid = Column(String(64), primary_key=True)
    PRid = Column(String(64), nullable=False)      # 商品id
    PRtarget = Column(String(64), nullable=False)  # 对应模块id


class ProductBigActivity(BaseModel):
    """商品关联专题"""
    __tablename__ = 'productbigactivity'
    PBid = Column(String(64), primary_key=True)
    PRid = Column(String(64), nullable=False)      # 商品id
    BAid = Column(String(64), nullable=False)      # 对应专题id

class ProductLike(BaseModel):
    """商品收藏(喜欢)"""
    __tablename__ = 'productlike'
    PLid = Column(String(64), primary_key=True)
    USid = Column(String(64), nullable=False)  # 用户
    PRid = Column(String(64), nullable=False)  # 商品
    PLcreatetime = Column(String(14))  # 创建时间

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = self.all


class Recommend(BaseModel):
    """每日十荐页中部商品区域"""
    __tablename__ = 'recommend'
    REid = Column(String(64), primary_key=True)
    SUid = Column(String(64), nullable=False)  # 管理员
    REcreatetime = Column(String(14))  # 创建时间
    REstarttime = Column(String(14))  # 该次推荐开始时间
    REendtime = Column(String(14))  # 该次推荐结束时间
    REviewnum = Column(Integer, default=0)  # 浏览量
    REfakeviewnum = Column(Integer)  # 虚拟浏览数
    RElikenum = Column(Integer, default=0)  # 喜欢数
    RElikefakenum = Column(Integer)  # 可编辑的喜欢数量, 如果留空, 则使用实际的喜欢数量
    REisdelete = Column(Boolean, default=False)  # 是否删除

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = [
            'REid',
            'SUid',
            'REcreatetime',
            'REstarttime',
            'REendtime']


class RecommendProduct(BaseModel):
    """每日十荐页商品滚动区域的中转表"""
    __tablename__ = 'recommendproduct'
    RPid = Column(String(64), primary_key=True)
    REid = Column(String(64), nullable=False)  # 关联的推荐商品区域
    PRid = Column(String(64), nullable=False)  # 关联的商品
    RPsort = Column(Integer)  # 商品顺序

    @orm.reconstructor
    def __init__(self):
        self.fields = self.all


class RecommendLike(BaseModel):
    """每日十荐页点赞笑脸"""
    __tablename__ = 'recommendlike'
    RLid = Column(String(64), primary_key=True)
    USid = Column(String(64))  # 用户id
    REid = Column(String(64))  # 推荐商品id
    RLcreatetime = Column(String(14))  # 推荐页点赞时间

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = self.all


class ShoppingCart(BaseModel):
    """购物车"""
    __tablename__ = 'shopingcart'
    SCid = Column(String(64), primary_key=True)
    USid = Column(String(64))  # 用户id
    PSKid = Column(String(64))  # 商品的选项id
    PRid = Column(String(64))  # 商品id, 冗余字段
    SCnums = Column(Integer)  # 数量

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['SCid', 'PRid', 'SCnums']


class OrderInfo(BaseModel):
    """订单信息"""
    __tablename__ = 'orderinfo'
    OIid = Column(String(64), primary_key=True)
    OIsn = Column(String(64))  # 订单号
    USid = Column(String(64))  # 用户
    OItradenum = Column(String(125))  # 交易号, (如果有)
    """
    订单状态: {0:全部, 1: 待付款, 2: 支付成功, 3: 支付超时关闭（交易关闭）, 4:待发货, 5: 已发货,
    6:已完成, 7:已取消, 8:交易失败（退货）,  10:待评价(评价放到), 11:退换货, 12: 换货(买家退回中),
    13: 换货(卖家发货中), 14: 卖家已发货
     }
    """
    OIpaystatus = Column(Integer, default=1)
    OIpaytype = Column(Integer)  # 支付类型: {0: 银行卡支付, 1: 微信支付}
    OIleavetext = Column(String(255))  # 订单留言
    OImount = Column(Float)  # 金额
    OIpaytime = Column(DateTime)  # 支付时间
    OIaddress = Column(String(255), nullable=False)  # 地址
    OIrecvname = Column(String(64), nullable=False)  # 收货人
    OIrecvphone = Column(String(16), nullable=False)  # 收货人电话
    OIcreatetime = Column(DateTime, default=datetime.now)  # 订单创建时间
    OIisdelete = Column(Boolean, default=False)  # 是否删除
    Sellerid = Column(String(64))  # 卖家id
    RAid = Column(String(64), comment=u'优惠券id')
    OIcomfirmtime = Column(DateTime, comment=u'确认收货时间')

    @orm.reconstructor
    def __init__(self):
        self.fields = self.all


class OrderProductInfo(BaseModel):
    """订单商品详情, 多个订单商品详情对应一个订单"""
    __tablename__ = 'orderproductinfo'
    OPIid = Column(String(64), primary_key=True)
    OIid = Column(String(64), nullable=False)  # 订单
    PRid = Column(String(64), nullable=False)  # 商品id
    # OPIsku = Column(Text, nullable=False)  # 订单中的sku值(无需存skuid)
    _PSKproperkey = Column(Text, nullable=False)  # 商品sku属性的key, json
    OIproductprice = Column(Float, nullable=False)   # 商品价格(购买时候的价格)单价
    OPIproductname = Column(String(64))  # 商品的名字(购买之时的)
    OPIproductimages = Column(String(255))  # 商品主图
    OPIproductnum = Column(Integer, default=1)  # 购买数量
    OPIstatus = Column(Integer, default=0, comment=u'0: 待发货, 1 待收货, 2 交易成功(未评价), 3 交易成功(已评价), 4 已签收')
    SmallTotal = Column(Float, nullable=False, comment=u'价格小计')

    OPIlogisticsSn = Column(String(64), comment=u'发货物流单号')
    OPIlogisticsCompnay = Column(String(16), comment=u'快递公司')
    OPIlogisticsText = Column(Text, comment=u'发货物流信息')
    OPIlogisticstime = Column(String(16), comment=u'发货时间')
    # OPIsignperson = Column(String(16), comment=u'签收人')
    #
    # OPIresendLogisticSn = Column(String(64), comment=u'快递公司: 退货单号')
    # OPIresendLogisticText = Column(String(64),  comment=u'退货物流信息')
    # OPIresendLogistictime = Column(String(16), comment=u'退货时间')

    @property
    def PSKproperkey(self):
        return eval(self._PSKproperkey)

    @PSKproperkey.setter
    def PSKproperkey(self, raw):
        self._PSKproperkey = str(raw)

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = self.all
        self.add('PSKproperkey').hide('_PSKproperkey')


class OrderProductResend(BaseModel):
    """退款(换货)"""
    __tablename__ = 'orderproductresend'
    OPRid = Column(String(64), primary_key=True)
    OPRsn = Column(String(64), comment=u'退货编号')
    OPIid = Column(String(64), nullable=False, comment=u'订单商品详情id')

    OPRschedule = Column(Integer, default=0, comment=u"进度,  { 0: '已申请', 1: '等待买家发货', 2: '买家已发货', 3: '卖家发货中', 4: '卖家已发货', 5: '完成', 6: '拒绝申请'}")
    OPRtype = Column(Integer, default=0, comment=u'类型, 0 退货  1 换货')
    OPRmount = Column(Float, comment=u'退款金额')
    OPRreason = Column(String(64), comment=u'退款原因')
    OPRdesc = Column(String(255), comment=u'退款说明')
    OPRimage = Column(Text, comment=u'凭证, [http://www.jpg, http://www.jpb')
    OPRcreatetime = Column(DateTime, default=datetime.now, comment=u'申请时间')

    OPRresendLogisticSn = Column(String(64), comment=u'退货单号')
    OPRresendLogisticCompany = Column(String(16), comment=u'物流公司')
    OPRresendLogisticText = Column(Text, comment=u'退货物流信息')
    OPRresendLogistictime = Column(DateTime, comment=u'退货时间')
    OPRreceivername = Column(String(16), comment=u'收货人信名')
    OPRreceiverphone = Column(String(16), comment=u'收货人手机')
    OPRreceiveraddress = Column(String(255), comment=u'收货地址')


class OrderProductSendTwice(BaseModel):
    """卖家第二次发货"""
    __tablename__ = 'ordersendtwice'
    OPSid = Column(String(64), primary_key=True)
    OPRid = Column(String(64), nullable=False, comment=u'退货换货id')
    OPSsendtime = Column(DateTime, default=datetime.now, comment=u'发货时间')
    OPSsendsn = Column(String(64), nullable=False, comment=u'退货单号')
    OPSsendLogisticCompany = Column(String(16), nullable=False, comment=u'物流公司')
    OPSsendLogisticText = Column(Text, comment=u'物流信息')
    OPSreceivername = Column(String(16), comment=u'姓名')
    OPSreceivephone = Column(String(16), comment=u'手机')
    OPSreceiveaddress = Column(String(255), comment=u'收货地址')


class ProductCategory(BaseModel):
    """
    商品分类
    """
    __tablename__ = 'productcategory'
    PAid = Column(String(64), primary_key=True)
    PAname = Column(String(16))  # 类别名
    PAtype = Column(Integer)  # 类目级别{1 一级分类, 2 二级分类, 3 三级分类}
    Parentid = Column(String(64), default=0)  # 父类别id, 默认0


class ProductFowardInfo(BaseModel):
    """
    转发商品
    """
    __tablename__ = 'productfowardinfo'
    PFIid = Column(String(64), primary_key=True)
    PRid = Column(String(64), nullable=False)  # 商品
    PFItext = Column(String(64))  # 转发显示文字, 为空则使用商品名
    PFIimage = Column(String(255))  # 转发显示图片, 为空则使用商品主图


class TopNav(BaseModel):
    """
    上导航栏
    """
    __tablename__ = 'topnav'
    TNid = Column(String(64), primary_key=True)
    TNname = Column(String(8), nullable=False)  # 导航文字
    Tisdelete = Column(Boolean, default=False)  # 是否删除
    TSort = Column(Integer)  # 顺序标志
    TNurl = Column(String(255))  # 跳转链接, 可能需要
    TNtype = Column(Integer, default=1)  # 导航位置分类: {1: 首页, 2: 发现页}
    TNparentid = Column(String(64), default=0)  # 父导航id, 0表示本身是一级导航

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['TNid', 'TNname', 'TSort', 'TNtype']


class HotMessage(BaseModel):
    """
    热文
    """
    __tablename__ = 'hotmessage'
    HMid = Column(String(64), primary_key=True)
    HMtext = Column(String(64), nullable=False)  # 热文文字
    # PRid = Column(String(64))  # 对应商品
    # BAid = Column(String(64))  # 对应专题
    HMcontent = Column(String(64))  # 对应跳转id
    HMcreatetime = Column(String(14))  # 创建时间
    HMstarttime = Column(String(14))  # 上线时间
    HMendtime = Column(String(14))  # 下线时间
    HMsort = Column(Integer)  # 热文的顺序标志
    HMSkipType = Column(Integer, default=0)  # 跳转类型{0:无跳转类型, 1:专题, 2:商品, 3: 教程推文, 4, 公告推文}
    HMisdelete = Column(Boolean, default=False)  # 删除
    HMdisplaytype = Column(Integer, default=0)  # 热文展示类别{该热文展示给 0:普通买家, 1: 合伙人}

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = [
            'HMid',
            'HMtext',
            'HMcreatetime',
            'HMstarttime',
            'HMendtime',
            'HMsort',
            'HMSkipType',
            'HMcontent',
            'HMdisplaytype'
        ]


class BigActivity(BaseModel):
    """
    轮播图/专场
    """
    __tablename__ = 'bigactivity'
    BAid = Column(String(64), primary_key=True)
    BAtext = Column(String(125), nullable=False)    # 专题名
    BAimage = Column(String(255), nullable=False)   # 专题图片
    BAcreatetime = Column(String(14))               # 创建时间
    BAstarttime = Column(String(14))                # 上线时间
    BAendtime = Column(String(14))                  # 下线时间
    BAurl = Column(String(255))                     # 专题外链（可能不用）
    BAsort = Column(Integer, default=0)             # 顺序标志
    BAposition = Column(Integer, default=0)         # 图片展示位置{0:首页 1:发现页}
    BAisdisplay = Column(Boolean, default=True)     # 是否展示
    BAisdelete = Column(Boolean, default=False)     # 删除
    BAtype = Column(Integer, comment=u'类型: 0 图片,1 非图片')
    BAlongimg = Column(String(255), comment=u'长图')

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['BAid', 'BAtext', 'BAimage', 'BAposition', 'BAisdisplay', 'BAstarttime', 'BAendtime', 'BAsort', 'BAtype', 'BAlongimg']

#
# class RecommendBanner(BaseModel):
#     """每日十荐页上部轮播图"""
#     __tablename__ = 'recommendbanner'
#     RBid = Column(String(64), primary_key=True)
#     RBimage = Column(String(255))  # 图片
#     PRid = Column(String(64))  # 推荐页轮播图对应的商品
#     RBcreatetime = Column(String(14))  # 创建时间
#     RBstarttime = Column(String(14))  # 上线时间
#     RBendtime = Column(String(14))  # 下线时间
#     RBsort = Column(Integer)  # 顺序标志
#
#     @orm.reconstructor
#     @auto_createtime
#     def __init__(self):
#         self.fields = self.all



class Banner(BaseModel):
    """
    首页轮播图/专场题图
    """
    __tablename__ = 'banner'
    BAid = Column(String(64), primary_key=True)
    BAimage = Column(String(255))  # 图片
    # ACid = Column(String(64))  # 轮播图对应的活动
    SAid = Column(String(64))  # 对应的专场
    BAcreatetime = Column(String(14))  # 创建时间
    BAstarttime = Column(String(14))  # 上线时间
    BAendtime = Column(String(14))  # 下线时间
    BAsort = Column(Integer)  # 顺序标志
    BAisdelete = Column(Boolean, default=False)  # 删除

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['BAid', 'BAimage', 'SAid', 'BAstarttime', 'BAendtime', 'BAsort']


# class SpicialActivity(BaseModel):
#     """
#     专题活动页（废弃）
#     """
#     __tablename__ = 'spicialactivity'
#     SAid = Column(String(64), primary_key=True)
#     SAtext = Column(Text)                           # 专题介绍(可能用不到)
#     # SAbanner = Column(String(255) )                # 专题页banner图
#     SAcreatetime = (String(14))                     # 创建时间
#     SAisdelete = Column(Boolean, default=False)     # 删除
#
#     @orm.reconstructor
#     @auto_createtime
#     def __init__(self):
#         self.fields = ['SAid', 'SAtext']


class User(BaseModel):
    """
    普通用户
    """
    __tablename__ = 'user'
    USid = Column(String(64), primary_key=True)
    USname = Column(String(64), nullable=False)  # 用户名
    # USpassword = Column(String(255))           # 密码
    USphone = Column(String(16))                 # 手机号
    USheader = Column(String(255))               # 头像
    USgender = Column(String(64))                # 性别
    USage = Column(Integer)  # 年龄
    USlastlogin = Column(String(64))             # 用户上次登录时间
    # 用户级别: {0 普通用户, 1 普通合伙人, 2 中级合伙人, 3 高级合伙人}
    USlevel = Column(Integer, default=0)
    UPPerd = Column(String(64), default=0)       # 店主 -> 对应专粉
    USshopkeeper = Column(String(64), default=0) # 上级 -> 对应三级合伙人
    openid = Column(String(64))                  # 微信唯一值
    unionid = Column(String(255))                # 绑定公众号会出现
    accesstoken = Column(String(255))            # 微信token
    subscribe = Column(Integer)                  # 是否关注公众号
    USisfreeze = Column(Boolean, default=False)  # 被冻结（不能提现）

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['USid', 'USname', 'USheader', 'USphone']


class UserLoginTime(BaseModel):
    """
    用来记录用户的登录时间
    """
    __tablename__ = 'userlogintime'
    ULTid = Column(String(64), primary_key=True)
    USid = Column(String(64), nullable=False)  # 用户id
    USTcreatetime = Column(String(14))  # 登录时间
    USTip = Column(String(64))  # 登录ip地址


class SuperUser(BaseModel):
    """
    超级管理员, 管理员, (客服)
    """
    __tablename__ = 'superuser'
    SUid = Column(String(64), primary_key=True)
    SUname = Column(String(64), nullable=False)  # 超级用户名
    SUpassword = Column(String(255), nullable=False)  # 密码
    SUheader = Column(String(255))  # 用户头像, 可以设置一个默认值
    SUlevel = Column(Integer, default=0)  # 用户类型{0: 客服, 1: 管理员, 2:超管}　
    SUcreatetime = Column(String(14))  # 创建时间
    SUidfreeze = Column(Boolean, default=False)  # 是否被冻结
    SUisdelete = Column(Boolean, default=False)  # 是否被删除

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['SUid', 'SUname', 'SUheader']


class SearchField(BaseModel):
    """
    输入框
    """
    __tablename__ = 'searchfield'
    SFid = Column(String(64), primary_key=True)
    SFtext = Column(String(64))  # 搜索框文字
    SFcreatetime = Column(String(14))  # 创建时间
    SFstarttime = Column(String(14))  # 上线时间
    SFendtime = Column(String(14))  # 下线时间
    SFsort = Column(Integer)  # 顺序

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['SFid', 'SFtext', 'SFsort']


# class MyCenter(BaseModel):
#     """我的"""
#     __tablename__ = 'mycenter'
#     MYid = Column(String(64), primary_key=True)
#     USid = Column(String(64), nullable=False)
#     MYranking = Column(String(64))  # 我的排名
#     MYrewards = Column(String(64))  # 额外奖励
#
#     @orm.reconstructor
#     def __init__(self):
#         self.fields = ['MYid', 'MYranking', 'MYrewards']



class IndexAdAlert(BaseModel):
    """
    首页弹窗
    """
    __tablename__ = 'indexadalert'
    IAid = Column(String(64), primary_key=True)
    IAimage = Column(String(255))  # 图片
    IAurl = Column(String(255))  # 暂存url(点击弹窗后的效果未知)
    # 弹窗所针对的用户: {0 普通用户, 1 普通合伙人, 2 中级合伙人, 4 高级合伙人, 5 全部}
    IAtype = Column(Integer, default=0)


class PartnerRequired(BaseModel):
    """合伙人需要满足的条件"""
    __tablename__ = 'partnerrequired'
    id = Column(String(64), primary_key=True)
    partnerlevel = Column(Integer)  # 合伙人级别{0: 普通合伙人, 1: 初级合伙人, 2:高级合伙人}
    ordinaryrequired = Column(Integer, default=0)  # 需要满足的普通合伙人人数
    primaryrequired = Column(Integer, default=0)  # 需要的初级合伙人人数
    invitedordinary = Column(Integer, default=0)  # 需要邀请成功开店的人数
    shopgiftrequired = Column(Boolean, default=True)  # 是否需要开店大礼包


class MonthMonthReward(BaseModel):
    """月月奖"""
    __tablename__ = 'monthmonthreward'
    MMRid = Column(String(64), primary_key=True)
    partnerlevel = Column(Integer)  # 合伙人级别{0: 普通合伙人, 1: 初级合伙人, 2:高级合伙人}
    MMRstarttime = Column(String(16), nullable=False)  # 开始时间
    MMRendtime = Column(String(16), nullable=False)  # 结束时间
    MMRaverage = Column(Float)  # 需要人均销售额
    MMRmount = Column(Float)  # 需要的团队销售总额


class Complain(BaseModel):
    """投诉"""
    __tablename__ = 'complain'
    COid = Column(String(64), primary_key=True)
    COcontent = Column(Text)           # 投诉内容
    COtype = Column(String(16))        # 投诉类型 {201："客服态度差", 202："商品质量问题", 203："售后方案不合理", 204："商品包装问题"}
    OIid = Column(String(64))          # 关联订单id
    USid = Column(String(64))          # 发起人id
    COcreatetime = Column(String(14))  # 创建时间
    COtreatstatus = Column(Integer, default=0)    # 投诉处理状态 {0:未被投诉, 1:投诉处理中, 2:投诉已处理}

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['COid', 'COcontent', 'COtype', "OIid", "USid", 'COcreatetime', 'COtreatstatus']


# 任务等级
class TaskLevel(BaseModel):
    __tablename__ = 'tasklevel'
    TLid = Column(String(64), primary_key=True)
    TAlevel = Column(Integer)                 # 设置任务等级
    TArole  = Column(Text)                    # 当前任务等级的规则弹框
    TAcomplateNotifications = Column(Text)    # 当前等级下任务完成的提示图片
    TLisdelete = Column(Boolean, default=False)              # 是否删除当前任务等级
    # TRid = Column(String(64))                 # 当前等级下的奖励

    @orm.reconstructor
    def __init__(self):
        self.fields = ['TAlevel', "TArole", "TAcomplateNotifications", "TLid"]


# 任务
class Task(BaseModel):
    __tablename__ = "task"
    TAid = Column(String(64), primary_key=True)
    TAname = Column(Text)              # 任务标题
    TAtype = Column(Integer)           # 任务类型 {0: "观看视频", 1: "转发商品", 2: "售出商品", 3: "售出大礼包", 4: "",}
    # TAisOpen = Column(Integer)         # 是否开启
    TAhead = Column(Text)              # 任务前部头像图片
    TAcreatetime = Column(String(14))  # 任务创建时间
    TAstartTime = Column(String(14))   # 任务开启时间
    TAendTime = Column(String(14))     # 任务结束时间
    TAduration = Column(String(14))    # 任务持续时间
    TAstatus = Column(Integer)         # 任务状态 {0: "进行中", 1: "已结束", 2: "已暂停", 3: "已过期", 4: "已失效"}
    # TAlevel = Column(Integer)          # 任务等级 {0: "1级", 1: "2级", 2: "3级", 4:"额外"}
    # TArole = Column(Text)              # 规则弹框图片
    TAmessage = Column(Text)           # 备注
    TLid = Column(String(64))          # 当前任务等级
    TAurl = Column(Text)               # 跳转链接 如果是观看视频，则存入对应视频url，如果不是。则为达标数目
    # RAid = Column(String(64))          # 任务奖励id  已废弃
    # TAcomplateNotifications = Column(Text)  # 任务完成提示图片

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['TAname', "TAtype", "TAhead", "TLid", "TAid"]


# 用户任务关联表
class TaskUser(BaseModel):
    __tablename__ = "taskuser"
    TUid = Column(String(64), primary_key=True)
    USid = Column(String(64))          # 用户id
    TAid = Column(String(64))          # 任务id
    TUcreatetime = Column(String(14))  # 领取任务时间
    TUstatus = Column(Integer)         # 任务状态 {0: "进行中", 1: "已结束", 2: "已暂停", 3: "已过期", 4: "已失效"}
    TUendtime = Column(String(14))     # 任务失效时间
    TUnumber = Column(Integer)         # 完成量
    # RAid = Column(String(64))

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['TUid', "TAid", "TUcreatetime",
                       "TUstatus", "TUendtime", "TAid", "TUnumber"]


# 优惠券
class Raward(BaseModel):
    __tablename__ = "raward"
    RAid = Column(String(64), primary_key=True)
    RAtype = Column(Integer)        # {0: "满减", 1: "佣金加成", 2: "无门槛", 3: "邀请粉丝券", 4:"开店大礼包专用"}
    RAfilter = Column(Float)        # 条件
    RAamount = Column(Float)        # 减少金额
    RAratio = Column(Float)         # 上调比例
    SUid = Column(String(64))       # 创建者id
    RAmaxusenum = Column(Integer, default=1)        # 允许叠加使用张数
    RAmaxholdnum = Column(Integer, default=1)       # 同种券最大可拥有数量
    RAcreatetime = Column(String(14))               # 创建时间
    RAendtime = Column(String(14))                  # 失效时间
    RAname = Column(String(64))                     # 优惠券名称
    RAtransfer = Column(Boolean, default=False)     # 是否允许转赠
    RAtransfereffectivetime = Column(Integer)       # 转赠有效时长(单位:小时), 超时则返回
    RAisdelete = Column(Boolean, default=False)     # 删除
    RAreceiveimg = Column(String(255))              # 领取优惠券弹框图
    RAinvalidimg = Column(String(255))               # 优惠券失效弹框图

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ["RAid", "RAtype", "RAfilter", "RAamount", "RAratio", "RAname", "RAmaxusenum", "RAmaxholdnum",
                       "RAcreatetime", "RAendtime", "RAtransfer", "RAtransfereffectivetime", "RAreceiveimg",
                       "RAinvalidimg"]

class RewardToUser(BaseModel):
    """平台页面内发放给用户的优惠券"""
    __tablename__ = 'rewardtouser'
    RTid = Column(String(64), primary_key=True)
    RAid = Column(String(64))               # 优惠券
    RTcount = Column(Integer)               # 发放数量
    RUcreatetime = Column(String(14))       # 发放时间

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['RTid', 'RAid', 'RUcreatetime']

class RewardPacket(BaseModel):
    """优惠券集合"""
    __tablename__ = 'rewardpacket'
    RPTid = Column(String(64), primary_key=True)
    SUid = Column(String(64))                       # 创建者id
    RPTname = Column(String(64))                    # 优惠券集合名
    RPTcreatetime = Column(String(14))              # 创建时间
    RPTisdelete = Column(Boolean, default=False)    # 删除

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['RPTid', 'RPTname']

class RewardPacketContact(BaseModel):
    """优惠券集合关联表"""
    __tablename__ = 'rewardpacketcontact'
    RPCid = Column(String(64), primary_key=True)
    RAid = Column(String(64), nullable=True)    # 优惠券id
    RPTid = Column(String(64), nullable=True)   # 优惠券集合id
    RPCnumber = Column(Integer, default=1)      # 优惠券数量

    @orm.reconstructor
    def __init__(self):
        self.fields = self.all

class RewardTransfer(BaseModel):
    """优惠券转赠表"""
    __tablename__ = 'rewardtransfer'
    RFid = Column(String(64), primary_key=True)
    USid = Column(String(64))               # 接收用户
    RAid = Column(String(64))               # 优惠券
    RFfrom = Column(String(64))             # 赠送人
    RAnumber = Column(Integer)              # 赠送数量
    RFcreatetime = Column(String(14))       # 转赠时间
    RFendtime = Column(String(14))          # 退回时间
    RFusetime = Column(String(14))          # 优惠券使用时间
    RFstatus = Column(Integer, default=0)   # 转赠状态 {0:已领取 1:已退回 2:已使用 }

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['RAid', 'USid', 'RAnumber', 'RFfrom', 'RFcreatetime', 'RFendtime', 'RFstatus']


class RewardGrantRecord(BaseModel):
    """平台赠送优惠券记录"""
    __tablename__ = 'rewardgrantrecord'
    RGRid = Column(String(64), primary_key=True)
    USid = Column(String(64))               # 接收用户
    SUid = Column(String(64))               # 运营id
    RAid = Column(String(64))               # 优惠券id
    RAnumber = Column(Integer)              # 赠送数量
    RGRcreatetime = Column(String(14))      # 创建时间

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['USid', 'SUid', 'RAid', 'RAnumber', 'RGRcreatetime']


# 奖励和任务的关联表
class TaskRaward(BaseModel):
    __tablename__ = "taskreward"
    TRid = Column(String(64), primary_key=True)
    TLid = Column(String(64))   # 任务等级id
    RAid = Column(String(64))  # 奖励id
    RAnumber = Column(Integer)                # 奖励数目

    @orm.reconstructor
    def __init__(self):
        self.fields = ['TRid', "TLid", "RAid", "RAnumber"]


class UserRaward(BaseModel):
    __tablename__ = "userreward"
    URid = Column(String(64), primary_key=True)
    RAid = Column(String(64))  # 奖励id
    USid = Column(String(64))  # 用户id
    RAnumber = Column(Integer, default=1)  # 奖励数目
    URcreatetime = Column(String(14))  # 创建时间
    URFrom = Column(String(64))  # 优惠券来源 如果为空则为平台

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        # self.fields = ['TRid', "TAid", "RAid", "RAnumber"]
        self.fields = ["URid", "USid", "RAid", "RAnumber", "URcreatetime"]


class AdImage(BaseModel):
    """（我的）广告图片"""
    __tablename__ = "adimage"
    AIid = Column(String(64), primary_key=True)
    AIimage = Column(String(255))  # 图片地址
    AItype = Column(Integer)
    """
     图片类型{0: 我的导师， 1:小静态广告图, 2:大静态广告图, 3: 发现弹框图片,
     4: 等级规则图片(未开店), 5: 等级规则(已开店), 6: 专属粉丝管理规则，
     7：开店邀请海报规则， 8：邀请开店海报，9：邀请专属粉丝海报, 10：专属粉丝分享海报, 11: 提现帮助,
     12: 客服, 13: 开店邀请函, 14: 收益详情 }
    """
    AIsize = Column(Integer)  # 图片尺寸{ 1:小图 高度120px, 2:大图 高度400px}
    ACid = Column(String(64))  # 图片对应的活动
    AIcreatetime = Column(String(14))  # 创建时间
    AIstarttime = Column(String(14))  # 上线时间
    AIendtime = Column(String(14))  # 下线时间
    AIisdelete = Column(Boolean, default=False)  # 删除
    AIurl = Column(String(255))  # 外链url （可能会用）


    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['AIid', 'AIimage', 'AItype', 'AIsize', 'ACid', 'AIurl']

class LevelRules(BaseModel):
    """等级规则"""
    __tablename__ = "levelrules"
    LRid = Column(String(64), primary_key=True)
    LRtext = Column(Text)  # 规则内容
    LRtype = Column(Integer)  # 规则类别 {1.未开店(我的), 2.已开店, 3.专属粉丝, 4.开店邀请}
    LRcreatetime = Column(String(14))  # 创建时间
    LRisdelete = Column(Boolean, default=False)  # 删除

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['LRtext', 'LRtype']

class BankCard(BaseModel):
    """银行卡"""
    __tablename__ = "bankcard"
    BCid = Column(String(64), primary_key=True)
    USid = Column(String(64), nullable=False)           # 用户id
    BCusername = Column(String(64), nullable=False)     # 姓名
    BCnumber = Column(String(19), nullable=False)       # 银行卡号
    BCtype = Column(Integer, default=1)                 # 银行卡类别{1:储蓄卡, 2:信用卡}
    BCbankname = Column(String(64), nullable=False)     # 银行名称
    BCaddress = Column(String(125), nullable=False)     # 开户行地址
    BCisdelete = Column(Boolean, default=False)         # 删除
    BCcreatetime = Column(String(14))                   # 创建时间

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['BCid', 'BCusername', 'BCnumber', 'BCbankname', 'BCaddress']

class UserAddress(BaseModel):
    """用户收货地址"""
    __tablename__ = 'useraddress'
    UAid = Column(String(64), primary_key=True)
    USid = Column(String(64), nullable=False)           # 用户
    UAname = Column(String(16), nullable=False)         # 收货人姓名
    UAphone = Column(String(16), nullable=False)        # 收货人电话
    UAtext = Column(String(255), nullable=False)        # 具体地址
    UAdefault = Column(Boolean, default=False)          # 默认收获地址
    UAisdelete = Column(Boolean, default=False)         # 删除
    UAcreatetime = Column(String(14))                   # 创建时间
    areaid = Column(String(8), nullable=False)         # 关联的区域id

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['UAid', 'UAname', 'UAphone', 'UAtext', 'UAdefault', 'areaid']


class Province(BaseModel):
    """省"""
    __tablename__ = 'province'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    provinceid = Column(String(8), nullable=False)

    @orm.reconstructor
    def __init__(self):
        self.fields = ['name', 'provinceid']

class City(BaseModel):
    """市"""
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    cityid = Column(String(8), nullable=False)
    name = Column(String(20), nullable=False)
    provinceid = Column(String(8), nullable=False)

    @orm.reconstructor
    def __init__(self):
        self.fields = ['cityid', 'name', 'provinceid']

class Area(BaseModel):
    """区县"""
    __tablename__ = 'area'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    areaid = Column(String(8), nullable=False)
    cityid = Column(String(8), nullable=False)

    @orm.reconstructor
    def __init__(self):
        self.fields = ['name', 'areaid', 'cityid']


class IdentifyingCode(BaseModel):
    """验证码"""
    __tablename__ = "identifyingcode"
    ICid = Column(String(64), primary_key=True)
    ICtelphone = Column(String(14), nullable=False)  # 获取验证码的手机号
    ICcode = Column(String(8), nullable=False)    # 获取到的验证码
    ICtime = Column(String(14), nullable=False)    # 获取的时间，格式为20180503100322

    @orm.reconstructor
    def __init__(self):
        self.fields = self.all


class PartnerSellOrinviteMount(BaseModel):
    """合伙人活动时间内的销售额"""
    __tablename__ = 'PartnerSellOrinviteMount'
    PSOMid = Column(String(64), primary_key=True)
    USid = Column(String(64), comment=u'用户')
    sellorinvitemount = Column(Float, comment=u'销售额')
    PSIMid = Column(String(64), comment=u'销售额.活动id')


class PartnerSellOrInviteMatch(BaseModel):
    """合伙人销售额或者邀请开店活动"""
    __tablename__ = 'PartnerSellOrInviteMatch'
    PSIMid = Column(String(64), primary_key=True)
    PSIMname = Column(String(16), comment=u'奖励名称')
    PSIMlevel = Column(Integer, default=1, comment=u'针对合伙人级别')
    PSIMstarttime = Column(String(16), nullable=False, comment=u'活动起始时间')
    PSIMendtime = Column(String(16), nullable=False, comment=u'活动结束时间')
    PSIMrule = Column(Text, comment=u'奖励各个级别规则,格式{1: 122, 2: 5000, 3: 10000}')  # 奖励条件
    PSIfavor = Column(Text, comment=u'额外奖励{1: 0.9, 2: 0.5, 3:0.66}')  # 额外奖励存比例，为实际销售额的比例
    PSIMfavortime = Column(String(16), comment=u'奖励发放时间')
    PSIMtype = Column(String(8), default=u'sell', comment=u'活动类型: sell, extra')  # 活动分类:周周奖/额外活动
    PSIMisclose = Column(Boolean, default=False, comment=u'是否关闭')
    PSIMisdelete = Column(Boolean, default=False, comment=u'是否删除')

    @orm.reconstructor
    def __init__(self):
        self.fields = self.all


class UserCommision(BaseModel):
    """佣金"""
    __tablename__ = 'commision'
    UCid = Column(String(64), primary_key=True)
    USid = Column(String(64), nullable=False, comment=u'用户')
    UCnum = Column(Float, default=0, comment=u'余额')
    UCtotal = Column(DECIMAL(precision=28, scale=4), default=0, comment=u'总获得, 只做加法运算')


class UserCommisionPriview(BaseModel):
    """用户预估佣金流水表, 粉丝购买商品获得"""
    __tablename__ = 'usercommsionprivew'
    UCPid = Column(String(64), primary_key=True)
    OPIid = Column(String(64), comment=u'订单商品详情')  # 记录预估值的来源订单详情, 收货时方便获取
    USid = Column(String(64), nullable=False, comment=u'用户')
    UCPtime = Column(DateTime, default=datetime.now, comment=u'时间')
    UCPnums = Column(Float, default=0, comment=u'佣金金额')
    UCtype = Column(Float, default=0, comment=u'佣金类型： 0: 开店佣金收益， 1: 专粉收益')
    UCPstatus = Column(Integer, default=0, comment=u'状态: 0: 预估佣金, 10: 已到帐, 20: 不可用')


class UserCommisionFlow(BaseModel):
    """用户资金到帐流水表"""
    __tablename__ = 'usercommisionflow'
    UCfid = Column(String(64), primary_key=True)
    USid = Column(String(64), comment=u'用户')
    UCFnums = Column(Float, comment=u'金额')
    UCFtype = Column(Integer, default=0, comment=u'佣金来源: 0: 销售获得, 10 邀请开店, 20: 专粉支出, 30 团队佣金 40 周周奖 41 额外奖励 45 新店主任务奖励（做完任务后的佣金加成） ')
    UCFtime = Column(DateTime, default=datetime.now, comment=u'时间')


class CommisionToCash(BaseModel):
    """用户佣金提现"""
    __tablename__ = 'commiontocash'
    CTCid = Column(String(64), primary_key=True)
    USid = Column(String(64), nullable=False, comment=u'用户')
    CTCtime = Column(DateTime, default=datetime.now, comment=u'申请时间')
    CTCamount = Column(Integer, nullable=False, comment=u'金额')
    CTCtowxacount = Column(Boolean, default=False, comment=u'是否提款到微信,如为false提款到银行卡')
    CTCname = Column(String(16), nullable=False, comment=u'姓名')
    CTCbankname = Column(String(64), nullable=False, comment=u'银行')
    CTCbankaddress = Column(String(125), comment=u'开户行')
    CTCstatus = Column(Integer, default=0, comment=u'申请提现审核状态 {0: 审核中, 1:允许, 2:拒绝}')
    CTCrefusereason = Column(String(125), comment=u'拒绝理由')


class TeamCommision(BaseModel):
    """团队佣金"""
    __tablename__ = 'teamcommision'
    TCid = Column(String(64), primary_key=True)
    USid = Column(String(64), nullable=False)
    TCtotal = Column(DECIMAL(precision=28, scale=4), default=0, comment=u'团队总额')
    TCtime = Column(DateTime, default=datetime.now, comment=u'时间')


# class PersonalInfo(BaseModel)
#     """账号设置个人信息"""
#     __tablename__ = "personalinfo"
#     PIid = Column(String(64), primary_key=True)
#     USid = Column(String(64), nullable=False)           # 用户id
#     UAid = Column(String(64), nullable=False)           # 用户地址id
#     BCid = Column(String(64), nullable=False)           # 银行卡id


# 交易相关


"""
class ProductSelector(Base):
    # 商品的选项名
    __tablename__ = 'productselect'
    PSid = Column(String(64), primary_key=True)
    PRid = Column(String(64), nullable=False)  # 所属于的商品
    PSname = Column(String(16))  # 可供选择的类别, 比如'颜色', '尺码'


class ProductSelectorInfo(Base):
    # 具体选项
    __tablename__ = 'productselectorinfo'
    PSIid = Column(String(64), primary_key=True)
    PSid = Column(String(64), nullable=False)  # 所属于的选项
    PSItext = Column(String(64), nullable=False)  # 可供选择的选项的文本信息, 比如'xxl', 'M', '红色'
    PSIStock = Column(Integer)  # 该选项(尺码, 或者颜色)的库存
"""

from base_model import Base
Base.metadata.create_all(mysql_engine)
