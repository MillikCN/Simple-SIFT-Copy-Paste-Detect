import cv2
import time
import numpy as np
imgArr = ["image001.jpg","image002.jpg","image003.jpg","image004.jpg","image005.jpg","image006.jpg"]
for holy in imgArr:
    print("[",holy,"]")
    start = time.process_time()
    img = cv2.imread(holy)
    # 读入图像
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # 转为灰度图像

    sift = cv2.SIFT_create()
    # 创建SIFT对象
    kp, des = sift.detectAndCompute(gray,None)
    # kp为关键点位坐标等信息，des为各点位特征值，共128项
    for point in range(np.size(des,axis=0)):
        des[point] = des[point] / np.linalg.norm(des[point])
    # 单位化输入各向量
    print('number of key points:', len(kp))
    # 输出关键点总数
    rowMatrix, colMatrix = des.shape[0], des.shape[1]
    match = np.ones((1,rowMatrix))

    #求取行向量与特征矩阵中每一行的欧氏距离

    for i in range(rowMatrix):
        if(rowMatrix>=100000):
            i*=100
        if(i>=rowMatrix):
            break
        vet = des[i]
        colVec = np.ones((rowMatrix,1))
        matTemp = (colVec*vet-des)**2
        distance_I_other = np.sqrt(np.sum(matTemp,1))
        vals = np.sort(distance_I_other,axis=0)
        indx = np.argsort(distance_I_other,axis=0)
        if(vals[1] < 0.4 * vals[2]):
            match[0][i] = indx[1]
        else: 
            match[0][i] = 0
    # 0.4为设置的阈值，可自由更改

    # 根据match值决定是否画线
    for i in range(rowMatrix):
        if(rowMatrix>=100000):
            i*=100
        if(i>=rowMatrix):
            break
        a = int(match[0][i])
        if(a>0):
            cv2.line(img,(int(kp[a].pt[0]),int(kp[a].pt[1])),(int(kp[i].pt[0]),int(kp[i].pt[1])),(0,255,0))

    imgRes_name = "sift_res_"+holy
    # 存取结果到文件
    cv2.imwrite(imgRes_name,img)
    end = time.process_time()
    print("Processing Time:",end-start,"s\n")
    