package com.dlg.blog_project.service.impl;

import com.dlg.blog_project.mapper.BannerMapper;
import com.dlg.blog_project.pojo.Banner;
import com.dlg.blog_project.service.BannerService;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.List;

@Service
public class BannerServiceImpl implements BannerService {
    @Resource
    private BannerMapper bannerMapper;
    @Override
    public List<Banner> bannersShow() {
        return bannerMapper.bannersShow();
    }

    @Override
    public void Insert(Banner banner) {
        bannerMapper.bannersInsert(banner);
    }

    @Override
    public void Delete(Integer ID) {
        bannerMapper.deleteById(ID);
    }

    @Override
    public void Update(String title,String description,String href,Integer ID) {
        Banner banner = bannerMapper.selectById(ID);
        if (title.equals("")){
            title = banner.getTitle();
        }
        if (description.equals("")){
            description = banner.getDescription();
        }
        if (href.equals("")){
            href = banner.getHref();
        }
        bannerMapper.updateById(title,description,href,ID);
    }
}
