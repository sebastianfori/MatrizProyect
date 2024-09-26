Here's the README.md file formatted in Markdown:

markdown
Copiar código
# Image Processor Project

This project allows users to load, crop, adjust contrast, convert to grayscale, transpose, and perform other image processing operations using Python. The project is modular, adhering to SOLID principles and organized with separate files for clarity.

## Project Structure

```plaintext
ImageProcessorProject/
│
├── main.py                 # Main script to process images
├── image_processor.py       # Class with image processing methods
├── requirements.txt         # Dependencies required for the project
└── README.md                # Instructions for setting up and running the project
```
## Features

Load an image from a file path.
Crop images to a square format.
Display images in different states (cropped, grayscale, etc.).
Convert images to grayscale.
Transpose the image matrix.
Adjust image contrast by a given factor.
Calculate the negative of an image.
## Prerequisites
Before running this project, you need to have Python installed. The project uses Python 3.x.

Setup Instructions
Clone or download the project: If you're using Git, clone the repository:

'''bash
git clone <repository-url>
'''
Or download the project manually as a ZIP and unzip it.

Navigate to the project directory:

'''bash

cd ImageProcessorProject
Install the dependencies:

Make sure you have pip installed, then run:

'''bash

pip install -r requirements.txt
'''
Update image paths:

Open main.py and update the paths for image_path1 and image_path2 with the actual paths to your images:


image_path1 = 'path/to/your/image1.jpg'  # Update this path
image_path2 = 'path/to/your/image2.jpg'  # Update this path
Run the project:

Execute the main script:

'''bash

python main.py
'''
Usage
The program will load the specified images, perform various processing tasks, and display the results in different windows.
You can press any key to close the image windows after viewing them.