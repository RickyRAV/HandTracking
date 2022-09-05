import time
import mediapipe as mp
import cv2
vid = cv2.VideoCapture(0)
prevFrameTime = 0
newFrameTime = 0
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
fin = ''
val = 0
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.2, max_num_hands=5) as hands:
    while True:
        ret, frame = vid.read()
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        print(results.multi_hand_landmarks)
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS, mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=5, circle_radius=2))
                if hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y > hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y:
                    val1 = 0
                else:
                    val1 = 1
                    fin += 'Index '
                if hand.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y > hand.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y:
                    val2 = 0
                else:
                    val2 = 1
                    fin += 'Middle '
                if hand.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y > hand.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y:
                    val3 = 0
                else:
                    val3 = 1
                    fin += 'Ring '
                if hand.landmark[mp_hands.HandLandmark.PINKY_TIP].y > hand.landmark[mp_hands.HandLandmark.PINKY_DIP].y:
                    val4 = 0
                else:
                    val4 = 1
                    fin += 'Pinky '
                if hand.landmark[mp_hands.HandLandmark.THUMB_TIP].y > hand.landmark[mp_hands.HandLandmark.THUMB_IP].y:
                    val5 = 0
                else:
                    val5 = 1
                    fin += 'Thumb '
                val = val1+val3+val2+val4+val5
        gray = frame
        gray = cv2.resize(gray, (1024, 700))
        font = cv2.FONT_HERSHEY_SIMPLEX
        newFrameTime = time.time()
        fps = 1/(newFrameTime-prevFrameTime)
        prevFrameTime = newFrameTime
        fps = int(fps)
        fps = 'FPS:'+str(fps)
        final = 'Shown fingers:'+str(val)
        cv2.putText(gray, fps, (7, 40), font, 1.3, (165, 100, 100), 2, cv2.LINE_AA)
        cv2.putText(gray, final, (690, 688), font, 1.3, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Hand Tracking', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
vid.release()
cv2.destroyAllWindows()
