package com.dlg.blog_project.service.impl;

import com.dlg.blog_project.mapper.UserMapper;
import com.dlg.blog_project.pojo.User;
import com.dlg.blog_project.service.UserService;
import com.dlg.blog_project.service.exception.LoginException;
import com.dlg.blog_project.utils.Md5Utils;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
@Service
public class UserServiceImpl implements UserService {
    @Resource
    private UserMapper userMapper;
    @Override
    public User checkLogin(String username, String password) {
       User user = userMapper.selectByUserName(username);
       if (user == null){
           throw new LoginException("用户名不存在");
       }
       String md5 = Md5Utils.md5(password + Md5Utils.getMd5Suffix());
       if (!md5.equals(user.getPassword())){
           throw new LoginException("密码错误");
       }
       return user;
    }
}
