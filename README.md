# Wildlife Insight

[![Project Video Demo](https://img.youtube.com/vi/r7_4Xyb1DnI/0.jpg)](https://youtu.be/r7_4Xyb1DnI)

# Live Demo
[Live Demo](https://alu-mlopsummative-1.streamlit.app/)

**Wildlife Insight** is an interactive web app built using **Streamlit** that leverages **machine learning** to classify species and analyze wildlife data efficiently. The app is designed for wildlife conservation efforts, providing tools to predict species, visualize data, and update models with new data for better accuracy.

## Features

- **Model Prediction**: Users can make predictions based on species data, helping to classify and identify wildlife species.
- **Data Visualizations**: Interactive data exploration and visualizations to understand trends and insights from the dataset.
- **Upload & Retrain**: Users can upload new data and retrain the machine learning model to improve its performance.
- **Performance Testing**: Test the model’s scalability and response time by simulating a large number of requests using **Locust** for load testing.
  
## Getting Started

### Prerequisites

To run the app locally, make sure you have the following installed:

- Python 3.7 or higher
- Streamlit
- Locust (for performance testing)
  
You can install the required dependencies using pip:

```bash
pip install streamlit locust
```

### Running the App Locally

1. Clone the repository or download the code.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the app with the following command:

```bash
streamlit run app.py
```

This will open the app in your web browser.

### Performance Testing

To simulate a flood of requests and test the performance of the app, use **Locust**. Here's how to run the performance tests:

1. Navigate to the `locustfile.py` in the project directory.
2. Run the following command:

```bash
locust -f locustfile.py
```

This will start the Locust web interface where you can configure the number of users and requests per second to simulate load.

## App Layout

- **Home**: The landing page introduces the app, its purpose, and the available features.
- **Model Prediction**: Allows users to input data and get species predictions.
- **Data Visualizations**: Users can explore data using interactive charts and plots.
- **Upload & Retrain**: Provides a file upload option to update the model with new data.
- **Performance Testing**: A section dedicated to load testing, simulating multiple requests.

## LOCUST RESULTS

| Name       | Request Count | Failure Count | Median Response Time | Average Response Time | Min Response Time | Max Response Time | Average Content Size | Requests/s | Failures/s | 50%   | 66%   | 75%   | 80%   | 90%   | 95%   | 98%   | 99%   | 99.90% | 99.99% | 100%  |
|------------|---------------|---------------|----------------------|-----------------------|-------------------|-------------------|----------------------|------------|------------|-------|-------|-------|-------|-------|-------|-------|-------|--------|--------|-------|
| **/predict**   | 120           | 1             | 35000                | 33163.11743           | 2046.9266         | 68866.1414         | 117.0166667          | 1.448011648 | 0.012066764 | 35000 | 41000 | 43000 | 47000 | 63000 | 66000 | 67000 | 67000 | 69000  | 69000  | 69000 |
| **Aggregated** | 120           | 1             | 35000                | 33163.11743           | 2046.9266         | 68866.1414         | 117.0166667          | 1.448011648 | 0.012066764 | 35000 | 41000 | 43000 | 47000 | 63000 | 66000 | 67000 | 67000 | 69000  | 69000  | 69000 |


## Model API

You can access the Model API [here](https://mlop-wildlife-insight-1.onrender.com).
