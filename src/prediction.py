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


# Function to evaluate the model
def evaluate_model(model, X_test_scaled, y_test):
    # Predict probabilities and classes
    predictions_proba = model.predict(X_test_scaled)
    predictions = np.argmax(predictions_proba, axis=1)

    # Calculate metrics
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, average='weighted')
    recall = recall_score(y_test, predictions, average='weighted')
    f1 = f1_score(y_test, predictions, average='weighted')

    # Evaluate loss
    loss, _ = model.evaluate(X_test_scaled, y_test, verbose=0)

    # Print the scores
    print(f"Evaluation Metrics:")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Loss: {loss:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")

    # Visualize the metrics
    metrics = {'Accuracy': accuracy, 'Loss': loss, 'Precision': precision, 'Recall': recall, 'F1 Score': f1}
    plt.figure(figsize=(10, 6))
    plt.bar(metrics.keys(), metrics.values(), color='skyblue')
    plt.title("Model Evaluation Metrics")
    plt.ylabel("Score")
    plt.show()

    return metrics
