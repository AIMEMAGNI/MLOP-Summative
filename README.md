# Wildlife Insight

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

