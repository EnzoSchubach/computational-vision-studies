import cv2

img_path = "../intro_to_images/media/img.jpeg"

img = cv2.imread(img_path)
if img is None:
    print("image not found")
else:
    print("image successfully loaded")
    cv2.putText(img, "zib zib zib bla bla bla", (400, 400), cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 255, 120))
    cv2.imshow("Amolga", img)
    cv2.waitKey(0)