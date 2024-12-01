import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import os
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# Function for preprocessing data
def preprocess_data(file_path, sample_frac=0.4, random_state=42):
    # Load the dataset
    df = pd.read_csv(file_path)
    df = df.sample(frac=sample_frac, random_state=random_state)
    
    # Drop unnecessary columns
    df = df.drop(['internalTaxonId', 'scientificName'], axis=1)
    
    # Encode categorical features
    label_encoders = {}
    for col in ['speciesName', 'systems', 'scopes', 'Category']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    # Separate features and target
    X = df.drop('Category', axis=1)
    y = df['Category']

    # Split data: 80% train, 20% test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)

    # Scale the data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Save the scaler and label encoders for future use
    joblib.dump(scaler, "scaler.pkl")
    joblib.dump(label_encoders, "label_encoders.pkl")
    
    return X_train_scaled, X_test_scaled, y_train, y_test, df, label_encoders
