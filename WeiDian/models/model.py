# *- coding:utf8 *-
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine, Integer, String, Text, Float, Boolean, orm
from WeiDian.config import dbconfig as cfg
from WeiDian.models.base_model import BaseModel, auto_createtime

DB_PARAMS = "{0}://{1}:{2}@{3}/{4}?charset={5}".format(
    cfg.sqlenginename,
    cfg.username,
    cfg.password,
    cfg.host,
    cfg.database,
    cfg.charset)
mysql_engine = create_engine(DB_PARAMS, echo=False)
Base = declarative_base()


class Activity(Base, BaseModel):
    """
    活动
    """
    __tablename__ = 'activity'
    ACid = Column(String(64), primary_key=True)
    PRid = Column(String(64), nullable=False)  # 活动商品
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

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = [
            'ACid',
            'PRid',
            'ACtype',
            'ACtext',
            'ACbrowsenum',
            'ACcreatetime',
            'ACstarttime',
            'ACendtime',
            'ACistop',
            'ACisended',
            'TopnavId']


class ActivityComment(Base, BaseModel):
    """
    活动评论, 以及评论回复
    """
    __tablename__ = 'activitycomment'
    ACOid = Column(String(64), primary_key=True)
    ACid = Column(String(64), nullable=False)  # 评论对应的活动)
    ACOparentid = Column(String(64))  # 所回复的评论(可以为空, 为空代表是评论)
    USid = Column(String(64), nullable=False)  # 发布评论的用户
    ACtext = Column(String(255), nullable=False)  # 评论内容
    ACOcreatetime = Column(String(64))  # 时间
    ACisdelete = Column(Boolean, default=False)  # 是否删除

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['USid', 'ACOcreatetime', 'ACtext']


class ActivityLike(Base, BaseModel):
    """
    点赞
    """
    __tablename__ = 'like'
    ALid = Column(String(64), primary_key=True)
    ACid = Column(String(64), nullable=False)  # 活动
    USid = Column(String(64), nullable=False)  # 用户
    ALcreatetime = Column(String(64))  # 时间

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['ACid', 'USid', 'ALcreatetime']


class ActivityMedia(Base, BaseModel):
    """
    活动图片/视频
    """
    __tablename__ = 'activatymedia'
    AMid = Column(String(64), primary_key=True)
    ACid = Column(String(64), nullable=False)  # 商品图片对应的活动
    AMimage = Column(String(64))  # 图片对应的路径
    AMvideo = Column(String(64))  # 视频地址
    AMsort = Column(Integer)  # 图片的顺序, 用于表明图片的位置

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['AMid']


class ActivityTag(Base, BaseModel):
    """
    活动右上角标
    """
    __tablename__ = 'activitytag'
    ATid = Column(String(64), primary_key=True)
    ACid = Column(String(64), nullable=False)  # 活动
    ATname = Column(String(8), nullable=False)  # 角标文字
    ATstate = Column(Integer, default=1)  # 显示状态: {1 显示, 0 隐藏}

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['ATid', 'ATname', ]


class ActivityFoward(Base):
    """
    活动转发
    """
    __tablename__ = 'activityfoward'
    AFid = Column(String(64), primary_key=True)
    USid = Column(String(64))  # 用户
    ACid = Column(String(64))  # 活动


class Product(Base, BaseModel):
    """
    商品
    """
    __tablename__ = 'product'
    PRid = Column(String(64), primary_key=True)
    PRdetail = Column(LONGTEXT)  # 商品详情, 大文本
    PRmainpic = Column(String(64), nullable=False)  # 商品主图
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
    PRcreatetime = Column(String(64))  # 创建时间
    SUmodifyid = Column(String(64))  # 修改人id
    PRmodifytime = Column(String(64))  # 修改时间
    PRstatuss = Column(Integer, default=1)  # 商品状态: {0 删除, 1 正常, 2 禁用}
    PRprice = Column(Float, nullable=False)  # 显示价格
    PRisdelete = Column(Boolean, default=False)
    # 以下
    PRviewnum = Column(Integer, default=0)  # 浏览量
    PRfakeviewnum = Column(Integer)  # 虚拟浏览数
    PRfakelikenum = Column(Integer, default=0)  # 虚拟收藏数量
    PRsalefakenum = Column(Integer)  # 商品自定义销量
    PAid = Column(String(64))  # 类目id
    PRlogisticsfee = Column(Float)  # 物流费
    PRstock = Column(Integer)  # 商品详情页库存

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
            'PRstock']


class ProductSkuKey(Base, BaseModel):
    """sku属性名"""
    __tablename__ = 'productskukey'
    PSKid = Column(String(64), primary_key=True)
    PRid = Column(String(64), nullable=False)  # 商品id
    PSVid = Column(String(64), nullable=False)  # 商品sku属性的value
    PSKproperkey = Column(Text, nullable=False)  # 商品sku属性的key, json
    PSKproductnum = Column(Integer, nullable=False)  # 库存
    PSKalias = Column(String(64), nullable=False)  # 商品别名
    PSKprice = Column(Float, default=0.00)  # 价格
    PSKpostfee = Column(Float, nullable=False)  # 物流费
    PSKactiviyid = Column(String(64))  # 活动id, 不知用处

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = self.all


class ProductSkuValue(Base, BaseModel):
    """sku属性值, 每一个商品对应一个此表"""
    __tablename__ = 'productskuvalue'
    PSVid = Column(String(64), primary_key=True)
    PRid = Column(String(64), nullable=False)  # 关联商品
    PSVpropervalue = Column(Text, nullable=False)  # 商品sku的属性, json

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = self.all


class ProductImage(Base, BaseModel):
    """商品展示图片"""
    __tablename__ = 'productimage'
    PIid = Column(String(64), primary_key=True)
    PRid = Column(String(64), nullable=False)  # 商品id
    PIurl = Column(String(50), nullable=False)  # 图片链接(七牛云)
    PIsort = Column(Integer)  # 图片顺序

    @orm.reconstructor
    def __init__(self):
        self.fields = self.all


class ProductLike(Base, BaseModel):
    """商品收藏(喜欢)"""
    __tablename__ = 'productlike'
    PLid = Column(String(64), primary_key=True)
    USid = Column(String(64), nullable=False)  # 用户
    PRid = Column(String(64), nullable=False)  # 商品
    PLcreatetime = Column(String(64))  # 创建时间

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        pass


class RecommendBanner(Base, BaseModel):
    """每日十荐页上部轮播图"""
    __tablename__ = 'recommendbanner'
    RBid = Column(String(64), primary_key=True)
    RBimage = Column(String(64))  # 图片
    PRid = Column(String(64))  # 推荐页轮播图对应的商品
    RBcreatetime = Column(String(14))  # 创建时间
    RBstarttime = Column(String(14))  # 上线时间
    RBendtime = Column(String(14))  # 下线时间
    RBsort = Column(Integer)  # 顺序标志

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = self.all


class Recommend(Base, BaseModel):
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


class RecommendProduct(Base, BaseModel):
    """每日十荐页商品滚动区域的中转表"""
    __tablename__ = 'recommendproduct'
    RPid = Column(String(64), primary_key=True)
    REid = Column(String(64))  # 关联的推荐商品区域
    PRid = Column(String(64))  # 关联的商品


class RecommendLike(Base, BaseModel):
    """每日十荐页点赞笑脸"""
    __tablename__ = 'recommendlike'
    RLid = Column(String(64), primary_key=True)
    USid = Column(String(64))  # 用户id
    REid = Column(String(64))  # 推荐商品id
    RLtime = Column(String(14))  # 推荐页点赞时间


class ShoppingCart(Base, BaseModel):
    """购物车"""
    __tablename__ = 'shopingcart'
    SCid = Column(String(64), primary_key=True)
    USid = Column(String(64))  # 用户id
    PSKid = Column(String(64))  # 商品的选项id
    PRid = Column(String(64))  # 商品id
    SCnums = Column(Integer)  # 数量

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['SCid', 'PRid', 'SCnums']


class OrderInfo(Base):
    """订单信息"""
    __tablename__ = 'orderinfo'
    OIid = Column(String(64), primary_key=True)
    OIsn = Column(String(64))  # 订单号
    USid = Column(String(64))  # 用户
    OItradenum = Column(String(125))  # 交易号, (如果有)
    # 订单状态: {0: 待支付, 1: 支付成功, 2: 超时关闭, 3: 支付关闭}
    OIpaystatus = Column(Integer, default=0)
    OIpaytype = Column(Integer)  # 支付类型: {0: 银行卡支付, 1: 微信支付}
    OIleavetext = Column(String(255))  # 订单留言
    OImount = Column(Float)  # 金额
    OIpaytime = Column(String(64))  # 支付时间
    OIaddress = Column(String(255), nullable=False)  # 地址
    OIsigername = Column(String(64))  # 收货人
    OIcreatetime = Column(String(64))  # 订单创建时间


class OrderProductInfo(Base):
    """订单商品详情, 多个订单商品详情对应一个订单"""
    __tablename__ = 'orderproductinfo'
    OPIid = Column(String(64), primary_key=True)
    OIid = Column(String(64), nullable=False)  # 订单
    PRid = Column(String(64), nullable=False)  # 商品
    OIproductprice = Column(Float, nullable=False)   # 商品价格(购买时候的价格)
    OPIproductname = Column(String(64))  # 商品的名字(购买之时的)
    OPIproductimages = Column(String(64))  # 商品主图
    OPIproductnum = Column(Integer, default=1)  # 购买数量


class ProductCategory(Base):
    """
    商品分类
    """
    __tablename__ = 'productcategory'
    PAid = Column(String(64), primary_key=True)
    PAname = Column(String(16))  # 类别名
    PAtype = Column(Integer)  # 类目级别{1 一级分类, 2 二级分类, 3 三级分类}
    Parentid = Column(String(64), default=0)  # 父类别id, 默认0


class ProductFowardInfo(Base):
    """
    转发商品
    """
    __tablename__ = 'productfowardinfo'
    PFIid = Column(String(64), primary_key=True)
    PRid = Column(String(64), nullable=False)  # 商品
    PFItext = Column(String(64))  # 转发显示文字, 为空则使用商品名
    PFIimage = Column(String(255))  # 转发显示图片, 为空则使用商品主图


class TopNav(Base, BaseModel):
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


class HotMessage(Base, BaseModel):
    """
    热文
    """
    __tablename__ = 'hotmessage'
    HMid = Column(String(64), primary_key=True)
    HMtext = Column(String(64), nullable=False)  # 热文文字
    PRid = Column(String(64), nullable=False)  # 对应商品
    HMcreatetime = Column(String(64))  # 创建时间
    HMstarttime = Column(String(64))  # 上线时间
    HMendtime = Column(String(64))  # 下线时间
    HMsort = Column(Integer)  # 热文的顺序标志

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = [
            'HMid',
            'HMtext',
            'PRid',
            'HMcreatetime',
            'HMstarttime',
            'HMendtime',
            'HMsort'
        ]


class Banner(Base, BaseModel):
    """
    轮播图
    """
    __tablename__ = 'banner'
    BAid = Column(String(64), primary_key=True)
    BAimage = Column(String(64))  # 图片
    ACid = Column(String(64))  # 轮播图对应的活动
    BAcreatetime = Column(String(64))  # 创建时间
    BAstarttime = Column(String(64))  # 上线时间
    BAendtime = Column(String(64))  # 下线时间
    BAsort = Column(Integer)  # 顺序标志

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = self.all


# 可能用不到
class SpicialActivity(Base):
    """
    轮播对应的专场活动
    """
    __tablename__ = 'spicialactivity'
    SAid = Column(String(64), primary_key=True)
    ACid = Column(String(64), nullable=False)  # 对应活动的id
    BAid = Column(String(64), nullable=False)  # 对应的轮播图
    SAtext = Column(Text)  # 活动专场介绍


class User(Base):
    """
    普通用户
    """
    __tablename__ = 'user'
    USid = Column(String(64), primary_key=True)
    USname = Column(String(64), nullable=False)  # 用户名
    USphone = Column(String(16))  # 手机号
    UShader = Column(String(255))  # 头像
    USgender = Column(String(64))  # 性别
    USage = Column(Integer)  # 年龄
    USlastlogin = Column(String(64))  # 用户上次登录时间
    # 用户级别: {0 普通用户, 1 普通合伙人, 2 中级合伙人, 3 高级合伙人}
    USlevel = Column(Integer, default=0)


class UserLoginTime(Base, BaseModel):
    """
    用来记录用户的登录时间
    """
    __tablename__ = 'userlogintime'
    ULTid = Column(String(64), primary_key=True)
    Usid = Column(String(64), nullable=False)  # 用户id
    USTcreatetime = Column(String(64))  # 登录时间
    USTip = Column(String(64))  # 登录ip地址


class SuperUser(Base, BaseModel):
    """
    超级管理员, 管理员, (客服)
    """
    __tablename__ = 'superuser'
    SUid = Column(String(64), primary_key=True)
    SUname = Column(String(64), nullable=False)  # 超级用户名
    SUpassword = Column(String(255), nullable=False)  # 密码
    SUheader = Column(String(64))  # 用户头像, 可以设置一个默认值
    SUlevel = Column(Integer, default=0)  # 用户类型{0: 客服, 1: 管理员, 2:超管}　
    SUcreatetime = Column(String(64))  # 创建时间
    SUidfreeze = Column(Boolean, default=False)  # 是否被冻结
    SUisdelete = Column(Boolean, default=False)  # 是否被删除

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['SUid', 'SUname', 'SUheader']


class UserAddress(Base):
    __tablename__ = 'useraddress'
    UAid = Column(String(64), primary_key=True)
    USid = Column(String(64), nullable=False)  # 用户
    UAtext = Column(String(255), nullable=False)  # 具体地址
    UAphone = Column(String(16), nullable=False)  # 电话
    UAname = Column(String(16), nullable=False)  # 收货人姓名


class SearchField(Base, BaseModel):
    """
    输入框
    """
    __tablename__ = 'searchfield'
    SFid = Column(String(64), primary_key=True)
    SFtext = Column(String(64))  # 搜索框文字
    SFcreatetime = Column(String(64))  # 创建时间
    SFstarttime = Column(String(64))  # 上线时间
    SFendtime = Column(String(64))  # 下线时间
    SFsort = Column(Integer)  # 顺序
    ACisended = Column(Boolean, default=False)  # 是否被手动截止

    @orm.reconstructor
    @auto_createtime
    def __init__(self):
        self.fields = ['SFid', 'SFtext', 'SFsort']


class IndexAdAlert(Base):
    """
    首页弹窗
    """
    __tablename__ = 'indexadalert'
    IAid = Column(String(64), primary_key=True)
    IAimage = Column(String(64))  # 图片
    IAurl = Column(String(128))  # 暂存url(点击弹窗后的效果未知)
    # 弹窗所针对的用户: {0 普通用户, 1 普通合伙人, 2 中级合伙人, 4 高级合伙人, 5 全部}
    IAtype = Column(Integer, default=0)


# 交易相关
"""
class ShoppingCart(Base):
    购物车
    pass


class OrderInfo(Base):
    订单信息
    pass


class OrderInfo(Base):
    订单内的商品详情

    pass

"""


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
