import cv2

img_path = "../intro_to_images/media/img.jpeg"

img = cv2.imread(img_path)
blur_img = cv2.GaussianBlur(img, (45, 45), 0)

if img is None:
    print("image not found")
else:
    print("image successfully loaded")
    cv2.imshow("original image", img)
    
    if blur_img is None: 
        print("couldnt blur the image")
    else:
        cv2.imshow("blurred image", blur_img)

    cv2.waitKey(0)