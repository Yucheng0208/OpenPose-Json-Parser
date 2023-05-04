#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import time
import numpy as np
file_path = "./json/"
file_i = 0
pose_kepoints = []
filename_keywords = "_keypoints.json"
filename = "000000000000_keypoints.json"

# 開啟json
with open(filename) as f:
    data = json.load(f)
    # 取得people底下的pose_keypoints_2d
    for people_item in data['people']:
        pose_kepoints = people_item['pose_keypoints_2d']
        print(pose_kepoints)
        print('\n')
        pose_kepoints_array = np.array(pose_kepoints)
        print(pose_kepoints_array)
        #print(np.array((json.loads(pose_kepoints))))
        #print(len(pose_kepoints))