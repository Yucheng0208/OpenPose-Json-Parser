#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

pose_kepoints = []
    
with open('000000000031_keypoints.json') as f:
    data = json.load(f)
for people_item in data['people']:
    pose_kepoints = people_item['pose_keypoints_2d']
    print(pose_kepoints)
    print(type(people_item))
