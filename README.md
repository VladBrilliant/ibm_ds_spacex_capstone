# SpaceX Falcon 9 Data Science Project

This repository contains the full Capstone Project for analyzing and predicting SpaceX Falcon 9 first‑stage landing outcomes.

It includes:
- Data collection (API + Web Scraping)
- Data wrangling & cleaning
- SQL exploration (SQLite)
- Exploratory Data Analysis & Visualization
- Machine Learning prediction models
- Interactive Folium map
- Plotly Dash dashboard
- Engineering layer (DevOps / MLOps extensions)
- Final presentation materials

---

## Table of Contents
- [Project Structure](#project-structure)
- [Notebooks](#notebooks)
- [Data Files](#data-files)
- [Dashboard Screenshot](#dashboard-screenshot)
- [GIF Visuals](#gif-visuals)
- [Engineering Layer](#engineering-layer)
- [Environment](#environment)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Project Structure

```
spacex_project/
├── notebooks/
├── reports/
├── engineering/
│   ├── java/
│   ├── monitoring/
│   └── pipelines/
├── images/
└── README.md
```

---

## Notebooks

All notebooks are available inside  
**`spacex_project/notebooks/`**

### Data Acquisition
- jupyter-labs-spacex-data-collection-api.ipynb
- jupyter-labs-webscraping.ipynb

### Data Wrangling
- labs-jupyter-spacex-Data wrangling.ipynb

### SQL EDA
- jupyter-labs-eda-sql-coursera_sqllite.ipynb

### Visualization EDA
- edadataviz.ipynb

### Launch Site Mapping
- lab_jupyter_launch_site_location.ipynb

### Machine Learning Prediction
- SpaceX_Machine Learning Prediction_Part_5.ipynb

---

## Data Files

All data files are inside  
**`spacex_project/notebooks/`**

- dataset_part_1.csv
- dataset_part__3.csv
- spacex_web_scraped.csv
- features_one_hot.csv
- my_data1.db

> **Note:** Browsers may open CSV in a tab instead of downloading.  
> Use *Right‑click → Save link as…* and ensure the file ends with `.csv`.

---

## Dashboard Screenshot

![Dash Screenshot](spacex_project/images/spacex_dash.png)

---

## GIF Visuals

**Falcon 9 launch**

![Falcon 9 launch](spacex_project/images/tenor2.gif)

**Falcon 9 landing**

![Falcon 9 landing](spacex_project/images/tenor1.gif)

**Crash demo (classification contrast)**

![Crash](spacex_project/images/crash.gif)

---

## Engineering Layer

Extensions beyond the Coursera Capstone.

### engineering/java/
Utilities, experimental tools, future CLI concepts.

### engineering/monitoring/
Ideas for runtime monitoring of training workloads  
(e.g., preventing kernel crashes on weak hardware).

### engineering/pipelines/
Skeletons for ETL flows, data ingestion, automation.

---

## Environment

Install requirements:

```
pip install -r requirements.txt
```

---

## License

This project is licensed under the **Apache License 2.0**.  
See: LICENSE

---

## Acknowledgements

This repository is the Capstone Project for the  
**IBM Data Science Professional Certificate (Coursera)**.

The project is purely educational and **not affiliated with SpaceX**.  
SpaceX® is a trademark of Space Exploration Technologies Corp.
