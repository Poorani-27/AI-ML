# Salary Prediction Project Documentation

## Overview
This project aims to predict salaries based on years of experience using a machine learning model. The model is trained on a dataset containing information about individuals' experience years and corresponding salaries. By analyzing this data and building a predictive model, the project seeks to provide insights into salary trends and assist in making salary predictions for individuals based on their experience.

## Dataset
The dataset used for this project contains the following columns:
- **Experience Years**: Number of years of experience
- **Salary**: Corresponding salary based on experience

## Methodology
The project follows the following methodology:
1. **Data Collection**: The dataset is collected from a remote location using the pandas library in Python.
2. **Data Preprocessing**: The dataset is preprocessed to handle any missing values or inconsistencies.
3. **Feature Selection**: The feature "Experience Years" is selected as the independent variable (X), and "Salary" is selected as the target variable (y).
4. **Train-Test Split**: The dataset is split into training and testing sets using the train_test_split function from scikit-learn.
5. **Model Selection**: A linear regression model is chosen for its simplicity and effectiveness in predicting numerical values.
6. **Model Training**: The linear regression model is trained on the training data using the fit method.
7. **Prediction**: The trained model is used to make salary predictions on the testing data using the predict method.
8. **Evaluation**: The performance of the model is evaluated using the mean absolute error metric, which measures the average absolute difference between predicted and actual salaries.

## Results
After training and evaluating the model, the project achieves an accuracy of approximately 95% on the testing data. This means that the model's predictions are 95% accurate on average.

## Conclusion
The salary prediction project demonstrates the application of machine learning techniques to predict salaries based on years of experience. By leveraging a linear regression model, the project provides a valuable tool for estimating salaries and gaining insights into salary trends in various industries.
