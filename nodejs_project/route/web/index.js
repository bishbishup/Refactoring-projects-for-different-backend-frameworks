const express = require('express');
const mysql = require('mysql');

var db = mysql.createPool({host:'localhost',user:'root',password:'1234',database:'learn'})

module.exports = function(){
    var rounter = express.Router();

    rounter.get('/get_banners',(req,res)=>{
        db.query(`SELECT * FROM banner_table`,(err,data)=>{
            if(err){
                console.error(err);
                res.status(500).send('database error').end();
            }else{
                res.send(data).end();
            }
        });
    });

    rounter.get('/get_custom_evaluations',(req,res)=>{
        db.query(`SELECT * FROM custom_evaluation_table`,(err,data)=>{
            if(err){
                console.error(err);
                res.status(500).send('database error').end();
            }else{
                res.send(data).end();
            }
        });
    });

    return rounter;
};