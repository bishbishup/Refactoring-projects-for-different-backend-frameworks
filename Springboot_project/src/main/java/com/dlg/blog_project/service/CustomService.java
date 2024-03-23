package com.dlg.blog_project.service;

import com.dlg.blog_project.pojo.Custom;

import java.util.List;

public interface CustomService {
    public List<Custom> customShow();

    public void Insert(Custom custom);

    public void Delete(Integer id);

    public void Update(Custom custom);
}
