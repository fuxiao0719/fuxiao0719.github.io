import numpy as np
import cv2

file = '2_'
h_uni = 700
w_uni = 560

rgb_file = file + 'rgb.jpg'
rgb = cv2.imread(rgb_file)
h, w = rgb.shape[:2]
cv2.imwrite(rgb_file, cv2.resize(rgb, (w_uni, int(h/560*h_uni)), interpolation=cv2.INTER_CUBIC)[100:800,:,:])

# ours_depth_file = file + 'ours_depth.jpg'
# ours_depth = cv2.imread(ours_depth_file)
# h, w = ours_depth.shape[:2]
# cv2.imwrite(ours_depth_file, cv2.resize(ours_depth, (w_uni,int(h/560*h_uni)), interpolation=cv2.INTER_CUBIC)[100:800,:,:])

# ours_normal_file = file + 'ours_normal.jpg'
# ours_normal = cv2.imread(ours_normal_file)
# h, w = ours_normal.shape[:2]
# cv2.imwrite(ours_normal_file, cv2.resize(ours_normal, (w_uni,int(h/560*h_uni)), interpolation=cv2.INTER_CUBIC)[100:800,:,:])

# marigold_file = file + 'marigold.jpg'
# marigold = cv2.imread(marigold_file)
# h, w = marigold.shape[:2]
# cv2.imwrite(marigold_file, cv2.resize(marigold, (w_uni,int(h/560*h_uni)), interpolation=cv2.INTER_CUBIC)[100:800,:,:])

omnidata_file = file + 'omnidata.jpg'
omnidata = cv2.imread(omnidata_file)
h, w = omnidata.shape[:2]
cv2.imwrite(omnidata_file, cv2.resize(omnidata, (w_uni,int(h/560*h_uni)), interpolation=cv2.INTER_CUBIC)[100:800,:,:])

# depthany_file = file + 'depthany.jpg'
# depthany = cv2.imread(depthany_file)
# h, w = depthany.shape[:2]
# cv2.imwrite(depthany_file, cv2.resize(depthany, (w_uni,int(h/560*h_uni)), interpolation=cv2.INTER_CUBIC)[100:800,:,:])

dsine_file = file + 'dsine.jpg'
dsine = cv2.imread(dsine_file)
h, w = dsine.shape[:2]
cv2.imwrite(dsine_file, cv2.resize(dsine, (w_uni,int(h/560*h_uni)), interpolation=cv2.INTER_CUBIC)[100:800,:,:])