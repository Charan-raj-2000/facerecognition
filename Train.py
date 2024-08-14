import face_recognition
import os
import pickle

# Path to the directory containing images
images_directory = r"images"

# Lists to hold face encodings and names
known_face_encodings = []
known_face_names = []

# Iterate over all images in the directory
for filename in os.listdir(images_directory):
    # Construct full file path
    file_path = os.path.join(images_directory, filename)
    
    # Load the image file
    image = face_recognition.load_image_file(file_path)
    
    # Find face encodings in the image
    face_encodings = face_recognition.face_encodings(image)
    
    # Check if at least one face is found
    if len(face_encodings) > 0:
        # Assuming each image contains only one face
        encoding = face_encodings[0]
        
        # Extract name from filename (remove extension)
        name = os.path.splitext(filename)[0]
        
        # Save encoding and name
        known_face_encodings.append(encoding)
        known_face_names.append(name)
    else:
        print(f"No faces found in image {filename}")

# Save encodings and names to a file
with open('face_encodings.pkl', 'wb') as f:
    pickle.dump((known_face_encodings, known_face_names), f)

print("All images trained and encodings saved.")
