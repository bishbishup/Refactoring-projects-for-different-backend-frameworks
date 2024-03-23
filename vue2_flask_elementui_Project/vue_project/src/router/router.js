import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/admin/Home'
import Login from '@/components/admin/Login'
import Qiantai from '@/components/web/Qiantai'

// 使用vue-router插件 vue.prototype.$router = router
Vue.use(Router)

const router =  new Router({
  // 匹配的路由规则 
  routes: [
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path:'/home',
      name:'home',
      component:Home
    },
    {
      path:'/',
      name:'qiantai',
      component:Qiantai
    }
  ]
})

// 挂载路由导航守卫
// 在访问其他页面前需要确保已经登陆了，否则强行打回login界面
router.beforeEach((to,from,next) => {
  // to将要访问的路径
  // from 代表从哪个路径跳转过来
  // next是一个函数，表示放行
  // 1.如果用户访问的是登录页，则直接放行
  if(to.path === '/login' || to.path === '/')
    return next()
  // 2.如果用户访问的不是登录页
  // 获取token（此时token已经存在sessionStorage里了）
  const id = window.sessionStorage.getItem('id');
  // 2.1 如果token不存在，则强制跳转到登录页/login
  if(!id)
    return next('/login')
  // 2.2 如果token存在，则直接放行
  next()
})

// 将这个路由对象暴露出去
export default router
