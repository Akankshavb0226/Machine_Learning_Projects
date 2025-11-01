# Smart Crop Recommendation – Precision Agriculture (IoT + ML)
**Patent no:** 2023/02252 (South Africa)
## Overview
This project applies machine learning to precision agriculture, aiming to help farmers select optimal crops based on real-time soil and environmental data. By deploying sensors in fields to gather parameters such as rainfall, humidity, temperature, pH, and NPK nutrients, the solution enables data-driven decision support for crop selection, increasing productivity and yield.

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
1. Sensor data collected from field and transmitted to server-client architecture  
2. Data exploration, cleaning, and visualization  
3. Train/test split (typically 80/20)  
4. Model training, evaluation, and prediction using selected ML algorithms  
5. Crop suggestion output to end user

## Outcomes
- Enables farmers to make informed crop choices based on local field data  
- Demonstrates robust machine learning deployment with real-time IoT data  



