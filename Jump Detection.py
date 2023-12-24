import cv2
import mediapipe as mp
import pyautogui

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_frame)

    if results.pose_landmarks:
        y_position = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * frame.shape[0])
        
        if y_position < 500 and var == 1:
            pyautogui.press('space')
            var = 0

        if y_position > 500:
            var = 1

        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.imshow('Jump Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


