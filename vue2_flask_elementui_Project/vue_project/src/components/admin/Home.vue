<template>
    <el-tabs v-model="activeName"  @tab-click="handleClick" stretch>
        <el-tab-pane label="首页" name="first">
           <Navigation></Navigation>
        </el-tab-pane>
    <el-tab-pane label="banner设置" name="second">
        <Banner></Banner>
    </el-tab-pane>
    <el-tab-pane label="用户评价" name="third">
        <Custom></Custom>
    </el-tab-pane>
    <el-tab-pane label="退出" name="fourth">
        <div class="button-container">
            <el-button type="info" @click="logout">退出</el-button>
        </div>
    </el-tab-pane>
  </el-tabs>
</template>

<script>
import Navigation from './Navigation.vue'
import Banner from './Banner.vue'
import Custom from './Custom.vue'

export default{
    data(){
        return{
            activeName: 'second'
        };
    },
    components:{
        Navigation,
        Banner,
        Custom
    },
    methods:{
    handleClick(){

    },
    logout(){
        // 先清空token
        window.sessionStorage.clear();
        // 重定向到/login
        this.$router.push('/login');
        this.$message.success('退出登陆成功')
      }
    }
};
</script>

<style lang="css" scoped>
.button-container {
    display: flex;
    justify-content: center; /* 水平居中 */
    margin-top: 400px;
}
</style>