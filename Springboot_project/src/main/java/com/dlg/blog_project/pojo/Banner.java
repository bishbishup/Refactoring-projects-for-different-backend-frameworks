package com.dlg.blog_project.pojo;

public class Banner {
    private Integer ID;
    private String title;
    private String description;
    private String href;

    public Banner(Integer ID, String title, String description, String href) {
        this.ID = ID;
        this.title = title;
        this.description = description;
        this.href = href;
    }

    public Banner() {
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

    public String getHref() {
        return href;
    }

    public void setHref(String href) {
        this.href = href;
    }
}
