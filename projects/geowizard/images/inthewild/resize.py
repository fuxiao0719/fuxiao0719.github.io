import numpy as np
import cv2
file = '2_'

rgb_file = file + 'rgb.jpg'
rgb = cv2.imread(rgb_file)
h, w = rgb.shape[:2]
cv2.imwrite(rgb_file, cv2.resize(rgb, (int(w/h*700),700), interpolation=cv2.INTER_CUBIC))

ours_depth_file = file + 'ours_depth.jpg'
ours_depth = cv2.imread(ours_depth_file)
h, w = ours_depth.shape[:2]
cv2.imwrite(ours_depth_file, cv2.resize(ours_depth, (int(w/h*700),700), interpolation=cv2.INTER_CUBIC))

ours_normal_file = file + 'ours_normal.jpg'
ours_normal = cv2.imread(ours_normal_file)
h, w = ours_normal.shape[:2]
cv2.imwrite(ours_normal_file, cv2.resize(ours_normal, (int(w/h*700),700), interpolation=cv2.INTER_CUBIC))

marigold_file = file + 'marigold.jpg'
marigold = cv2.imread(marigold_file)
h, w = marigold.shape[:2]
cv2.imwrite(marigold_file, cv2.resize(marigold, (int(w/h*700),700), interpolation=cv2.INTER_CUBIC))

omnidata_file = file + 'omnidata.jpg'
omnidata = cv2.imread(omnidata_file)
h, w = omnidata.shape[:2]
cv2.imwrite(omnidata_file, cv2.resize(omnidata, (int(w/h*700),700), interpolation=cv2.INTER_CUBIC))

depthany_file = file + 'depthany.jpg'
depthany = cv2.imread(depthany_file)
h, w = depthany.shape[:2]
cv2.imwrite(depthany_file, cv2.resize(depthany, (int(w/h*700),700), interpolation=cv2.INTER_CUBIC))

dsine_file = file + 'dsine.jpg'
dsine = cv2.imread(dsine_file)
h, w = dsine.shape[:2]
cv2.imwrite(dsine_file, cv2.resize(dsine, (int(w/h*700),700), interpolation=cv2.INTER_CUBIC))