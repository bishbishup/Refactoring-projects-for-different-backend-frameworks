package com.dlg.blog_project.service;

import com.dlg.blog_project.pojo.Banner;

import java.util.List;

public interface BannerService {
    public List<Banner> bannersShow();

    public void Insert(Banner banner);

    public void Delete(Integer id);

    public void Update(String title,String description,String href,Integer ID);
}
