package com.dlg.blog_project.controller;

import com.dlg.blog_project.pojo.Custom;
import com.dlg.blog_project.service.CustomService;
import com.dlg.blog_project.utils.ResponseUtils;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import javax.annotation.Resource;
import java.util.List;

@RestController
@RequestMapping("/admin")
@CrossOrigin
public class CustomController {
    @Resource
    private CustomService customService;

    @GetMapping("/custom")
    @ResponseBody
    public ResponseUtils customShow(){
        ResponseUtils resp;
        try {
            List<Custom> custom = customService.customShow();
            resp = new ResponseUtils().put("custom",custom);
        }catch (Exception e){
            e.printStackTrace();
            resp = new ResponseUtils(e.getClass().getSimpleName(), e.getMessage());
        }
        return resp;
    }

    @PostMapping("/custom/add")
    public ResponseUtils addCustom(@RequestParam(value = "file", required = false) MultipartFile file, @RequestParam("title") String title, @RequestParam("description") String description){
        ResponseUtils resp;
        try {
            Custom custom = new Custom();
            custom.setDescription(description);
            custom.setTitle(title);
            custom.setFile(file);
            customService.Insert(custom);
            resp = new ResponseUtils();
        }catch (Exception e){
            e.printStackTrace();
            resp = new ResponseUtils(e.getClass().getSimpleName(),e.getMessage());
        }
        return resp;
    }

    @GetMapping("/custom/delete")
    public ResponseUtils deleteCustom(Integer ID){
        ResponseUtils resp;
        try {

            customService.Delete(ID);
            resp = new ResponseUtils();
        }catch (Exception e){
            e.printStackTrace();
            resp = new ResponseUtils(e.getClass().getSimpleName(), e.getMessage());
        }
        return resp;
    }

    @PostMapping("/custom/edit")
    public ResponseUtils updatecustom(@RequestParam(value = "file", required = false) MultipartFile file, @RequestParam("title") String title, @RequestParam("description") String description,@RequestParam("ID") Integer ID){
        ResponseUtils resp;
        try {
            Custom custom = new Custom();
            custom.setID(ID);
            custom.setDescription(description);
            custom.setTitle(title);
            custom.setFile(file);
            customService.Update(custom);
            resp = new ResponseUtils();
        }catch (Exception e){
            e.printStackTrace();
            resp = new ResponseUtils(e.getClass().getSimpleName(),e.getMessage());
        }
        return resp;
    }
}
