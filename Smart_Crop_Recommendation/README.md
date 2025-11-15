# Smart Crop Recommendation – Precision Agriculture (IoT + ML)
**Patent no:** 2023/02252 (South Africa)
## Overview
This project applies machine learning to precision agriculture, aiming to help farmers select optimal crops based on real-time soil and environmental data. By deploying sensors in fields to gather parameters such as rainfall, humidity, temperature, pH, and NPK nutrients, the solution enables data-driven decision support for crop selection, increasing productivity and yield.

### Hardware at a Glance
This is the hardware setup used.

![Hardware Setup](https://github.com/Akankshavb0226/Machine_Learning_Projects/blob/4df6c8de86fc24259a9e3c2f2527889bbb9377b8/Smart_Crop_Recommendation/Images/Hardware%20Setup.png?raw=true)

## Features
- Collects soil and environmental data using sensors (rainfall, humidity, temperature, pH, NPK)
- Integrates microcontroller hardware for real-time data transmission
- Processes and analyzes sensor data with Python-based machine learning models
- Implements algorithms including XGBoost, Artificial Neural Network, and k-Nearest Neighbor for crop recommendation
- Achieves up to 99% model accuracy, minimizing crop failure and maximizing efficiency

## Tools & Hardware Used

### Hardware
- NodeMCU ESP32 microcontroller
- Rainfall sensor
- DHT11 humidity and temperature sensor
- pH sensor
- NPK nutrient sensor
- Display unit
- Laptop with Intel Core-i7
- Raspberry Pi running Raspbian OS

### Software & Libraries
- Python programming language
- Jupyter Notebook for development and analysis
- Visual Studio for IDE tasks
- Data science and machine learning libraries: Pandas, Numpy, Scikit-learn, TensorFlow, Keras

## Dataset
The system uses multi-source datasets combining field sensor values and publicly available agricultural records. The dataset includes measurements of rainfall, humidity, temperature, pH, NPK concentration, and associated crop labels.

## Methodology
The following block diagram methodology describes the complete flow of the Smart Crop Recommendation System, from data processing to final prediction.

![Methodology](https://github.com/Akankshavb0226/Machine_Learning_Projects/blob/42466e1027b5abb4ee1d2937b90f07b77e190d1f/Smart_Crop_Recommendation/Images/Methodology.png)
1. **Data Collection**  
   A large volume of agricultural and sensor data is collected and fed into the system.

2. **Data Exploration**  
   The system performs exploratory analysis on every feature and parameter.

3. **Data Splitting**  
   The processed dataset is divided into training and testing subsets.

4. **Model Training**  
   The training portion of the data is used to train machine learning models for accurate prediction.

5. **Model Evaluation**  
   Evaluation metrics are used to measure how well the model has learned from the training data.

6. **Accuracy Measurement**  
   Model accuracy is calculated to verify efficiency and identify improvements.

7. **Prediction Phase**  
   The model performs predictions to validate how effectively it generalizes to new data.

8. **Result Generation**  
   Based on predictions and evaluations, the system produces the final recommended crop.

### IoT-Based Live Data Flow

9. **Sensor Measurement**  
   Sensors (NPK, pH, temperature, humidity, rainfall) measure real-time environmental parameters.

10. **Client System Input**  
   The measured parameters are entered into the IoT client system (ESP32 or dashboard).

11. **Server Processing**  
   The backend server receives the sensor data, processes it, and runs the ML model.

12. **Result Delivery**  
   The processed output (recommended crop) is sent back to the client system for user display.

   ![Expected Output](https://github.com/Akankshavb0226/Machine_Learning_Projects/blob/4df6c8de86fc24259a9e3c2f2527889bbb9377b8/Smart_Crop_Recommendation/Images/Expected%20output.png)

## Outcomes
- Enables farmers to make informed crop choices based on local field data  
- Demonstrates robust machine learning deployment with real-time IoT data  



