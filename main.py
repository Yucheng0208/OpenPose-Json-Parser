#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import time

file_path = "./json/"
file_i = 0
pose_kepoints = []
filename_keywords = "_keypoints.json"
filename = "000000000000_keypoints.json"
"""
# 設定名稱迴圈以及字串合成
for file_i in range(1000000000000):
    filename = file_path + f'{file_i:012}' + filename_keywords
    #print(filename)
"""
# 開啟json
with open(filename) as f:
    data = json.load(f)

    # 取得people底下的pose_keypoints_2d
for people_item in data['people']:
    pose_kepoints = people_item['pose_keypoints_2d']
    # print(pose_kepoints)
    # print(len(pose_kepoints))
    """
        # 定義X軸座標
        X_Nose = pose_kepoints[0]
        X_Neck = pose_kepoints[3]
        X_RShoulder = pose_kepoints[6]
        X_RElbow = pose_kepoints[9]
        X_RWrist = pose_kepoints[12]
        X_LShoulder pose_kepoints[15]
        X_LElbow = pose_kepoints[18]
        X_LWrist = pose_kepoints[21]
        X_MidHip = pose_kepoints[24]
        X_RHip = pose_kepoints[27]
        X_RKnee = pose_kepoints[30]
        X_RAnkle = pose_kepoints[33]
        X_LHip =pose_kepoints[36]
        X_LKnee = pose_kepoints[39]
        X_LAnkle = pose_kepoints[42]
        X_REye = pose_kepoints[45]
        X_LEye = pose_kepoints[48]
        X_LEar = pose_kepoints[52]
        X_LBigToe = pose_kepoints[55]
        X_LSmallToe = pose_kepoints[58]
        X_LHeel = pose_kepoints[61]
        X_RBigToe = pose_kepoints[64]
        X_RSmallToe = pose_kepoints[67]
        X_RHeel = pose_kepoints[70]
        X_Background = pose_kepoints[73]
        
        # 定義Y軸座標
        Y_Nose = pose_kepoints[1]
        Y_Neck = pose_kepoints[4]
        Y_RShoulder = pose_kepoints[7]
        Y_RElbow = pose_kepoints[10]
        Y_RWrist = pose_kepoints[13]
        Y_LShoulder pose_kepoints[16]
        Y_LElbow = pose_kepoints[19]
        Y_LWrist = pose_kepoints[22]
        Y_MidHip = pose_kepoints[25]
        Y_RHip = pose_kepoints[26]
        Y_RKnee = pose_kepoints[39]
        Y_RAnkle = pose_kepoints[34]
        Y_LHip =pose_kepoints[37]
        Y_LKnee = pose_kepoints[40]
        Y_LAnkle = pose_kepoints[43]
        Y_REye = pose_kepoints[46]
        Y_LEye = pose_kepoints[49]
        Y_LEar = pose_kepoints[53]
        Y_LBigToe = pose_kepoints[56]
        Y_LSmallToe = pose_kepoints[59]
        Y_LHeel = pose_kepoints[62]
        Y_RBigToe = pose_kepoints[65]
        Y_RSmallToe = pose_kepoints[68]
        Y_RHeel = pose_kepoints[71]
        Y_Background = pose_kepoints[74]
        """
