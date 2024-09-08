import face_recognition
import cv2

# Load known faces and their encodings
known_face_encodings = []
known_face_names = []

# Example: Add known faces
# Load an image file containing the face to recognize, then encode it
image_of_person1 = face_recognition.load_image_file("Dheeraj.jpg")
image_of_person2 = face_recognition.load_image_file("Lucky.jpg")
image_of_person3 = face_recognition.load_image_file("Madhuri.jpg")
person1_face_encoding = face_recognition.face_encodings(image_of_person1)[0]
person2_face_encoding = face_recognition.face_encodings(image_of_person2)[0]
person3_face_encoding = face_recognition.face_encodings(image_of_person3)[0]
# Add the face encoding and the name
known_face_encodings.append(person1_face_encoding)
known_face_encodings.append(person2_face_encoding)
known_face_encodings.append(person3_face_encoding)
known_face_names.append("Dheeraj Kumar")
known_face_names.append("Lucky")
known_face_names.append("Madhuri")


# Initialize some variables
face_locations = []
face_encodings = []
face_names = []

# Start the video capture
video_capture = cv2.VideoCapture(0)  # 0 for default camera

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    
    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    
    face_names = []
    for face_encoding in face_encodings:
        # Compare faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Check if a match was found
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        face_names.append(name)
    
    # Display results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        
        # Draw a label with the name below the face
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
    
    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
video_capture.release()
cv2.destroyAllWindows()
