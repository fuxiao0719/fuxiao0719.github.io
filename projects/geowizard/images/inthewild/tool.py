import cv2
import numpy as np
for i in range(22):
    img = cv2.imread(str(i)+'_rgb.jpg')
    blank = np.ones_like(img)*255
    cv2.imwrite(str(i)+'_rgb_blank.jpg', blank)

<div class="twoitem">
    <div class="twentytwenty-container">
        <div class="cmpcontent">
        <img src="./images/inthewild/21_rgb.jpg">
        </div>
    </div>
    <div class="twentytwenty-container">
        <div class="cmpcontent">
        <img src="./images/inthewild/21_rgb_blank.jpg">
        </div>
    </div>
</div>

<div class="twoitem">
    <div class="twentytwenty-container">
        <div class="cmpcontent">
        <img src="./images/inthewild/21_ours_depth.jpg">
        </div>
    </div>
    <div class="twentytwenty-container">
        <div class="cmpcontent">
        <img src="./images/inthewild/21_ours_normal.jpg">
        </div>
    </div>
</div>

<div class="twoitem">
    <div class="twentytwenty-container twentytwenty-container-depth-left">
        <div class="cmpcontent">
        <img src="./images/inthewild/21_ours_depth.jpg">
        </div>
        <div class="cmpcontent">
        <img src="./images/inthewild/21_marigold.jpg">
        </div>
    </div>
    <div class="twentytwenty-container twentytwenty-container-normal-left">
        <div class="cmpcontent">
        <img src="./images/inthewild/21_ours_normal.jpg">
        </div>
        <div class="cmpcontent">
        <img src="./images/inthewild/21_omnidata.jpg">
        </div>
    </div>
</div>

<div class="twoitem">
    <div class="twentytwenty-container twentytwenty-container-depth-right">
        <div class="cmpcontent">
        <img src="./images/inthewild/21_ours_depth.jpg">
        </div>
        <div class="cmpcontent">
        <img src="./images/inthewild/21_depthany.jpg">
        </div>
    </div>
    <div class="twentytwenty-container twentytwenty-container-normal-right">
        <div class="cmpcontent">
        <img src="./images/inthewild/21_ours_normal.jpg">
        </div>
        <div class="cmpcontent">
        <img src="./images/inthewild/21_dsine.jpg">
        </div>
    </div>
</div>