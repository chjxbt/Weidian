<template>
  <div>
    <el-dialog :title="this.activity.actitle" :visible.sync="commentsDialog" width="8rem">
      <div class="comment-table">
        <el-table :data="commentList" border v-loading="commentLoading">
          <el-table-column property="usname" label="评论人" width="150"></el-table-column>
          <el-table-column property="acocreatetime" label="评论时间" width="170"></el-table-column>
          <el-table-column property="actext" label="评论内容"></el-table-column>
          <el-table-column property="robot" label="用户身份" width="100"></el-table-column>
          <el-table-column fixed="right" label="管理" width="150">
            <template slot-scope="scope">
              <el-button type="text" size="small" @click="replyComment(scope)">回复</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small" @click="">删除</el-button>
            </template>
          </el-table-column>
        </el-table>

        <el-dialog :title="this.activity.actitle" append-to-body :visible.sync="replyComments" width="6rem">
          <div class="comment-box">
            <div class="comment-row">
              <div class="title-text">评论人：</div>
              <div class="content-text">{{comment.usname}}</div>
            </div>
            <div class="comment-row">
              <div class="title-text">评论内容：</div>
              <div class="content-text">{{comment.actext}}{{comment.actext}}{{comment.actext}}{{comment.actext}}{{comment.actext}}{{comment.actext}}</div>
            </div>
            <div class="comment-row">
              <div class="title-text">评论时间：</div>
              <div class="content-text">{{comment.acocreatetime}}</div>
            </div>
            <div class="comment-row">
              <div class="title-text">用户身份：</div>
              <div class="content-text">{{comment.robot}}</div>
            </div>
            <div class="comment-row">
              <div class="title-text">回 复：</div>
              <div class="content-text">
                <el-input type="textarea" :autosize="{ minRows: 3, maxRows: 6 }" placeholder="请输入回复" v-model="replyText" style="width: 4rem"></el-input>
              </div>
            </div>
          </div>
          <div slot="footer" class="dialog-footer">
            <el-button class="at-img-dialog-btn" @click="replyComments = false">取 消</el-button>
            <el-button class="at-img-dialog-btn btn-color" type="primary" @click="addComment">确 定</el-button>
          </div>
        </el-dialog>
        <Pagination class="page-box" :total="total_page" @pageChange="pageChange"></Pagination>
      </div>
    </el-dialog>
  </div>
</template>

<script>
  import Pagination from "../../components/common/page";
  import axios from 'axios';
  import api from '../../api/api';

  export default {
    name: "comments",
    data() {
      return {
        activity: {},           // 查看评论的那条推文
        commentsDialog: false,  // 展示评论
        replyComments: false,   // 回复评论
        replyText: "",          // 回复的内容
        comment: {},            // 回复的那条评论
        commentList: [],        // 评论list
        commentLoading: false,  // 评论表格加载中
        page_size: 5,           // 每页显示的数量
        total_page: 1,          // 总页数
        page_num: 1             // 第几页
      }
    },
    props: {
      // activity: { type: Object, default: {} },    // 点击的推文
    },
    components:{ Pagination },
    methods: {
      // 获取推文下的评论-嵌套回复
      getComments(activity) {
        if(activity) {
          this.activity = activity;
        }
        this.commentsDialog = true;
        this.commentLoading = true;
        axios.get(api.get_comment_with_apply + "?token=" + localStorage.getItem("token") + "&acid=" + this.activity.acid + "&count=" + this.page_size + "&page=" + this.page_num).then(res => {
          if(res.data.status == 200) {
            this.commentList = res.data.data;
            this.total_page = Math.ceil(res.data.count/this.page_size);

            for(let i = 0; i < this.commentList.length; i ++) {
              if(this.commentList[i].user.robot == "0") {
                this.commentList[i].robot = "真实用户";
              }else if(this.commentList[i].user.robot == "1") {
                this.commentList[i].robot = "小马甲用户";
              }
              this.commentList[i].usname = this.commentList[i].user.usname;
            }

            this.commentLoading = false;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 打开回复评论的dialog
      replyComment(scope) {
        this.comment = scope.row;
        this.replyComments = true;
      },

      // 回复评论
      addComment() {
        let params = {
          acoid: this.comment.acoid,
          ACtext: this.replyText
        };
        axios.post(api.add_comment + '?token=' + localStorage.getItem('token'), params).then(res=>{
          if(res.data.status == 200){
            this.$message({ message: res.data.message, type: 'success', duration: 1500 });
            this.replyComments = false;
          }else{
            this.$message({ type: 'error', message: res.data.message, duration: 1500 });
          }
        });
      },

      // 分页点击方法
      pageChange(v) {
        this.page_num = v;
        this.getComments();
      }
    },
    mounted() {

    },
    created() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";

  .comment-table {
    margin: -0.1rem 0.2rem 0 0.2rem;
  }
  .page-box {
    margin-top: 0.1rem;
    text-align: right;
  }
  .comment-box {
    margin: -0.3rem -0.2rem;
    padding: 0.2rem 0.5rem;
    .comment-row {
      display: flex;
      padding: 0.03rem 0;
      &:last-child {
        margin-top: 0.1rem;
      }
      .title-text {
        width: 0.6rem;
        white-space: nowrap;
      }
      .content-text {
        width: 4.5rem;
        margin-left: 0.1rem;
      }
    }
  }
  .dialog-footer {
    .at-img-dialog-btn {
      padding: 0.05rem 0.1rem;
      font-size: 14px;
    }
    .btn-color {
      border-color: @btnActiveColor;
      background-color: @btnActiveColor;
    }
  }
</style>
