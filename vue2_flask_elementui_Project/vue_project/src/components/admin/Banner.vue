                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               <template>
  <div>
    <!--增添banner-->
    <el-form ref="form" :model="addform" style="width: 1500px;" label-width="50px" >
      <el-form-item label="标题">
        <el-input v-model="addform.title" style="width: 500px;"></el-input>
      </el-form-item>
      <el-form-item label="描述">
        <el-input v-model="addform.description" style="width: 500px;"></el-input>
      </el-form-item>
      <el-form-item label="链接">
        <el-input v-model="addform.href" style="width: 1000px;"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="success" size="medium" @click="handleadd" style="margin:0 !important">添加</el-button>
      </el-form-item>
    </el-form>

    <!-- 实时显示banner的情况-->
    <el-table :data="bannerData" border>
    <el-table-column label="ID" prop="id"  width="100" align="center">
    </el-table-column>
    <el-table-column label="标题" prop="title" width="200" align="center">
    </el-table-column>
    <el-table-column label="描述" prop="description" width="300" align="center">
    </el-table-column>
    <el-table-column label="链接" prop="href" align="center">
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
        <el-form-item label="链接">
          <el-input v-model.number="editForm.href"></el-input>
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


export default {
    data () {
    return {
      addform:{
        title:'',
        description:'',
        href:''
      },
      bannerData:[],
      search: '',
      // 控制编辑弹窗的显示与隐藏
      showEditDialog: false,  
      editForm:{
        title:'',
        description:'',
        href:''
      },
      // 获取id，并将传值给编辑的方法，
      index2:''
     }
    },
    methods: {
    // ----------------------------------------------------
    // 增加操作
    handleadd(){
        const params = new URLSearchParams();
        params.append("title",this.addform.title);
        params.append("description",this.addform.description);
        params.append("href",this.addform.href);
        axios.post('http://127.0.0.1:5000/admin/banners/add',params)
        .then(res => {
          if(res.data.code == '0'){
            this.$message.success('添加成功');
            // 提交完清空输入框
            this.addform.title = '';
            this.addform.description = '';
            this.addform.href = '';
            // 添加后实时更新
            axios.get('http://127.0.0.1:5000/admin/banners')
            .then(res => {
              if(res.data.code == '0'){
                // 展示数据
                this.bannerData = res.data.data.banner;
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
    // 点击编辑 弹窗弹出
    handleEdit(index) {
      this.showEditDialog = true;
      this.index2 = index;
    },
    // 修改数据
    saveData(){
      const params = new URLSearchParams();
      params.append("ID",this.index2);
      params.append("title",this.editForm.title);
      params.append("description",this.editForm.description);
      params.append("href",this.editForm.href);
      axios.post('http://127.0.0.1:5000/admin/banners/edit',params)
      .then(res => {
        if(res.data.code == '0'){
          this.$message.success('修改成功')
          this.editForm.title = '';
          this.editForm.description = '';
          this.editForm.href = '';
          // 修改后实时更新
          axios.get('http://127.0.0.1:5000/admin/banners')
            .then(res => {
              if(res.data.code == '0'){
                // 展示数据
                this.bannerData = res.data.data.banner;
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
    },
    // ----------------------------------------------------
    // 删除数据
    handleDelete(index) {
      axios.get('http://127.0.0.1:5000/admin/banners/delete',{
        params:{
          ID:index
        }
      })
      .then(res => {
        if(res.data.code == '0'){
          this.$message.success("删除成功");
           // 删除后实时更新
           axios.get('http://127.0.0.1:5000/admin/banners')
            .then(res => {
              if(res.data.code == '0'){
                // 展示数据
                this.bannerData = res.data.data.banner;
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
    created:function(){
        axios.get('http://127.0.0.1:5000/admin/banners')
        .then(res => {
          if(res.data.code == '0'){
            // 展示数据
            this.bannerData = res.data.data.banner;
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
  