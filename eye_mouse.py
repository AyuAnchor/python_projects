import cv2
import mediapipe as mp

camera = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh()
while 1:
    _, frame = camera.read()
    frame_h, frame_w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmarks_points = output.multi_face_landmarks
    if landmarks_points:
        landmarks = landmarks_points[0].landmark
        for landmark in landmarks:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            print(x, y)
    cv2.imshow("Eye - MOUSE", frame)
    cv2.waitKey(1)