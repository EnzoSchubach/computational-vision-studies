import cv2

img_path = "../intro_to_images/media/img.jpeg"

img = cv2.imread(img_path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

if img is None:
    print("image not found")
else:
    print("image successfully loaded")
    cv2.imshow("original image", img)
    
    if gray_img is None: 
        print("couldnt convert to gray scale")
    else:
        cv2.imshow("grayscale image", gray_img)

    cv2.waitKey(0)