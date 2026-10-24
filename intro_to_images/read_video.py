import cv2

video_path="media/video.mp4"
frame_rate = 60
rate_in_millis = int(1000/frame_rate)

video = cv2.VideoCapture(video_path)

while True:
    success, frame = video.read()
    if success:
        cv2.imshow("Pessoas andando uau", frame)
        cv2.waitKey(rate_in_millis)
    else:
        break