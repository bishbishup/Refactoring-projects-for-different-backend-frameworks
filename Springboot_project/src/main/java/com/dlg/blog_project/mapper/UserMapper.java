package com.dlg.blog_project.mapper;

import com.dlg.blog_project.pojo.User;

public interface UserMapper {
    public User selectByUserName(String username);
}
