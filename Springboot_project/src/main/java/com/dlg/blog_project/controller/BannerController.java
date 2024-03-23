package com.dlg.blog_project.controller;

import com.dlg.blog_project.pojo.Banner;
import com.dlg.blog_project.service.BannerService;
import com.dlg.blog_project.utils.ResponseUtils;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;
import java.util.List;

@RestController
@RequestMapping("/admin")
@CrossOrigin
public class BannerController {
    @Resource
    private BannerService bannerService;

    @GetMapping("/banners")
    @ResponseBody
    public ResponseUtils showBanners(){
        ResponseUtils resp;
        try {
            List<Banner> bannner = bannerService.bannersShow();
            resp = new ResponseUtils().put("banner",bannner);
        }catch (Exception e){
            e.printStackTrace();
            resp = new ResponseUtils(e.getClass().getSimpleName(),e.getMessage());
        }
        return resp;
    }

    @PostMapping("/banners/add")
    public ResponseUtils addBanners(Banner b){
        ResponseUtils resp;
        try {
            Banner banner = new Banner();
            banner.setDescription(b.getDescription());
            banner.setHref(b.getHref());
            banner.setTitle(b.getTitle());
            bannerService.Insert(banner);
            resp = new ResponseUtils();
        }catch (Exception e){
            e.printStackTrace();
            resp = new ResponseUtils(e.getClass().getSimpleName(), e.getMessage());
        }
        return resp;

    }

    @GetMapping("/banners/delete")
    public ResponseUtils deleteBanners(Integer ID){
        ResponseUtils resp;
        try {
            bannerService.Delete(ID);
            resp = new ResponseUtils();
        }catch (Exception e){
            e.printStackTrace();
            resp = new ResponseUtils(e.getClass().getSimpleName(),e.getMessage());
        }
        return resp;
    }

    @PostMapping("/banners/edit")
    public ResponseUtils updateBanners(String title,String description,String href,Integer ID){
        ResponseUtils resp;
        try {
            bannerService.Update(title,description,href,ID);
            resp = new ResponseUtils();
        }catch (Exception e){
            e.printStackTrace();
            resp = new ResponseUtils(e.getClass().getSimpleName(),e.getMessage());
        }
        return resp;
    }
}
