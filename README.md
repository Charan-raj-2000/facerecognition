Here's a `README.md` file with clear instructions for your GitHub repository:

---

# Face Recognition System

This repository contains two Python scripts: `Train.py` for training a face recognition model using images stored in a directory, and `Recog.py` for real-time face recognition using a webcam.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Training the Model](#training-the-model)
- [Running the Face Recognition](#running-the-face-recognition)
- [License](#license)

## Prerequisites

Before running the scripts, ensure you have the following installed:

1. **Python 3.11**: The scripts are compatible with Python version 3.11.
2. **CMake**: Download and install CMake from the [CMake official website](https://cmake.org/download/).
3. **dlib 19.24.1**: Install the appropriate dlib wheel file for Python 3.11 from a GitHub repository or other sources.

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/Charan-raj-2000/facerecognition.git
cd facerecognition
```

### Installing Dependencies

Use pip to install the required Python packages:

```bash
pip install -r requirements.txt
```

**Dependencies:**

- `click==8.1.7`
- `cmake==3.30.2`
- `colorama==0.4.6`
- `cv2-tools==2.4.0`
- `face-recognition==1.3.0`
- `face_recognition_models==0.3.0`
- `ImageHash==4.3.1`
- `numpy==1.23.5`
- `opencv-python==4.10.0.84`
- `pillow==10.4.0`
- `python-constraint==1.4.0`
- `PyWavelets==1.7.0`
- `scipy==1.14.0`

## Usage

### Training the Model

1. Place your images in the `images` directory. Each image should contain a single face, and the filename should represent the name of the person (e.g., `john_doe.jpg`).

2. Run the `Train.py` script to encode the faces and save the encodings:

   ```bash
   python Train.py
   ```

   This script will generate a `face_encodings.pkl` file containing the face encodings and names.

### Running the Face Recognition

1. Ensure your webcam is connected and functional.

2. Run the `Recog.py` script to start real-time face recognition:

   ```bash
   python Recog.py
   ```

3. The webcam feed will open, and recognized faces will be highlighted with a rectangle, displaying the name of the person. Press `q` to exit the feed.



---
