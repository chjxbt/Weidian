<template>
  <div>
    <el-dialog :title="this.activity.actitle" :visible.sync="commentsDialog" width="8rem">
      <div class="comment-table">
        <el-table :data="commentList" border v-loading="commentLoading">
          <el-table-column property="usname" label="评论人" width="150"></el-table-column>
          <el-table-column property="acocreatetime" label="评论时间" width="170"></el-table-column>
          <el-table-column property="actext" label="评论内容"></el-table-column>
          <el-table-column property="robot" label="用户身份" width="100"></el-table-column>
          <el-table-column property="replyStatus" label="回复状态" width="100"></el-table-column>
          <el-table-column fixed="right" label="管理" width="150">
            <template slot-scope="scope">
              <el-button type="text" size="small" @click="replyComment(scope)" :disabled="scope.row.robot == '小马甲用户'">回复</el-button>
              <el-button type="text" size="small">|</el-button>
              <el-button type="text" size="small" @click="deleteComment(scope.row, scope.$index, 'comment')">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
        <Pagination class="page-box" :total="total_page" @pageChange="pageChange"></Pagination>

        <el-dialog :title="this.activity.actitle" append-to-body :visible.sync="replyComments" width="6rem">
          <div class="comment-box">
            <div class="comment-row">
              <div class="title-text">评论人：</div>
              <div class="content-text">{{comment.usname}}</div>
            </div>
            <div class="comment-row">
              <div class="title-text">评论内容：</div>
              <div class="content-text">{{comment.actext}}</div>
            </div>
            <div class="comment-row">
              <div class="title-text">评论时间：</div>
              <div class="content-text">{{comment.acocreatetime}}</div>
            </div>
            <div class="comment-row">
              <div class="title-text">用户身份：</div>
              <div class="content-text">{{comment.robot}}</div>
            </div>
            <div class="reply-box">
              <div v-for="(item, index) in comment.reply">
                <div class="reply-title-box">
                  <div>第{{comment.reply.length - index}}次回复</div>
                  <div class="delete-reply-btn" @click="deleteComment(item, index, 'reply')">删除</div>
                </div>
                <div class="comment-row" style="margin-top: 0.1rem" v-if="comment.reply">
                  <div class="title-text">回复人：</div>
                  <div class="content-text">{{item.user.suname}}</div>
                </div>
                <div class="comment-row" v-if="comment.reply">
                  <div class="title-text">回复内容：</div>
                  <div class="content-text">{{item.actext}}</div>
                </div>
                <div class="comment-row" v-if="comment.reply">
                  <div class="title-text">回复时间：</div>
                  <div class="content-text">{{item.acocreatetime}}</div>
                </div>
              </div>
            </div>
            <div class="comment-row" style="margin-top: 0.2rem">
              <div class="title-text" v-if="comment.reply">再次回复：</div>
              <div class="title-text" v-if="!comment.reply">回 复：</div>
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
        page_size: 10,          // 每页显示的数量
        total_page: 1,          // 总页数
        page_num: 1,            // 第几页
        total_num: 1,           // 总条数
      }
    },
    props: {
      // activity: { type: Object, default: {} },    // 点击的推文
    },
    components:{ Pagination },
    methods: {
      // 获取点击的推文下的评论-嵌套回复
      getComments(activity) {
        if(activity) {
          this.activity = activity;
        }
        this.commentsDialog = true;
        this.commentLoading = true;
        axios.get(api.get_comment_with_apply + "?token=" + localStorage.getItem("token") + "&acid=" + this.activity.acid + "&count=" + this.page_size + "&page=" + this.page_num).then(res => {
          if(res.data.status == 200) {
            this.commentList = res.data.data;
            this.total_page = Math.ceil(res.data.count / this.page_size);
            this.total_num = res.data.count;

            for(let i = 0; i < this.commentList.length; i ++) {
              if(this.commentList[i].user.robot == "0") {
                this.commentList[i].robot = "真实用户";
              }else if(this.commentList[i].user.robot == "1") {
                this.commentList[i].robot = "小马甲用户";
              }
              this.commentList[i].usname = this.commentList[i].user.usname;

              // 处理评论的回复状态
              this.commentList[i].replyStatus = "未回复";
              if(this.commentList[i].reply != undefined) {
                this.commentList[i].replyStatus = "已回复";
              }
            }

            this.commentLoading = false;
          }else{
            this.$message({ message: res.data.message, type: 'error', duration: 1500 });
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
        if(this.replyText) {
          let params = {
            acoid: this.comment.acoid,
            ACtext: this.replyText
          };
          axios.post(api.add_comment + '?token=' + localStorage.getItem('token'), params).then(res=>{
            if(res.data.status == 200){
              this.$message({ message: "回复成功", type: 'success', duration: 1500 });
              this.replyComments = false;

              // 回复成功后更新数据
              this.replyText = "";
              this.getComments();
            }else{
              this.$message({ message: res.data.message, type: 'error', duration: 1500 });
            }
          });
        }else {
          this.replyComments = false;
        }
      },

      // 删除评论
      deleteComment(scope, index, where) {
        if(where == "comment") {
          this.$confirm("此操作将删除该条评论, 是否继续?", "提示",
            {confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
            this.commentLoading = true;
            axios.post(api.del_comment + '?token=' + localStorage.getItem('token'), { acoid: scope.acoid }).then(res=>{
              if(res.data.status == 200){
                this.commentLoading = false;
                this.$message({ message: "删除成功", type: 'success', duration: 1500 });
                this.commentList.splice(index, 1);    // 刷新视图
                this.total_page = Math.ceil((this.total_num - 1) / this.page_size);   // 页码更新
              }else{
                this.$message({ type: 'error', message: res.data.message, duration: 1500 });
              }
            });
          }).catch(() => {  });
        }else if(where == "reply") {
          this.$confirm("此操作将删除该条回复, 是否继续?", "提示",
            {confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning'}).then(() => {
            axios.post(api.del_comment + '?token=' + localStorage.getItem('token'), { acoid: scope.acoid }).then(res=>{
              if(res.data.status == 200){
                this.$message({ message: "删除成功", type: 'success', duration: 1500 });
                this.comment.reply.splice(index, 1);    // 刷新视图
              }else{
                this.$message({ type: 'error', message: res.data.message, duration: 1500 });
              }
            });
          }).catch(() => {  });
        }
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
    margin-top: 0.2rem;
    text-align: right;
  }
  .comment-box {
    margin: -0.3rem -0.2rem;
    padding: 0.2rem 0.5rem;
    .comment-row {
      display: flex;
      padding: 0.03rem 0;
      .title-text {
        width: 0.6rem;
        white-space: nowrap;
      }
      .content-text {
        width: 4.5rem;
        margin-left: 0.1rem;
      }
    }
    .reply-box {
      margin: 0.1rem 0;
      overflow-y: auto;
      overflow-x: hidden;
      max-height: 2rem;
      .reply-title-box {
        display: flex;
        margin: 0.1rem 0 -0.1rem 0;
        .delete-reply-btn {
          color: #4169E1;
          font-size: 0.11rem;
          margin-left: 0.1rem;
        }
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
