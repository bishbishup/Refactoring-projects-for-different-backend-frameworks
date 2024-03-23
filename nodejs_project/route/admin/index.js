const express = require('express');

module.exports = function(){
    var rounter = express.Router();

    // 检查登录状态
    rounter.use((req,res,next)=>{
        if(!req.session['admin_id'] && req.url != '/login'){ // 没有登录
            res.redirect('/admin/login');
        }else{
            next();
        }
    });

    rounter.get('/',(req,res)=>{
        res.render('admin/index.ejs',{});
    });
    
    rounter.use('/login',require('./login.js')());
    rounter.use('/banners',require('./banners.js')());
    rounter.use('/custom',require('./custom.js')());

    return rounter;
}``