<template>
    <div ref="vantaRef" style="width:100%;height:100vh">
      <div class="my_title">Welcome</div>
      <div class="login_box">
        <div class="avatar_box">
          <img src="../../assets/logo.png" alt="">
        </div>
        <el-form ref="loginFormRef" :model="loginForm" :rules="loginFormRules" label-width="0px" class="login_form">
          <!--用户名-->
          <el-form-item prop="username">
            <el-input v-model="loginForm.username" prefix-icon="el-icon-user-solid"></el-input>
          </el-form-item>
          <!--密码-->
          <el-form-item prop="password">
            <el-input v-model="loginForm.password" prefix-icon="el-icon-lock" type="password"></el-input>
          </el-form-item>
          <!--用户名-->
          <el-form-item class="btns">
              <el-button type="primary" @click="login">登录</el-button>
              <el-button type="info" @click="resetLoginForm" >重置</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </template>
  
<script>
import axios from 'axios';
import * as THREE from 'three'
import Rings from "vanta/src/vanta.rings"

  export default {
    data() {
      return {
        // 登录表单的数据绑定对象
        loginForm:{
          username: '',
          password: ''
        },
        loginFormRules:{
          username:[
            // required:true是必填项
            // trigger:'blur'是指当文本框失去焦点触发
            {required:true, message:'请输入登录名称',trigger:'blur'},
            // 限定用户名在3-10个字之间
            {min:3,max:10,message:'长度在3到10个字符',trigger:'blur'}
          ],
          password:[
             // required:true是必填项
            // trigger:'blur'是指当文本框失去焦点触发
            {required:true, message:'请输入登录密码',trigger:'blur'},
            // 限定用户名在4-8个字之间
            {min:4,max:8,message:'长度在4到8个字符',trigger:'blur'}
          ]
          
        }
      }
    },
    mounted() {
    this.vantaEffect = Rings({
      el: this.$refs.vantaRef,
      THREE: THREE
    })
  },
  beforeDestroy() {
    if (this.vantaEffect) {
      this.vantaEffect.destroy()
    }
  },
  methods:{            
      login(){
        const params = new URLSearchParams();
        params.append("username",this.loginForm.username);
        params.append("password",this.loginForm.password);
        axios.post('http://127.0.0.1:5000/admin/login',params,{})
        .then(res => {
          if(res.data.code == "0"){
            this.$message.success("登陆成功");
            window.sessionStorage.setItem('id',res.data.data.user.id);
            this.$router.push('/home')
          }else{
            console.log(res.data)
            this.$message.warning(res.data.message);
          }
        })
        .catch(err => {
          this.$message.warning('登录异常');
          console.log('登录异常',err)
        })
      },
      resetLoginForm(){
        // 点击重置按钮，重置表单
        this.$refs.loginFormRef.resetFields();
      }
    }
}
</script>
 

<style lang="less" scoped>
@import url("//unpkg.com/element-ui@2.15.14/lib/theme-chalk/index.css");

.login_box {
    width: 450px;
    height: 300px;
    background-color: #fff;
    border-radius: 3px;
    position: absolute;
    left: 20%;
    top: 50%;
    transform: translate(-50%, -50%);
}
 
.avatar_box {
    width: 130px;
    height: 130px;
    border: 1px solid #eee;
    border-radius: 50%;
    padding: 10px;
    box-shadow: 0 0 10px #ddd;
    position: absolute;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #fff;
 
    img{
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background-color: #eee;
    }
}

.login_form{
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 0px 20px;
  box-sizing: border-box;
}

.btns{
  display: flex;
  justify-content: flex-end;
}

.my_title{
  z-index: 999;
  position: fixed;
  top: 9%;
  left: 5.6%;
  color: aquamarine;
  font-size: 100px;
  font-weight: bolder;
  font-style: italic;
}
</style>
