package com.dlg.blog_project.mapper;

import com.dlg.blog_project.pojo.Custom;

import java.util.List;

public interface CustomMapper {
    public List<Custom> customShow();

    public void customInsert(Custom custom);

    public void deleteById(Integer ID);

    public void updateById(Custom custom);

    public Custom selectById(Integer ID);
}
