package com.dlg.blog_project.utils;

import org.junit.Test;

import static org.junit.Assert.*;

public class Md5UtilsTest {

    @Test
    public void md5() {
        String md5 = Md5Utils.md5("123456" + Md5Utils.getMd5Suffix());
        System.out.println(md5);
    }

    @Test
    public void getMd5Suffix() {

    }
}