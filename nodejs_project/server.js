const express = require('express');
const static = require('express-static');
const bodyParser = require('body-parser');
const multer = require('multer')
const multerObj = multer({dest:'./big_project/static/upload'});
const mysql = require('mysql');
const cookieParser = require('cookie-parser');
const cookieSession = require('cookie-session');
const consolidate = require('consolidate');
const expressRoute = require('express-route');

var server = express();    
server.listen(8080);

// 1.获取请求数据
// get自带
server.use(bodyParser.json());
server.use(bodyParser.urlencoded({extended:false}));
server.use(multerObj.any());


// 2.cookie、session
server.use(cookieParser());
(function(){
    var keys=[];
    for(var i = 0; i < 100000; i++){
        keys[i] = 'a_'+Math.random();
    }
    server.use(cookieSession({
        name:'sess_id',
        keys:keys,
        maxAge:20*60*1000  // 20min
    }));
})();


// 3.模板
// 哪种模板引擎 
server.engine('html',consolidate.ejs);
// 模板文件放在哪
server.set('views','./big_project/template');
// 输出什么东西
server.set('view engine','html');


// 4.route
server.use('/',require('./route/web')());
server.use('/admin/',require('./route/admin')());

// 5.default、static
server.use(static('./big_project/static/'));