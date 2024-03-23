<template>
    <div>
            <el-radio-group v-model="size">
                <el-radio label="">默认</el-radio>
                <el-radio label="medium">中等</el-radio>
                <el-radio label="small">小型</el-radio>
                <el-radio label="mini">超小</el-radio>
            </el-radio-group>

            <el-descriptions class="margin-top" title="带边框列表" :column="3" :size="size" border>
                <template slot="extra">
                <el-button type="primary" size="small">操作</el-button>
                </template>
                <el-descriptions-item>
                <template slot="label">
                    <i class="el-icon-user"></i>
                    用户名
                </template>
                blue
                </el-descriptions-item>
                <el-descriptions-item>
                <template slot="label">
                    <i class="el-icon-mobile-phone"></i>
                    手机号
                </template>
                17322939032
                </el-descriptions-item>
                <el-descriptions-item>
                <template slot="label">
                    <i class="el-icon-location-outline"></i>
                    居住地
                </template>
                广州市
                </el-descriptions-item>
                <el-descriptions-item>
                <template slot="label">
                    <i class="el-icon-tickets"></i>
                    学校
                </template>
                <el-tag size="small">广州大学</el-tag>
                </el-descriptions-item>
                <el-descriptions-item>
                <template slot="label">
                    <i class="el-icon-office-building"></i>
                    联系地址
                </template>
                广州市番禺区小谷围街道外环西路230号
                </el-descriptions-item>
            </el-descriptions>
            
            <el-collapse>
                <el-collapse-item title="首页介绍" name="1">
                    <div>调用了一些Element-UI插件</div>
                </el-collapse-item>
                <el-collapse-item title="banner设置介绍" name="2">
                    <div>管理员可添加、修改和删除标题、描述、链接</div>
                    <div>页面反馈：操作后，通过页面元素的变化清晰地展现当前状态。</div>
                </el-collapse-item>
                <el-collapse-item title="用户评价介绍" name="3">
                    <div>管理员可添加、修改和删除标题、描述、头像文件</div>
                    <div>清晰明确：语言表达清晰且表意明确，让用户快速理解进而作出决策；</div>
                    <div>帮助用户识别：界面简单直白，让用户快速识别而非回忆，减少用户记忆负担。</div>
                </el-collapse-item>
                <el-collapse-item title="退出" name="4">
                    <div>退出登录</div>
                    <div>结果可控：用户可以自由的进行操作，包括撤销、回退和终止当前操作等。</div>
                </el-collapse-item>
            </el-collapse>
    </div>
</template>

<script>
export default{
    data(){
        return{
            size: ''
        };
    },
};
</script>

<style lang="css" scoped>

</style>