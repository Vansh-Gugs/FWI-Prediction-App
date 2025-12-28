# Fire Weather Index (FWI) Prediction Web App

A Machine Learning web application built using **Flask** that predicts the Fire Weather Index (FWI) based on environmental features.

---

## Project Overview

This project demonstrates an **end-to-end ML pipeline** including:

- **Exploratory Data Analysis (EDA)** to understand feature distributions, correlations, and outliers.
- **Data Cleaning & Feature Engineering** to prepare the dataset for modeling.
- **Model Training & Selection**: Multiple regression models were trained (Linear Regression, Ridge, Lasso, Random Forest, etc.), and the best model was chosen based on **accuracy and cross-validation**.
- **Model Deployment**: The chosen model (Ridge Regression) is deployed using Flask as a web application.
- **Interactive Web Interface**: Users can input environmental parameters to get a real-time FWI prediction.

---

## Tech Stack

- Python
- Flask
- Pandas, NumPy
- Scikit-learn
- HTML/CSS for frontend

---

## How to Run Locally
1. Clone the repo
2. Create virtual environment
3. Install dependencies
4. Run `python application.py`

## Model
Ridge Regression model trained on FWI Algerian Forest Fire dataset.
