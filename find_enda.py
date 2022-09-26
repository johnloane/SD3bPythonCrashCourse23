import face_recognition
import numpy as np
from PIL import Image, ImageDraw

# Load in the picture of Enda
endas_image = face_recognition.load_image_file("enda.png")
enda_encoding = face_recognition.face_encodings(endas_image)[0]

# Load the image of unknown faces
unknown_image = face_recognition.load_image_file("dkit_erasmus.png")

# Find all faces and face encodings
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Create Pillow ImageDraw Draw so that we can draw on an image
pil_image = Image.fromarray(unknown_image)
draw = ImageDraw.Draw(pil_image)

# Loop through each face in the unknown image and see how closely it matches Enda's face
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces([enda_encoding], face_encoding)
    face_distances = face_recognition.face_distance([enda_encoding], face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        # draw a rectangle around the faces
        draw.rectangle(((left-20, top -20), (right+20, bottom+20)), outline=(0, 255, 0), width=5)
del draw
pil_image.show()
