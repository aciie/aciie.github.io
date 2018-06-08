numpy的下载与安装教程(windows系统)

感谢https://blog.csdn.net/llxlqy/article/details/76967830
的教程。其实已经写的非常的详细了。我只是重新记录一下numpy的安装过程，帮助自己记忆。

一开始要安装numpy是因为涉及到矩阵的计算。

numpy可以直接从这个网站下载https://pypi.org/project/numpy/#files
注意倒数第二列的Python version，要和自己的python版本一致。我这里下载的是numpy-1.14.4-cp36-none-win_amd64.whl

![](https://i.imgur.com/BZ5VG8k.png)
 
文件位置：
下载好后将文件放到python安装目录下的scripts文件夹中。如果python安装正确的话这个文件夹中应该还有pip和easy_install.

 
加入系统变量：
然后将上述文件夹路径加入到系统变量中。
方法如下：把Scripts这个目录拷贝下来,然后“右击计算机-属性-高级-环境变量-系统变量-path-编辑它”将刚才的路径粘贴进去。
 
开始安装：
 
搞定这些之后，因为我比较习惯用Windows Powershell, 所以打开Windows Powershell（x86）

首先通过命令cd进入到python的scripts目录：
cd C:\Users\ASUS\AppData\Local\Programs\Python\Python36\Scripts

然后输入命令安装numpy-1.14.4-cp36-none-win_amd64.whl
pip3.6 install C:\Users\ASUS\AppData\Local\Programs\Python\Python36\Scripts\numpy-1.14.4-cp36-none-win_amd64.whl

然后就会出现
Processing c:\users\asus\appdata\local\programs\python\python36\scripts\numpy-1.14.4-cp36-none-win_amd64.whl
Installing collected packages: numpy
Successfully installed numpy-1.14.4

然后就可以去python里面import numpy看看有没有出错啦。
