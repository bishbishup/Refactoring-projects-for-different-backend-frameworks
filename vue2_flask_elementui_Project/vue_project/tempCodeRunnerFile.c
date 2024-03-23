#include <stdio.h>

#include <tchar.h>

#include<math.h>

#include<stdio.h>

#include<stdlib.h>

int n, elem;      //n表示剖分数，node表示节点数，elem表示单元数

int * *lnd;         //lnd放置单元的节点编号

double *xco, *u;       //数组xco放置节点的坐标，数组u放置节点的数值解

double h;             //h 为步长

double gauss = 0.5773502692;       //数值积分中的高斯点

void main()

{

         int m, i, j, k, t, row, coln, e;

         double ea[2][2], alpha[2],sum1, sum2;

         double * *a, *b, *a1, *b1, *c1;

         double * *g;

         double f(double x);

         double phi(int i, double x);

         double fun1(int i, double x);

         double exact(double x);

         double fun2(int i, double x);

         double dxexact(double x);

         double fun3(int i, double x);

         double integral(double a, double b, int i, double (* fun)(int, double));

         double * chase_algorithm(double *a, double *b, double *c, int n, double *d);

        

 

         m = 40;   //总的剖分数

         printf("m=%d\n", m);

         elem = m;              //总的单元数

         h = 1.0 / m;             //网格尺度即空间步长

 

         xco = (double *)malloc(sizeof(double)*(m+1));//为节点坐标动态分配内存，放置在数组xco[]中

         for (i = 0; i<=m; i++)

                   xco[i] = i*h;    //节点坐标

 

         lnd = (int **)malloc(sizeof(int *)*elem);

         for (e = 0; e<elem; e++)

                   lnd[e] = (int *)malloc(sizeof(int)* 2);

         //为单元节点编号动态分配内存，放置在二维数组lnd[]中，lnd[e][i]表示第e个单元

         //第i个节点，e是整体单元编号，i是局部节点编号，lnd[e][i]是整体节点编号。

         for (e = 0; e<elem; e++)

         {

                   lnd[e][0] = e;

                   lnd[e][1] = e + 1;

         }         //即编号为e的单元上的第0个节点编号为e，第一个节点编号为e+1

 

         a = (double **)malloc(sizeof(double *)*(m+1));   //动态分配内存,二维数组a[ ][ ]放置总刚度矩阵，即线性方程组系数矩阵

         for (i = 0; i<=m; i++)

                   a[i] = (double *)malloc(sizeof(double)*(m+1));

         b = (double *)malloc(sizeof(double)*(m+1));//一维数组b[ ]放置总荷载即线性方程组右端项

 

         for (i = 0; i<=m; i++)   //初始化系数矩阵及右端项

         {

                   for (j = 0; j<=m; j++)

                            a[i][j] = 0;

                   b[i] = 0;

         }

         g = (double **)malloc(sizeof(double *)*elem);   //动态分配内存

         for (e = 0; e<elem; e++)

                   g[e] = (double *)malloc(sizeof(double)* 2); //放置单元荷载

 

         //计算单元刚度矩阵

         alpha[0] = -1.0 / h;//phi0'(x)

         alpha[1] = 1.0 / h; //phi1'(x)

         for (i = 0; i<2; i++)

         for (j = 0; j<2; j++)

                   ea[i][j] = alpha[i] * alpha[j] * h;

 

         for (e = 0; e<elem; e++)

         {

                   i = lnd[e][0];

                   j = lnd[e][1];

                   //利用两点高斯数值积分公式计算单元荷载

                   for (k = 0; k <= 1; k++)

                            g[e][k] = integral(xco[i], xco[j], lnd[e][k], fun1);

 

                   // 合成整体刚度矩阵

                   for (i = 0; i<2; i++)

                   {

                            for (j = 0; j<2; j++)

                            {

                                     row = lnd[e][i];   //确定整体行编号以明确合成总刚度矩阵时的位置

                                     coln = lnd[e][j];   //确定整体列编号以明确合成总刚度矩阵时的位置

                                     a[row][coln] = a[row][coln] + ea[i][j];

                            }

                            k = lnd[e][i]; //确定右端项行编号以明确合成总荷载时的位置

                            b[k] = g[e][i] + b[k]; //合成总荷载即整体右端项

                   }

         }//完成e循环

 

         //修改边界条件

         for (t = 0; t<=m; t++)

         {

                   a[t][0] = 0; a[0][t] = 0; a[t][m] = 0; a[m][t] = 0;

                   b[0] = 0; b[m] = 0;

         }

         a[0][0] = 1; a[m][m] = 1;

 

         a1 = (double *)malloc(sizeof(double)*(m + 1));//存储矩阵a[ ][ ]中的下次对角线元素

         b1 = (double *)malloc(sizeof(double)*(m + 1));//存储矩阵a[ ][ ]中的主对角线元素

         c1 = (double *)malloc(sizeof(double)*(m + 1));//存储矩阵a[ ][ ]中的上次对角线元素

         a1[0] = 0.0;

         c1[m] = 0.0;

         for (i = 0; i<=m ; i++)

         {

                   if (i!=0)

                            a1[i] = a[i][i - 1];

                   if (i!=m)

                            c1[i] = a[i][i + 1];

                   b1[i] = a[i][i];

         }

         for (i = 0; i<= m; i++)

                   free(a[i]);

         free(a);

         u=chase_algorithm(a1, b1, c1,m+1, b);//追赶法求解三对角线性方程组

         k = m / 5;//确定每隔几个点打印一次

         for (i = k; i<m; i=i+k)  //打印在各节点处的数值解并与精确解作比较

                   printf("xco[%d]=%.4f, u[%d]=%f, err=%.4e\n", i, xco[i], i, u[i], fabs(u[i] - exact(xco[i])));

//计算数值解与精确解在范数下的误差

         sum1 = 0.0;

         sum2 = 0.0;

         for (e = 0; e <elem; e++)

         {

                   i = lnd[e][0];

                   j = lnd[e][1];

                   sum1 = sum1 + integral(xco[i], xco[j],i, fun2);

                   sum2 = sum2 + integral(xco[i], xco[j], i, fun3);

         }

         printf("||u-uh||=%f, ||(u-uh)'||=%f\n", sqrt(sum1), sqrt(sum2));

 

 

}

 

double f(double x) //右端项f(x)

{

         double z;

         z = -(x+2)*exp(x);

         return z;

}

double phi(int i, double x) //基函数

{

         double temp,z;

         temp = fabs(x - xco[i]);

         if (temp <= h)

                   z = 1.0 - temp / h;

         else

                   z = 0.0;

         return z;

}

 

double fun1(int i, double x)//算单元荷载时的被积函数

{

         return f(x)*phi(i, x);

}

 

double exact(double x)//精确解u(x)

{

         return x*(exp(x)-exp(1.0));

}

 

double fun2(int i, double x)//算||u-uh||^2时的被积函数

{

         double temp, z;

         temp = u[i] * phi(i, x) + u[i + 1] * phi(i+1,x);

         z = exact(x) - temp;

         return z*z;

}

 

doubledxexact(double x)//u(x)的导函数

{

         return (x+1.0)*exp(x)-exp(1.0);

}

 

double fun3(int i, double x)//算||(u-uh)'||^2时的被积函数

{

         double temp, z;

         temp = (u[i + 1] - u[i]) / h;

         z = dxexact(x) - temp;

         return z*z;

}

 

double integral(double a, double b, int i, double (* fun)(int,double))//在区间[a,b]上对被积函数fun(i,x)进行数值积分（两点高斯公式）

{

         double mid, w, ans;

         mid = (b + a) / 2.0;

         w = (b - a) / 2.0;

         ans = w*((* fun)(i, mid + w*gauss) + (* fun)(i, mid - w*gauss));

         return ans;

}

 

double * chase_algorithm(double *a, double *b, double *c, int n, double *d)

{

         double * ans, *g, *w, p;

         int i;

         ans = (double *)malloc(sizeof(double)*n);

         g = (double *)malloc(sizeof(double)*n);

         w = (double *)malloc(sizeof(double)*n);

         g[0] = d[0] / b[0];

         w[0] = c[0] / b[0];

 

         for (i = 1; i<n; i++)

         {

                   p = b[i] - a[i] * w[i - 1];

                   g[i] = (d[i] - a[i] * g[i - 1]) / p;

                   w[i] = c[i] / p;

         }

         ans[n - 1] = g[n - 1];

         i = n - 2;

         do

         {

                   ans[i] = g[i] - w[i] * ans[i + 1];

                   i = i - 1;

         } while (i>= 0);

         free(g);

         free(w);

         return ans;

}