from cv2 import VideoCapture, imwrite

print("CAPTURING PHOTO SMILE :)")

cam = VideoCapture(0)
i = 0

while True:
    _, img = cam.read()
    imwrite("unknown.jpg", img)
    i += 1
    if i == 10:
        break

cam.release()

print("processing ...")

from face_recognition import load_image_file, compare_faces, face_encodings

unknown_image = load_image_file("unknown.jpg")
mark = load_image_file("markzuckerberg.jpg")

unknown_encode = face_encodings(unknown_image)[0]
mark_encode = face_encodings(mark)[0]

results = compare_faces([mark_encode], unknown_encode, 0.6)

if results[0] == True:

    print("I'M SURE THAT YOU ARE SHOWING A PHOTO OF MARK ZUCKERBERG OR YOUR FACES ARE SIMILAR. YOU AREN'T MARK ZUCKERBERG IT'S IMPOSSIBLE")

else:

    print("I DONT KNOW YOU")

input("exit ...")