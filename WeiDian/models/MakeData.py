# *- coding:utf8 *-
# 兼容linux系统
import random
import sys
import os
from datetime import datetime

from sqlalchemy.orm import scoped_session, sessionmaker

import model
import pymysql

sys.path.append(os.path.dirname(os.getcwd()))  # 增加系统路径
from WeiDian.service.SActivity import SActivity

change_index = 10  # 循环中改变type的点
info_count = 22  # 需要插入的数据库条数


class MakeData():
    def __init__(self):
        self.act = SActivity()
        self.session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=model.mysql_engine))

    # def make_id(self):
    #     import uuid
    #     user_ids = []
    #     i = 0
    #     while i < info_count:
    #         user_ids.append(str(uuid.uuid4()))
    #         i = i + 1
    #     return user_ids

    def add_activity(self):
        for i in range(2000, 2501):
            activity_model = model.Activity()
            activity_model.ACid = str(i)
            activity_model.ACtype = "2"
            activity_model.ACtext = "活动活动活动"
            activity_model.ACbrowsenum = "20"
            activity_model.AClikeFakeNum = str(random.randint(0, 500))
            activity_model.ACstarttime = str(random.randint(2017, 2019))+'0510000000'
            activity_model.ACendtime = str( random.randint(2017, 2019))+'0510000000'
            activity_model.PRid = 'this is prid'
            activity_model.USid = 'this is usid'
            activity_model.TopnavId = 'q'
            self.session.add(activity_model)
            self.session.commit()

    def add_media(self):
        for i in range(1500, 2500):
            media = model.ActivityMedia()
            media.AMid = str(i)
            media.ACid = str(random.randint(2000, 2500))
            # tem = random.randint(1, 2)

            media.AMimage = 'http://www.thisimage'
            media.AMsort = random.randint(1, 9)
            self.session.add(media)
            self.session.commit()

    def add_comment(self):
        from model import ActivityComment
        for i in range(1500, 2000):
            comment = ActivityComment()
            comment.ACOid = str(i)
            tem = random.randint(1, 2)
            if tem == 1:
                comment.ACid = str(random.randint(1500, 2500))
                comment.ACtext = '这是评论' + str(i)
            else:
                comment.ACOparentid = str(random.randint(1500, 2500))
                comment.ACtext = '这是回复' + str(i)
            comment.USid = 'this is usid'
            self.session.add(comment)
            self.session.commit()

    def add_tags(self):
        from model import ActivityTag
        for i in range(1500, 2000):
            tag = ActivityTag()
            tag.ATid = str(i)
            tag.ACid = str(random.randint(1500, 2500))
            tag.ATname = random.choice(['活动', '爆款', '其他'])
            self.session.add(tag)
            self.session.commit()

    def add_hotmessage(self):
        from model import HotMessage
        for i in range(1500, 2000):
            hm = HotMessage()
            hm.HMid = str(i)
            hm.PRid = 'this is prid'
            hm.HMstarttime = str(random.randint(2017, 2019))+'0510000000'
            hm.HMendtime = str( random.randint(2017, 2019))+'0510000000'




    # def update_activity(self, ):



    #
    # def add_shops(self, tshop_ids):
    #     for i in range(info_count):
    #         shop_model = model.Shops()
    #         shop_model.Sid = tshop_ids[i]
    #         shop_model.Sname = "test{0}".format(i)
    #         shop_model.Sreview = "5"
    #         shop_model.Sdetail = "包子，粥，面条"
    #         shop_model.Simage = "http://www.baidu.com"
    #         shop_model.Stel = "135880461%02d" % i
    #         self.shop.add_shop(shop_model)
    #
    # def add_conpons(self, conid):
    #     for i in range(info_count):
    #         self.cou.add_coupons(**{
    #             "COid": i,
    #             "COfilter": float("1%02d.00" % i),
    #             "COdiscount": 0.2,
    #             "COamount": 10.1,
    #             "COstart": "2018011421%02d00" % i,
    #             "COend": "2018041421%02d00" % i
    #         })


class databse_deal():
    def __init__(self):
        self.conn = pymysql.connect(
            host=model.cfg.host, user=model.cfg.username,
            passwd=model.cfg.password, charset=model.cfg.charset)
        self.cursor = self.conn.cursor()

    def create_database(self):
        sql = "create database if not exists {0} DEFAULT CHARACTER SET utf8 COLLATE utf8_gyeneral_ci ;".format(
            model.cfg.database)
        print sql
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
        finally:
            self.conn_close()

    def drop_database(self):
        sql = "drop database if exists {0} ;".format(
            model.cfg.database)
        print sql
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)

        finally:
            self.conn_close()

    def conn_close(self):
        self.conn.close()


def create():
    databse_deal().create_database()
    model.Base.metadata.create_all(model.mysql_engine)


def drop():
    databse_deal().drop_database()


if __name__ == "__main__":
    print("start")
    '''
       运行该文件就可以在对应的数据库里生成本文件声明的所有table
       如果需要清除数据库，输入drop
       如果需要创建数据库 输入任意不包含drop的字符
       '''
    action = raw_input("create database?")
    if "drop" in action:
        drop()

    else:
        # create()
        data = MakeData()
        # tshop_ids = data.make_id()
        # data.add_shops(tshop_ids)
        # data.add_products(tshop_ids)
        # data.add_conpons(tshop_ids)
        # print("over")
        # data.add_activity()
        # data.add_media()
        # data.add_comment()
        data.add_tags()
