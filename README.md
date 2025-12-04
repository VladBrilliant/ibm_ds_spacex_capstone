# SpaceX Falcon 9 Data Science Project

<p align="center">
  <img src="https://github.com/VladBrilliant/ibm_ds_spacex_capstone/blob/main/spacex_project/images/tenor2.gif?raw=1" width="48%">
  <img src="https://github.com/VladBrilliant/ibm_ds_spacex_capstone/blob/main/spacex_project/images/tenor1.gif?raw=1" width="48%">
</p>

This repository contains the complete SpaceX Falcon 9 analysis, visualizations, and machine learning workflow for the Falcon 9 first stage landing prediction capstone.

---

## Table of Contents
- [Project Structure](#project-structure)
- [Notebooks](#notebooks)
- [Dashboard Screenshot](#dashboard-screenshot)
- [Data Files](#data-files)
- [Reports](#reports)
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
├── images/              # GIF animations used in README
└── README.md
```

---

## Notebooks

### Data Acquisition
- [jupyter-labs-spacex-data-collection-api.ipynb](spacex_project/notebooks/jupyter-labs-spacex-data-collection-api.ipynb)
- [jupyter-labs-webscraping.ipynb](spacex_project/notebooks/jupyter-labs-webscraping.ipynb)

### Data Wrangling & Preprocessing
- [labs-jupyter-spacex-Data wrangling.ipynb](spacex_project/notebooks/labs-jupyter-spacex-Data%20wrangling.ipynb)

### SQL EDA
- [jupyter-labs-eda-sql-coursera_sqllite.ipynb](spacex_project/notebooks/jupyter-labs-eda-sql-coursera_sqllite.ipynb)

### Visualization EDA
- [edadataviz.ipynb](spacex_project/notebooks/edadataviz.ipynb)

### Launch Site Mapping
- [lab_jupyter_launch_site_location.ipynb](spacex_project/notebooks/lab_jupyter_launch_site_location.ipynb)

### Machine Learning Prediction
- [SpaceX_Machine Learning Prediction_Part_5.ipynb](spacex_project/notebooks/SpaceX_Machine%20Learning%20Prediction_Part_5.ipynb)

---

## Dashboard Screenshot

<p align="center">
  <img src="spacex_project/images/spacex_dash.png" width="700">
</p>

---

## Data Files

Located under `spacex_project/notebooks/`:

- [dataset_part_1.csv](spacex_project/notebooks/dataset_part_1.csv)
- [dataset_part__3.csv](spacex_project/notebooks/dataset_part__3.csv)
- [spacex_web_scraped.csv](spacex_project/notebooks/spacex_web_scraped.csv)
- [features_one_hot.csv](spacex_project/notebooks/features_one_hot.csv)
- [my_data1.db](spacex_project/notebooks/my_data1.db)

---

## Reports

Stored in `spacex_project/reports/`:

- ds-capstone-template-coursera.pptx
- spacex_capstone_presentation.pdf (if added)

---

## Engineering Layer

### engineering/java/
Java utilities and helper scripts (future extensions).

### engineering/monitoring/
Concepts and drafts for monitoring system load and preventing crashes during model training on limited hardware.

### engineering/pipelines/
Early DevOps/MLOps pipeline ideas: data ingestion, ETL, and notebook-to-production transformations.

---

## Environment

Install dependencies:

```
pip install -r requirements.txt
```

---

## License

This project is licensed under the **Apache License 2.0** — see LICENSE.

---

## Acknowledgements

This repository is the Capstone Project for the **IBM Data Science Professional Certificate** on Coursera.

It is an educational project and is **not affiliated with SpaceX**.  
SpaceX® is a trademark of Space Exploration Technologies Corp.

---

<p align="center">
  <img src="spacex_project/images/crash.gif" width="450">
</p>

<p align="center"><i>"The goal was simple: predict this outcome."</i></p>
