import cv2

img_path = "media/img.jpeg"

img = cv2.imread(img_path)
if img is None:
    print("image not found")
else:
    print("image successfully loaded")
    cv2.imshow("Amolga", img)
    cv2.waitKey(0)