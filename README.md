# Normal X-bar Control Chart Dashboard

## Introduction
This project uses Python Dash to build a dashboard for visualizing data. It includes features for uploading a CSV file, displaying the CSV file in a table, showing an X-bar control chart, dynamically inputting data, and downloading the data as a CSV file.

## About the Data
The data used in this project is experimental data that researchers and analysts input periodically.

## Getting Started

### Prerequisites
Make sure you have the following packages installed:
- dash
- plotly
- pandas
- openpyxl
- tkinter

You can install them using pip:
    ```sh
    pip install dash plotly pandas openpyxl
    ```

## Running the Application
1. Open a terminal and type:
   ```sh
   python app.py
   ```
2. Open a web browser and navigate to:
    ```sh
    http://127.0.0.1:8050/
    ```
3. Click the "Upload" button to upload a CSV file.
4. The data will be displayed in a table and an X-bar control chart.
5. Click the "Download" button to download the data in CSV format.

## Features
* Upload CSV File: Allows users to upload a CSV file.
* Display Data: Shows the uploaded data in a table.
* X-bar Control Chart: Visualizes the data using an X-bar control chart.
* Download Data: Allows users to download the data as a CSV file.

## File Structure
```plaintext
.
├── app.py
├── README.md

```

## License
This project is licensed under the MIT License.