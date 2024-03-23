package com.dlg.blog_project.utils;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Md5Utils {

    private static final String MD5_SUFFIX = "FDSW$t34tregt5tO&$(#RHuyoyiUYE*&OI$HRLuy87odlfh是个风格热腾腾)";

    /**
     * 生成 MD5 哈希值
     */

    public static String md5(String str) {
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] messageDigest = md.digest(str.getBytes());
            StringBuilder hexString = new StringBuilder();

            for (byte b : messageDigest) {
                String hex = Integer.toHexString(0xFF & b);
                if (hex.length() == 1) {
                    hexString.append('0');
                }
                hexString.append(hex);
            }

            return hexString.toString();
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }

        return null;
    }

    public static String getMd5Suffix() {
        return MD5_SUFFIX;
    }
}