package com.dlg.blog_project.controller;

import com.dlg.blog_project.pojo.User;
import com.dlg.blog_project.service.UserService;
import com.dlg.blog_project.utils.ResponseUtils;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;

@RestController
@RequestMapping("/admin")
@CrossOrigin
public class LoginController {
    @Resource
    private UserService userService;

    @PostMapping("/login")
    @ResponseBody
    public ResponseUtils checkLogin(String username,String password){
        ResponseUtils resp;
        try{
            User user = userService.checkLogin(username,password);
            user.setPassword(null);
            resp = new ResponseUtils().put("user",user);
        }catch (Exception e){
            e.printStackTrace();
            resp = new ResponseUtils(e.getClass().getSimpleName(),e.getMessage());
        }
        return resp;
    }
}
