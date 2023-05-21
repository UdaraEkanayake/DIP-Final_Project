# Vehicle Damage Detection and Assessment System

This project aims to develop an automated system for detecting and assessing vehicle damage using image processing techniques and deep learning algorithms. The system analyzes images of damaged vehicles, identifies the type and extent of damage, and provides a preliminary estimate for repair costs. It can be used in insurance claims processing, vehicle maintenance, and other related applications.

## UI Design in upload.html & result.html

<img width="1440" alt="Upload" src="https://github.com/udaraekanayake96/DIP-Final_Project/assets/113182571/43bb8367-8f9b-4209-9e27-de461c8acddd">

<img width="1440" alt="Upload" src="https://github.com/udaraekanayake96/DIP-Final_Project/assets/113182571/9361d545-dd32-4450-b5fe-77d950c0575d">

## Project Overview
The project consists of the following components:

1. Data Collection and Preprocessing: The system requires a dataset of vehicle images with labeled damage information. The images are preprocessed by resizing, normalization, and data augmentation techniques to prepare them for the deep learning model.

2. Damage Detection Model: A Convolutional Neural Network (CNN) model is implemented to detect and localize vehicle damage. The model is trained using the preprocessed dataset and evaluated using appropriate metrics.

3. Damage Classification and Assessment: The damage detection model is extended to classify the type of damage (e.g., scratches, dents, broken glass) and assess the extent of the damage (e.g., minor, moderate, severe). The extended model is trained and evaluated using the dataset.

4. Repair Cost Estimation: A regression model or a rule-based system is developed to estimate repair costs based on the type and extent of the damage. Historical repair cost data or industry-standard repair cost guidelines can be used for this purpose.

5. User Interface: A user-friendly interface is created to allow users to upload vehicle images, display the detected     damage, and provide an estimate for repair costs. The interface can be developed as a web application, mobile application, or desktop software.

## Project Setup and Usage

To set up and use the project, follow these steps:

1. Clone the repository from GitHub: [repository URL]

2. Install the required dependencies by running pip install -r requirements.txt.

3. Run the application by executing the main script: python main.py.

4. Access the user interface by opening the provided URL in your web browser.

## Project Structure

- app/
  - images/
    - (images are here)
- templates/
  - upload.html
  - result.html
- static/
  - css/
     - style.css
  - js/
     - script.js
- app.py
- preprocess.py
- train_damage_classification.py
- train_damage_detection.py
- train_repair_cost_estimation.py
- venv
  -resource packages
- README.md

