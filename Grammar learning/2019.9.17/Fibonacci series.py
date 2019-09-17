"""
斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学
家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子
而引入，故又称为“兔子数列”，指的是这样一个数列：1、1、2、3、5、
8、13、21、34、……在数学上，斐波那契数列以如下被以递推的方法定
义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
程序作者: Sep
"""
a = 1
b = 1
print(a)
print(b)
while True:
   a += b
   print(a)
   b += a
   print(b)
   if b > 100:
      break