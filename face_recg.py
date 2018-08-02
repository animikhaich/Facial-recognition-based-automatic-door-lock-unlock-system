import face_recognition
import cv2
import way2sms
import TelegramAPI
import sqlite3 as sql

q = way2sms.Sms('PHONE_NUMBER', 'PASSWORD')


# Get a reference to webcam #0
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
animikh_image = face_recognition.load_image_file("./Assets/ani_2.jpg")
animikh_face_encoding = face_recognition.face_encodings(animikh_image)[0]

akhilesh_image = face_recognition.load_image_file("./Assets/akhil_1.jpg")
akhilesh_face_encoding = face_recognition.face_encodings(akhilesh_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    animikh_face_encoding,
    akhilesh_face_encoding
]

known_face_dict = {
    "Animikh": False,
    "Akhilesh": False
}

known_face_names = [name for name in known_face_dict.keys()]
face_names = []

for pic in range(5):
    # Grab a single frame of video
    ret, frame = video_capture.read()
    cv2.imwrite("./DataBase/test_pic_" + str(pic) + ".jpg", frame)

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        face_names.append(name)

    # # Display the results
    # for (top, right, bottom, left), name in zip(face_locations, face_names):
    #     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
    #     top *= 4
    #     right *= 4
    #     bottom *= 4
    #     left *= 4
    #
    #     # Draw a box around the face
    #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    #
    #     # Draw a label with a name below the face
    #     cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
    #     font = cv2.FONT_HERSHEY_DUPLEX
    #     cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imwrite("./DataBase/test_pic_" + str(pic) + ".jpg", frame)

print(face_names)

boolean_list = []
for name in face_names:
    if name in known_face_names:
        boolean_list.append(True)
    else:
        boolean_list.append(False)

dict_bool_list = [known_face_dict.get(name, False) for name in face_names]

if any(dict_bool_list):
    boolean = any(boolean_list)
else:
    boolean = all(boolean_list)

if len(face_names) < 1:
    print("Camera Blocked!")
    boolean = False

if boolean:
    q.send('ADMIN_PHONE_NUMBER', 'The following guests have been allowed inside: ' + ' '.join(set(face_names)))
    TelegramAPI.arduino_open_door()
else:
    q.send('ADMIN_PHONE_NUMBER', 'Unknown person wants to enter. Please Enquire telegram for further details')
    pass

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
q.logout()

