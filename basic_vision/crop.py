import cv2

img_path = "../intro_to_images/media/img.jpeg"

img = cv2.imread(img_path)

#always stars with the y value y1:y2, x1:x2
cropped_img = img[430:1600, 450:1000]

if img is None:
    print("image not found")
else:
    print("image successfully loaded")
    cv2.imshow("original image", img)
    
    if cropped_img is None: 
        print("couldnt blur the image")
    else:
        cv2.imshow("blurred image", cropped_img)

    cv2.waitKey(0)