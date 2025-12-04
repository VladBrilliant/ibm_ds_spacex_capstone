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
- [Data Files](#data-files)
- [Reports](#reports)
- [Engineering Layer](#engineering-layer)
- [Environment](#environment)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Project Structure

```text
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
- [jupyter-labs-spacex-data-collection-api.ipynb](https://github.com/VladBrilliant/ibm_ds_spacex_capstone/blob/main/spacex_project/notebooks/jupyter-labs-spacex-data-collection-api.ipynb)
- [jupyter-labs-webscraping.ipynb](https://github.com/VladBrilliant/ibm_ds_spacex_capstone/blob/main/spacex_project/notebooks/jupyter-labs-webscraping.ipynb)

### Data Wrangling & Preprocessing
- [labs-jupyter-spacex-Data wrangling.ipynb](https://github.com/VladBrilliant/ibm_ds_spacex_capstone/blob/main/spacex_project/notebooks/labs-jupyter-spacex-Data%20wrangling.ipynb)

### SQL EDA
- [jupyter-labs-eda-sql-coursera_sqllite.ipynb](https://github.com/VladBrilliant/ibm_ds_spacex_capstone/blob/main/spacex_project/notebooks/jupyter-labs-eda-sql-coursera_sqllite.ipynb)

### Visualization EDA
- [edadataviz.ipynb](https://github.com/VladBrilliant/ibm_ds_spacex_capstone/blob/main/spacex_project/notebooks/edadataviz.ipynb)

### Launch Site Mapping
- [lab_jupyter_launch_site_location.ipynb](https://github.com/VladBrilliant/ibm_ds_spacex_capstone/blob/main/spacex_project/notebooks/lab_jupyter_launch_site_location.ipynb)

### Machine Learning Prediction
- [SpaceX_Machine Learning Prediction_Part_5.ipynb](https://github.com/VladBrilliant/ibm_ds_spacex_capstone/blob/main/spacex_project/notebooks/SpaceX_Machine%20Learning%20Prediction_Part_5.ipynb)

---

## Data Files

Located under `spacex_project/notebooks/`:

- [dataset_part_1.csv](https://github.com/VladBrilliant/ibm_ds_spacex_capstone/raw/main/spacex_project/notebooks/dataset_part_1.csv)
- [dataset_part__3.csv](https://github.com/VladBrilliant/ibm_ds_spacex_capstone/raw/main/spacex_project/notebooks/dataset_part__3.csv)
- [spacex_web_scraped.csv](https://github.com/VladBrilliant/ibm_ds_spacex_capstone/raw/main/spacex_project/notebooks/spacex_web_scraped.csv)
- [features_one_hot.csv](https://github.com/VladBrilliant/ibm_ds_spacex_capstone/raw/main/spacex_project/notebooks/features_one_hot.csv)
- [my_data1.db](https://github.com/VladBrilliant/ibm_ds_spacex_capstone/raw/main/spacex_project/notebooks/my_data1.db)

---

## Reports

Stored in `spacex_project/reports/`:

- [ds-capstone-template-coursera.pptx](https://github.com/VladBrilliant/ibm_ds_spacex_capstone/raw/main/spacex_project/reports/ds-capstone-template-coursera.pptx)
- [spacex_capstone_presentation.pdf](https://github.com/VladBrilliant/ibm_ds_spacex_capstone/raw/main/spacex_project/reports/spacex_capstone_presentation.pdf)

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

```bash
pip install -r requirements.txt
```

All required Python packages are listed in `requirements.txt` at the repository root.

---

## License

This project is licensed under the **Apache License 2.0** — see [LICENSE](LICENSE).

---

## Acknowledgements

This repository is the Capstone Project for the **IBM Data Science Professional Certificate** on Coursera.

It is an educational project and is **not affiliated with SpaceX**.  
SpaceX® is a trademark of Space Exploration Technologies Corp.

---

![Falcon 9 crash](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/crash.gif)

<p align="center"><i>"The goal was simple: predict this outcome."</i></p>
