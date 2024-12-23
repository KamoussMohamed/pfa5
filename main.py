import cv2
from simple_facerec import SimpleFacerec
import os

sfr = SimpleFacerec()
sfr.load_encoding_images("images/")


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erreur : Impossible d'accéder à la caméra.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Erreur : Impossible de lire le flux vidéo.")
        break

    face_locations, face_names = sfr.detect_known_faces(frame)

    for face_loc, name in zip(face_locations, face_names):
        top, right, bottom, left = face_loc
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:  # Touche ESC pour quitter
        if os.path.exists("presence.json"):
            os.remove("presence.json")
        break


    

cap.release()
cv2.destroyAllWindows()