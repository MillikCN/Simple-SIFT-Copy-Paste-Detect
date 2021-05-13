# 实验结果分析——复制粘贴篡改检测

## 前言

本次实验我采用了SIFT关键点采样算法作为核心算法，使用opencv作为主要依赖。

对于每张图片，首先读入RGB图像，再转换为灰度图像，使用opencv库中的SIFT算法检测关键点后，返回坐标数组（包含角度等信息）及关键点信息矩阵，每个关键点共有128个特征值，通过特征值进行点匹配。

计算各关键点特征值与其他关键点的欧氏距离，当小于阈值(0.4)时则意味着匹配，将match数组相应项修改。再根据match数组值，寻找坐标数组中的坐标，在原图上的匹配关键点画线，即完成。

处理每张图片后，均会输出关键点数量及处理时间，当关键点较多时（>=10000）处理速度较慢，超过1分钟

本次测试集中的image002.jpg取样到了17万个关键点，因而处理速度极慢，于是我选择了每100点取一点进行匹配计算

但由于本人**从未学过CV相关内容，根本不熟悉**NumPy/Opencv相关内容，且课堂上也未对相关函数用法做培训，所以我无法做到真正的取样，由于每一点仍然需要与剩余的17万余点相匹配，所以速度仍然很慢，但至少可以跑出结果了。时间紧任务重，取样算法只能留待以后完善了。

## 结果展示

以下是在本人PC上得到的结果

[ image001.jpg ]
number of key points: 411
Processing Time: 1.265625 s

[ image002.jpg ]
number of key points: 173952
Processing Time: 390.46875 s

[ image003.jpg ]
number of key points: 325
Processing Time: 0.109375 s

[ image004.jpg ]
number of key points: 3006
Processing Time: 5.203125 s

[ image005.jpg ]
number of key points: 13959
Processing Time: 101.953125 s

[ image006.jpg ]
number of key points: 1058
Processing Time: 0.578125 s



![image-20210509181605561](C:\Users\Millik\AppData\Roaming\Typora\typora-user-images\image-20210509181605561.png)

---

对于一些尺寸较小的图片，处理时间较快，且能较好的标出结果，例如1、3、6号图片：

![image-20210509182612640](C:\Users\Millik\AppData\Roaming\Typora\typora-user-images\image-20210509182612640.png)

![image-20210509182640108](C:\Users\Millik\AppData\Roaming\Typora\typora-user-images\image-20210509182640108.png)

而对于一些尺寸较大，关键点较多的图片，受制于NumPy矩阵处理性能，处理时间就很慢了，且如果使用了取样的方法，则只能达到很一般的匹配效果，如2、5号图片：

![image-20210509182745297](C:\Users\Millik\AppData\Roaming\Typora\typora-user-images\image-20210509182745297.png)

![image-20210509182755493](C:\Users\Millik\AppData\Roaming\Typora\typora-user-images\image-20210509182755493.png)