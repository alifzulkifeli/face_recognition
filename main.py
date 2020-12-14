import cv2
import face_recognition


def snap():
    """
    snap and save image
    """
    cam = cv2.VideoCapture(0)
    retval, frame = cam.read()
    if retval != True:
        raise ValueError("Can't read frame")

    cv2.imwrite("data/new.png", frame)


tmp = face_recognition.face_encodings(
    face_recognition.load_image_file("data/tony.jpg")
)[0]
tmp2 = face_recognition.face_encodings(
    face_recognition.load_image_file("data/saved.png")
)[0]
known_face_encodings = [tmp, tmp2]
known_face_names = ["aliff", "tony"]


while True:
    snap()

    unknown_image = face_recognition.load_image_file("data/new.png")

    if face_recognition.face_encodings(unknown_image) != []:

        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
        results = face_recognition.compare_faces(known_face_encodings, unknown_encoding)
        if results:
            print("ada")
            print(results)
            if not any(results):

                print("nonono")
                known_face_encodings.append(unknown_encoding)
                x = input("new entry: ")

    else:
        print("no human")
