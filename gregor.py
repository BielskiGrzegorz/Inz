from deepface import DeepFace
import cv2

import threading

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

face_emotion = "DUPA"


def check_emotion(frame):
    global face_emotion
    cv2.imwrite(f"frame.jpg", frame)
    try:
        objs = DeepFace.analyze(img_path = "frame.jpg", actions = ['emotion'])
    except ValueError:
        return
    emotions = objs[0]["emotion"]

    max_key = max(emotions, key=emotions.get)
    print(emotions)

    print(max(emotions))
    face_emotion = max_key




while True:
    ret, frame = cap.read()

    
    cv2.putText(frame, face_emotion, (20,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    key = cv2.waitKey(1)
    if key == ord("q"):
        if ret:
            try:
                threading.Thread(target=check_emotion, args=(frame.copy(),)).start()
                
            except ValueError:
                pass

    
    if key == ord("a"):
        break

    cv2.imshow("video", frame)

cv2.destroyAllWindows()