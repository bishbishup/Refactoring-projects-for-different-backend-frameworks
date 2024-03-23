package com.dlg.blog_project.service;

import com.dlg.blog_project.pojo.User;

public interface UserService {
    public User checkLogin(String username,String password);
}
