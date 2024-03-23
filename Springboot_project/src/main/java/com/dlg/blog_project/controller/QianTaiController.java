package com.dlg.blog_project.controller;

import com.dlg.blog_project.pojo.Custom;
import com.dlg.blog_project.service.CustomService;
import com.dlg.blog_project.utils.ResponseUtils;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;
import java.util.List;

@RestController
@RequestMapping("/qiantai")
@CrossOrigin
public class QianTaiController {
    @Resource
    private CustomService customService;

    @GetMapping("/get_custom_evaluations")
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
}
