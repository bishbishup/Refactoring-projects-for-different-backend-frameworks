<template>
  <div>
  <!--增添custom-->
  <el-form ref="form" :model="addform" style="width: 1500px;" label-width="50px" >
      <el-form-item label="标题">
        <el-input v-model="addform.title" style="width: 500px;"></el-input>
      </el-form-item>
      <el-form-item label="描述">
        <el-input v-model="addform.description" style="width: 500px;"></el-input>
      </el-form-item>
      <el-form-item label="头像">
        <el-upload
          drag
          ref="upload"
          action="http://127.0.0.1:5000/admin/custom/add"
          :http-request="httpRequest"
          :before-upload="beforeUpload"
          :limit="1"
          :on-exceed="handleExceed"
          :on-change="handleChange"
        >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">
            将文件拖到此处，或
            <em>点击上传</em>
          </div>
        </el-upload>
      </el-form-item>
      <el-form-item>
        <el-button type="success" size="medium" @click="submit" style="margin:0 !important">添加</el-button>
      </el-form-item>
  </el-form>

  <!-- 实时显示custom的情况-->
  <el-table :data="customData"  height="500" border>
    <el-table-column label="ID" prop="id" width="100" align="center">
    </el-table-column>
    <el-table-column label="标题" prop="title" align="center">
    </el-table-column>
    <el-table-column label="描述" prop="description" align="center">
    </el-table-column>
    <el-table-column label="头像" prop="src" width="150" align="center">
      <template #default="scope">
        <div style="width: 100px; height: 100px;">
          <el-image fit="fill" :src="scope.row.src"></el-image>
        </div>
      </template>
    </el-table-column>
    <el-table-column align="right" width="300">
      <template slot="header">
        <el-input
          v-model="search"
          size="mini"
          placeholder="输入关键字搜索"/>
      </template>
      <template slot-scope="scope">
        <div class="button-container">
          <el-button type="primary" icon="el-icon-edit" circle  @click="handleEdit(scope.row.id)"></el-button>
          <el-button type="danger" icon="el-icon-delete" circle @click="handleDelete(scope.row.id)"></el-button>
        </div>
      </template>
    </el-table-column>
  </el-table>

   <!-- 点击编辑按钮后弹出的编辑弹窗 -->
   <el-dialog :visible.sync="showEditDialog" title="编辑数据">
    <!-- 编辑表单内容 -->
    <el-form ref="editForm" :model="editForm" label-width="80px">
      <el-form-item label="标题">
        <el-input v-model="editForm.title"></el-input>
      </el-form-item>
      <el-form-item label="描述">
        <el-input v-model.number="editForm.description"></el-input>
      </el-form-item>
      <el-form-item label="头像">
        <el-upload
          drag
          ref="editupload"
          action="http://127.0.0.1:5000/admin/custom/add"
          :http-request="httpRequest2"
          :before-upload="beforeUpload2"
          :on-exceed="handleExceed2"
        >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">
            将文件拖到此处，或
            <em>点击上传</em>
          </div>
        </el-upload>
      </el-form-item>
    </el-form>

    
    <div slot="footer">
      <el-button type="primary" @click="saveData">保存</el-button>
    </div>
  </el-dialog>

</div>
</template>

<script>
import axios from 'axios';

export default{
    data () {
    return {
      addform:{
        title:'',
        description:''
      },
      fileList: [],
      file2:'',
      customData:[],
      search: '',
      showEditDialog: false,  // 控制编辑弹窗的显示与隐藏
      editForm:{
        title:'',
        description:'',
      },
      // 获取id，并将传值给编辑的方法，
      index2:''
    }
  },
  methods: {
    // ----------------------------------------------------
    // 增加操作
    handleChange(file, fileList) {
      if (fileList&&fileList.length>=2) {
          fileList.shift();
      }
        this.file2 = file
    },
    // 覆盖默认的上传行为
    httpRequest (raw) {
      this.fileList.push(raw)
    },
    // 上传前
    beforeUpload (file) {
      //判断文件类型，必须是png或者jpg格式
      let fileName = file.name
      let reg = /^.+(\.(png|jpg))$/
      if (!reg.test(fileName)) {
        this.$message.error("只能上传jpg或者npg!")
        return false
      }
      return true // 允许上传
    },
    // 文件数量提醒
    handleExceed() {
      this.$message.warning('只能上传一张头像')
    },
    // 提交
    async submit (){
    // 使用form表单的数据格式
    const params = new FormData();
    this.fileList.forEach((x) => {
      console.log(x.file)
      params.append('file', x.file)
    });
    params.append('title', this.addform.title)
    params.append('description', this.addform.description)
    console.log(params.get('file'))
    axios.post('http://127.0.0.1:5000/admin/custom/add',
    params,{
    headers: {
          'Content-Type': 'multipart/form-data;'
        }}
    )
    .then(res => {
          if(res.data.code == '0'){
            this.$message.success('添加成功');
            this.addform.title = '';
            this.addform.description = '';
            // 在提交上传后的回调函数中，通过 $refs 来访问 `el-upload` 组件实例
            this.$refs.upload.clearFiles();
            this.fileList = [];
            // 添加后实时更新
            axios.get('http://127.0.0.1:5000/admin/custom')
              .then(res => {
                if(res.data.code == '0'){
                  // 展示数据
                  this.customData = res.data.data.custom;
                }else{              
                  this.$message.warning(res.data.message);
                }
              })
              .catch(err => {
                  this.$message.warning('展示异常');
                  console.log('展示异常',err)
              })
          }else{
            this.$message.warning(res.data.message);
          }
        })
  .catch(err => {
          this.$message.warning('添加异常');
          console.log('添加异常',err)
        })  
    },
    // ----------------------------------------------------
    // 修改操作
    // 点击编辑 弹窗弹出
    handleEdit(index) {
      this.showEditDialog = true;
      this.index2 = index;
    },
    // 覆盖默认的上传行为
    httpRequest2 (raw) {
      this.fileList.push(raw)
    },
    // 上传前
    beforeUpload2 (file) {
      //判断文件类型，必须是png或者jpg格式
      let fileName = file.name
      let reg = /^.+(\.(png|jpg))$/
      if (!reg.test(fileName)) {
        this.$message.error("只能上传jpg或者npg!")
        return false
      }
      return true // 允许上传
    },
    // 文件数量提醒
    handleExceed2() {
      this.$message.warning('只能上传一张头像')
    },
    // 提交
    saveData(){
    // 使用form表单的数据格式
    const params = new FormData()
    if (this.fileList.length == 0){
      params.append('file',null)
    }
    else {
      this.fileList.forEach((x) => {
        params.append('file', x.file)
      });
    }
    params.append('ID',this.index2,)
    params.append('title', this.editForm.title)
    params.append('description', this.editForm.description)
    axios.post('http://127.0.0.1:5000/admin/custom/edit',params,{
      headers: {
          'Content-Type': 'multipart/form-data;'
        }
      })
    .then(res => {
        if(res.data.code == '0'){
          this.$message.success('修改成功')
          this.editForm.title = '';
          this.editForm.description = '';
          // 在提交上传后的回调函数中，通过 $refs 来访问 `el-upload` 组件实例
          this.$refs.upload.clearFiles();
          this.fileList = [];
          // 修改后实时更新
          axios.get('http://127.0.0.1:5000/admin/custom')
            .then(res => {
              if(res.data.code == '0'){
                // 展示数据
                this.customData = res.data.data.custom;
              }else{              
                this.$message.warning(res.data.message);
              }
            })
            .catch(err => {
                this.$message.warning('展示异常');
                console.log('展示异常',err)
            })
        }else{
          this.$message.warning('修改失败')
        }
      })
    .catch(err => {
        this.$message.warning('修改异常');
        console.log('修改异常',err)
      })
       // 关闭弹窗
       this.showEditDialog = false;
       this.index2 = '';
    },
    // ----------------------------------------------------
    // 删除数据
    handleDelete(index) {
    axios.get('http://127.0.0.1:5000/admin/custom/delete',{
        params:{
          ID:index
        }
    })
    .then(res => {
        if(res.data.code == '0'){
          this.$message.success("删除成功");
           // 删除后实时更新
           axios.get('http://127.0.0.1:5000/admin/custom')
            .then(res => {
              if(res.data.code == '0'){
                // 展示数据
                this.customData = res.data.data.custom;
              }else{              
                this.$message.warning(res.data.message);
              }
            })
            .catch(err => {
                this.$message.warning('展示异常');
                console.log('展示异常',err)
            })
        }else{
          this.$message.warning('删除失败');
        }
    })
    .catch(err => {
        this.$message.warning('删除异常');
        console.log('删除异常',err)
      })
    },
  },
  // ----------------------------------------------------
  // 显示数据
  // 这个created一定要写出methods方法外
  created:function(){
    axios.get('http://127.0.0.1:5000/admin/custom')
    .then(res => {
      if(res.data.code == '0'){
        // 展示数据
        this.customData = res.data.data.custom;
      }else{              
        this.$message.warning(res.data.message);
      }
    })
    .catch(err => {
        this.$message.warning('展示异常');
        console.log('展示异常',err)
    })
  } 
}
</script>

<style scoped>
.button-container {
  text-align: center; /* 水平居中 */
}
</style>
