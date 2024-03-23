<template>
<div>
	<!-- Bootstrap -->
	<link href="../../../static/css/bootstrap.min.css" rel='stylesheet' type='text/css' />
	<link href="../../../static/css/bootstrap.css" rel='stylesheet' type='text/css' />
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<!-- start slider -->
		<link href="../../../static/css/slider.css" rel="stylesheet" type="text/css" media="all" />
	<!----font-Awesome----->
		<link rel="stylesheet" href="../../../static/fonts/css/font-awesome.min.css">
	<!----font-Awesome----->
	<link href="../../../static/css/style.css" rel="stylesheet" type="text/css" media="all" />
	<div class="header_bg">
	<div class="container">
		<div class="row header">
			<div class="logo navbar-left">
				<h1><a href="../../../static/index.html">Learner </a></h1>
			</div>
			<div class="h_search navbar-right">
				<form>
					<input type="text" class="text" value="Enter text here" onFocus="this.value = '';" onBlur="if (this.value == '') {this.value = 'Enter text here';}">
					<input type="submit" value="search">
				</form>
			</div>
			<div class="clearfix"></div>
		</div>
	</div>
	</div>
	<div class="container">
		<div class="row h_menu">
			<nav class="navbar navbar-default navbar-left" role="navigation">
				<!-- Brand and toggle get grouped for better mobile display -->
				<div class="navbar-header">
				<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
					<span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				</div>
				<!-- Collect the nav links, forms, and other content for toggling -->
				<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
				<ul class="nav navbar-nav">
					<li class="active"><a href="../../../static/index.html">Home</a></li>
					<li><a href="../../../static/technology.html">Technologies</a></li>
					<li><a href="../../../static/about.html">About</a></li>
					<li><a href="../../../static/blog.html">Blog</a></li>
					<li><a href="../../../static/contact.html">Contact</a></li>
				</ul>
				</div><!-- /.navbar-collapse -->
				<!-- start soc_icons -->
			</nav>
			<div class="soc_icons navbar-right">
				<ul class="list-unstyled text-center">
					<li><a href="#"><i class="fa fa-twitter"></i></a></li>
					<li><a href="#"><i class="fa fa-facebook"></i></a></li>
					<li><a href="#"><i class="fa fa-google-plus"></i></a></li>
					<li><a href="#"><i class="fa fa-youtube"></i></a></li>
					<li><a href="#"><i class="fa fa-linkedin"></i></a></li>
				</ul>
			</div>
		</div>
	</div>
	<div class="slider_bg"><!-- start slider -->
		<div class="container">
			<div id="da-slider" class="da-slider text-center">
				<div ng-hide="item.hide" class="da-slide" ng-repeat="item in banners">
					<h2>[[item.title]]</h2>
					<p>[[item.description]]</p>
					<h3 class="da-link"><a href="[[item.href]]" class="fa-btn btn-1 btn-1e">view more</a></h3>
				</div>
		</div>
		</div>
	</div><!-- end slider -->
	<div class="main_bg"><!-- start main -->
		<div class="container">
			<div class="main row">
				<div class="col-md-3 images_1_of_4 text-center">
					<span class="bg"><i class="fa fa-globe"></i></span>
					<h4><a href="#">Sed Porta Dolor</a></h4>
					<p class="para">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text 1500s.</p>
					<a href="../../../static/single-page.html" class="fa-btn btn-1 btn-1e">read more</a>
				</div>
				<div class="col-md-3 images_1_of_4 bg1 text-center">
					<span class="bg"><i class="fa fa-laptop"></i></span>
					<h4><a href="#">Lorem Ipsum is</a></h4>
					<p class="para">It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.</p>
					<a href="../../../static/single-page.html" class="fa-btn btn-1 btn-1e">read more</a>
				</div>
				<div class="col-md-3 images_1_of_4 bg1 text-center">
					<span class="bg"><i class="fa fa-cog"></i></span>
					<h4><a href="#">Sed Porta Dolor</a></h4>
					<p class="para">The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32  by H. Rackham.</p>
					<a href="../../../static/single-page.html" class="fa-btn btn-1 btn-1e">read more</a>
				</div>
				<div class="col-md-3 images_1_of_4 bg1 text-center">
					<span class="bg"><i class="fa fa-shield"></i> </span>
					<h4><a href="#">Contrary  belief</a></h4>
					<p class="para">There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour.</p>
					<a href="../../../static/single-page.html" class="fa-btn btn-1 btn-1e">read more</a>
				</div>
			</div>
		</div>
	</div><!-- end main -->
	<div class="main_btm"><!-- start main_btm -->
		<div class="container">
			<div class="main row">
				<div class="col-md-6 content_left">
					<img src="../../../static/images/pic1.jpg" alt="" class="img-responsive">
				</div>
				<div class="col-md-6 content_right">
					<h4>Lorem Ipsum is simply <span>dummy text of the ornare  </span> vulputate printing and  There are many variations of passages.</h4>
					<p class="para">There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words. </p>
					<a href="../../../static/single-page.html" class="fa-btn btn-1 btn-1e">read more</a>
				</div>
			</div>
		</div>
	</div>
	
	<!--前台只展示评价-->
	<!----start-img-cursual---->	
	<div class="customdata">
		<el-table :data="qiancustomData"  height="500" border>
			<el-table-column label="ID" prop="id" width="100" align="center">
			</el-table-column>
			<el-table-column label="标题" prop="title" align="center">
			</el-table-column>
			<el-table-column label="描述" prop="description" align="center">
			</el-table-column>
			<el-table-column label="头像" prop="src" width="150" align="center">
				<template #default="scope">
					<div style="width: 100px; height: 100px;">
						<el-image fit="scale-down" :src="scope.row.src" style="width: 100px; height: 100px;"></el-image>
					</div>
				</template>
			</el-table-column>
		</el-table>
	</div>
	<!----//End-img-cursual---->

</div>
</template>

<script type="application/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } </script>
<script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
<script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
<!-- start plugins -->
<script type="text/javascript" src="../../../static/js/jquery.min.js"></script>
<script type="text/javascript" src="../../../static/js/bootstrap.js"></script>
<script type="text/javascript" src="../../../static/js/bootstrap.min.js"></script>
<script src="../../../static/js/angular.js" charset="utf-8"></script>

<script>
import axios from 'axios';
export default{
    data () {
    return {
		qiancustomData:[],
     }
    },
    methods:{
    },
	//----------------------------------------------
	// 只展示评论图片的功能
	created:function(){
        axios.get('http://127.0.0.1:5000/qiantai/get_custom_evaluations')
        .then(res => {
        	if(res.data.code == '0'){
				// 展示数据
				this.qiancustomData= res.data.data.custom;
        	}else{
				this.$message.warning(res.data.message);
            }
        })
        .catch(err => {
          this.$message.warning('展示异常');
          console.log('展示异常',err)
        })
    },

}
</script>

<style lang="css" scoped>

</style>
