# Indian Census 2011 Data Analysis

This project analyzes the **Indian Census 2011** data to provide insights into demographic patterns, literacy rates, and gender distributions at both state and district levels. The analysis is performed using Python, and an interactive web application is built using Flask and Plotly.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)

---

## Overview
The project uses the Indian Census 2011 dataset to:
- Analyze population distribution and gender ratio.
- Calculate literacy rates for males and females across districts and states.
- Provide insights into various demographic trends through visualizations.
- Build an interactive web interface to make the data and insights easily accessible.

---

## Features
- **Data Cleaning & Analysis:**
  - Handle missing values and preprocess raw data.
  - Calculate gender and literacy-related metrics.

- **Interactive Visualizations:**
  - Bar charts for male and female literacy rates.
  - Population distribution by district and state.

- **Web Application:**
  - User-friendly interface built using Flask.
  - Interactive charts implemented with Plotly.

---

## Tech Stack
### Programming Languages & Tools:
- Python (Core Analysis)
- HTML, CSS (Frontend)

### Libraries & Frameworks:
- Flask
- Pandas
- Plotly
- Jupyter Notebook
- Gunicorn (for deployment)

---

## Dataset
The project uses the **Indian Census 2011** dataset, which includes:
- State and district-wise population data.
- Literacy statistics for males and females.
- Geospatial centroids for visualizations.

### Key Files:
1. `india-districts-census-2011.csv` - Main dataset.
2. `state wise centroids_2011.csv` - State geospatial data.
3. `district wise centroids.csv` - District geospatial data.

---

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/rahuls472/Indian-Census-2011-Data-Analysis.git
    cd Indian-Census-2011-Data-Analysis
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # For Linux/Mac
    myenv\Scripts\activate   # For Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask app:
    ```bash
    python app.py
    ```

5. Open the application in your browser at `http://127.0.0.1:5000`.

---

## Usage
The application allows users to:
- View literacy rates for males and females by district or state.
- Analyze demographic statistics through interactive charts.
- Explore population and gender ratio insights.

---

## Project Structure
```
Indian-Census-2011-Data-Analysis/
├── app.py                  # Main Flask application
├── datasetworks.py         # Helper functions for data processing
├── templates/              # HTML templates for the web interface
├── Modified data.csv       # Cleaned dataset
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation (this file)
```

---

## Future Improvements
- Add choropleth maps to visualize literacy rates geographically.
- Integrate more datasets to enhance analysis.
- Optimize the application for faster data processing.
- Deploy the app to a cloud platform (e.g., Heroku, AWS).

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## Author
**Rahul Singh**
- Email: rahulsingh07d@gmail.com
- GitHub: [rahuls472](https://github.com/rahuls472)

