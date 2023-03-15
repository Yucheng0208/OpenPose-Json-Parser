#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import time

file_path = "./json/"
file_i = 0
pose_kepoints = []
filename_keywords = "_keypoints.json"
filename = "000000000000__keypoints.json"
# 設定名稱迴圈以及字串合成
for file_i in range(1000000000000):
    filename = file_path + f'{file_i:012}' + filename_keywords
    #print(filename)

# 開啟json
    with open(filename) as f:
        data = json.load(f)

    # 取得people底下的pose_keypoints_2d
    for people_item in data['people']:
        pose_kepoints = people_item['pose_keypoints_2d']
        #print(pose_kepoints)