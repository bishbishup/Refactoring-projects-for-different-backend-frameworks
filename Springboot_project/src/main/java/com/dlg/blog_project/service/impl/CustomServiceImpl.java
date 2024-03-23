package com.dlg.blog_project.service.impl;

import com.dlg.blog_project.mapper.CustomMapper;
import com.dlg.blog_project.pojo.Custom;
import com.dlg.blog_project.service.CustomService;
import org.springframework.stereotype.Service;
import org.springframework.util.ResourceUtils;
import org.springframework.web.multipart.MultipartFile;

import javax.annotation.Resource;
import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.UUID;

@Service
public class CustomServiceImpl implements CustomService {
    @Resource
    private CustomMapper customMapper;

    @Override
    public List<Custom> customShow() {
        return customMapper.customShow();
    }

    @Override
    public void Insert(Custom custom) {
        MultipartFile file = custom.getFile();
        String fileName = file.getOriginalFilename();
        try {
            // 文件名安全性检查和生成唯一文件名
            String securityName = UUID.randomUUID() + "_" + fileName.replaceAll("[^a-zA-Z0-9.-]", "_");

            // 获取项目的根目录路径
            String rootPath = System.getProperty("user.dir");

            // 拼接
            String relativePath = rootPath + "/src/main/resources/upload";

            // 保存文件到静态目录下
            File currFile = new File(relativePath + "/" + securityName);
            file.transferTo(currFile);

            custom.setSrc("http://localhost:5000/" + securityName);

        }catch (IOException e){
            e.printStackTrace();
        }
        customMapper.customInsert(custom);
    }

    @Override
    public void Delete(Integer id) {
        Custom custom = customMapper.selectById(id);
        String src = custom.getSrc();
        String fileName = src.substring(src.lastIndexOf("/") + 1);
        File file = new File("src\\main\\resources\\upload" + "/" + fileName);
        try {
           file.delete();
        } catch (Exception e) {
           e.printStackTrace();
        }
        customMapper.deleteById(id);
    }

    @Override
    public void Update(Custom custom) {
        Custom custom2 = customMapper.selectById(custom.getID());
        if (custom.getTitle().equals("")){
            custom.setTitle(custom2.getTitle());
        }
        if (custom.getDescription().equals("")){
            custom.setDescription(custom2.getDescription());
        }
        if (custom.getFile() == null){
            custom.setSrc(custom2.getSrc());
        }else {
            // 三条都需要更改 custom已经有title和description现在修改file
            // 根据id来获取需要修改的数据记录的src
            Custom temp = customMapper.selectById(custom.getID());
            String oldSrc = temp.getSrc();
            String oldFileName = oldSrc.substring(oldSrc.lastIndexOf("/") + 1);
            File oldFile = new File("src\\main\\resources\\upload" + "/" + oldFileName);
            try {
                // 将需要修改前的文件删除掉
                oldFile.delete();
                // 将新上传的文件更新进去
                MultipartFile newfile = custom.getFile();
                String newFileName = newfile.getOriginalFilename();
                try {
                    // 文件名安全性检查和生成唯一文件名
                    String securityName = UUID.randomUUID() + "_" + newFileName.replaceAll("[^a-zA-Z0-9.-]", "_");

                    // 获取项目的根目录路径
                    String rootPath = System.getProperty("user.dir");

                    // 拼接
                    String relativePath = rootPath + "/src/main/resources/upload";

                    // 保存文件到静态目录下
                    File currFile = new File(relativePath + "/" + securityName);
                    newfile.transferTo(currFile);

                    custom.setSrc("http://localhost:5000/" + securityName);

                }catch (Exception e){
                    e.printStackTrace();
                }
            } catch (Exception e) {
               e.printStackTrace();
            }

        }
        customMapper.updateById(custom);
    }
}
