package com.dlg.blog_project.mapper;

import com.dlg.blog_project.pojo.Banner;

import java.util.List;

public interface BannerMapper {
    public List<Banner> bannersShow();

    public void bannersInsert(Banner banner);

    public void deleteById(Integer ID);

    public void updateById(String title,String description,String href,Integer ID);

    public Banner selectById(Integer ID);
}
