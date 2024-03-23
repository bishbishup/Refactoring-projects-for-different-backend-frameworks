package com.dlg.blog_project.pojo;

import org.springframework.web.multipart.MultipartFile;

public class Custom {
    private Integer ID;
    private String title;
    private String description;
    private String src;
    private MultipartFile file;

    public Custom(Integer ID, String title, String description, String src, MultipartFile file) {
        this.ID = ID;
        this.title = title;
        this.description = description;
        this.src = src;
        this.file = file;
    }

    public Custom() {
    }

    public MultipartFile getFile() {
        return file;
    }

    public void setFile(MultipartFile file) {
        this.file = file;
    }

    public Integer getID() {
        return ID;
    }

    public void setID(Integer ID) {
        this.ID = ID;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
}
