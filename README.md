# Captcha Recognition Project
This repository contains the code and resources for a project on captcha recognition. The project involves retrieving captcha images, preprocessing the data, training a model, and preparing the output for submission on Submitty.

**File Retrieval** 

To start the project, the first step is to download the captcha images. There are two methods for retrieval: to a local laptop and to a Raspberry Pi.

**Retrieval to Local Laptop**

To download the 2000 captcha images to a local laptop, a VPN connection to the school network is required. Access the provided link through the VPN to obtain a text file containing a list of filenames for the captchas. Then, download the images using the provided link and specify the filename for each captcha. The code reads the file containing the list of image names and stores the transferred images in a target directory locally.

**Retrieval to Raspberry Pi**
For downloading the picture data to a Raspberry Pi, a similar principle applies. However, a proxy server needs to be added to support the Raspberry Pi's access to external websites. The retrieval code needs to be uploaded from the local laptop to the Raspberry Pi, and the download process is executed on the Raspberry Pi using the provided commands. This process requires network access and may take around 20 minutes to download all 2000 images.

**Preparation / Preprocessing**

Before proceeding with the project, it is recommended to create a virtual environment using the conda command to ensure a stable running environment and avoid version conflicts. Install the required Python packages, including captcha, TensorFlow (or TensorFlow Lite for Raspberry Pi), OpenCV, and others. These packages provide support for various tasks throughout the project.

**Training Set and Validation Set**

Observing the 2000 captchas, it is found that the length of the digits in the captchas is not fixed, and they contain special characters in addition to numbers and letters. To handle this, the data generation part needs to be adjusted. The solution is to add spaces as a normal character and additional characters to the symbol.txt file, randomly generating captcha images with 1-6 digits, and filling any remaining digits with spaces.
Additionally, to address issues with file naming and special characters, the file name is stored as a number, and the contents of the captcha are placed in a CSV file along with the number. This ensures compatibility across different operating systems.
Generating the training set and validation set will depend on the number of images required. Typically, generating a training set of 70,000 captchas takes around 5 minutes or more. The validation set is usually smaller and takes less time.

**Repository Structure**

•	code/: Contains the code for retrieval, preprocessing, training, and solution submission.
•	data/: Includes the generated captcha images and associated files.
•	models/: Contains the trained model or model checkpoints.
•	README.md: This file providing an overview of the project.

**Requirements**

•	Python 3.x
•	Required Python packages (specified in the code)

**Usage**

1.	Clone the repository
2.	Install the required dependencies (specified in the code).
3.	Follow the instructions in Regenerate response
