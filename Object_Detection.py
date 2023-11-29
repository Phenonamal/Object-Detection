import cv2 as cv
import numpy as np

#Get image and turns em into grayscale (for your needs you might not need this)
sample_img = cv.imread('sample.jpg', cv.IMREAD_UNCHANGED)  # Change to the name of your sample image
img_to_find = cv.imread('find_sample.jpg', cv.IMREAD_UNCHANGED) # Change to the name of the item you want to find in said image


result = cv.matchTemplate(sample_img,img_to_find, cv.TM_CCORR_NORMED) # Adjust last one to match your needs (use the documentation)

#get the best position that matches the template
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print("best match top left pos:%s" % str(max_loc))
print("best match confidence :%s" % max_val)

threshold = 0.4
loc = np.where( result >= threshold)
loc = list(zip(*loc[::-1]))


if loc:
    print("found")

    #get dimensions of the find_sample image
    match_w = img_to_find.shape[1]
    match_h = img_to_find.shape[0]
    line_colour = (0,255,0)
    line_type = cv.LINE_4

    #loops thru all the locations and draws the rectangle
    for location in loc:
        # determine the box positions
        top_left = location
        bottom_right = (top_left[0] + match_h, top_left[1] + match_w)
        # draw the box
        cv.rectangle(sample_img, top_left, bottom_right, line_colour, line_type)

    cv.imshow("Result", sample_img)
    cv.waitKey()
    cv.imwrite("result.jpg", sample_img)
else:   
    print("not found")