# SpaceX Falcon 9 Data Science Project

<p align="center">
  <img src="images/tenor2.gif" width="48%">
  <img src="images/tenor1.gif" width="48%">
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
ibm_ds_spacex_capstone/
│   .gitignore
│   LICENSE
│   README.md
│   requirements.txt
│
├── notebooks/
│
├── data/
│   └── processed/
│
├── images/              # GIF animations and static images used in README and report
│
├── reports/             # Final PPTX / PDF reports (to be added)
│
└── engineering/
    ├── java/
    ├── monitoring/
    └── pipelines/
```

---

## Notebooks

### Data Acquisition
- notebooks/jupyter-labs-spacex-data-collection-api.ipynb
- notebooks/jupyter-labs-webscraping.ipynb

### Data Wrangling & Preprocessing
- notebooks/labs-jupyter-spacex-Data wrangling.ipynb

### SQL EDA
- notebooks/jupyter-labs-eda-sql-coursera_sqllite.ipynb

### Visualization EDA
- notebooks/edadataviz.ipynb

### Launch Site Mapping
- notebooks/lab_jupyter_launch_site_location.ipynb

### Machine Learning Prediction
- notebooks/SpaceX Machine Learning Prediction_Part_5.ipynb

---

## Dashboard Screenshot

<p align="center">
  <img src="images/spacex_dash.png" width="700">
</p>

---
## Run Dashboard (Dash)
> The dashboard is a local Dash application.
> To run it, clone this repository to your machine and execute the commands below from the project root directory.


1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
2. Run the dashboard:
   ```bash
   python engineering/pipelines/dashboard/app.py


3. Open in browser:

   http://127.0.0.1:8050/

---

## Data Files

Located under `notebooks/`:

- notebooks/dataset_part_1.csv
- notebooks/dataset_part__3.csv
- notebooks/spacex_web_scraped.csv
- notebooks/features_one_hot.csv
- notebooks/my_data1.db
- spacex_launch_dash.csv

These files are intermediate artifacts produced during the labs (data collection, scraping, wrangling and feature engineering).

### Data Organization Note

For Coursera autograding compatibility, all datasets used in the notebooks
are stored directly in the `notebooks/` directory.

For better project organization and engineering workflows (e.g., dashboard
and pipelines), copies of generated datasets may also appear under:

- `data/processed/`

These files are synchronized from `notebooks/` and are not used by the
autograding system.

---

## Reports

Stored in `reports/` (when added):

- ds-capstone-template-coursera.pptx
- spacex_capstone_presentation.pdf (if exported)

**How to download report files from GitHub:**

1. Open the file in the `reports/` folder (click on its name in GitHub).
2. Click the “Download raw” button,  
   or right‑click the link and select **“Save link as…”**.

---

## Engineering Layer

The **Engineering Layer** contains experimental and forward‑looking engineering
extensions built on top of the core Data Science work.

- **[`engineering/`](engineering/ENGINEERING.md)**  
  Entry point for the engineering layer, design principles, and architecture overview.

- **[`engineering/java/`](engineering/java/README.md)**  
  Java utilities and helper scripts (future extensions, e.g. Java-based ML or monitoring prototypes).

- **[`engineering/monitoring/`](engineering/monitoring/README.md)**  
  Concepts and drafts for monitoring system load and preventing crashes during model training on limited hardware.

- **[`engineering/pipelines/`](engineering/pipelines/README.md)**  
  Early DevOps/MLOps pipeline ideas: data ingestion, ETL, and notebook-to-production transformations.

---

## Environment

Install dependencies:

```bash
pip install -r requirements.txt
```

You can then open the notebooks from the `notebooks/` directory using Jupyter, JupyterLab or VS Code.

---

## License

This project is licensed under the **Apache License 2.0** — see [LICENSE](LICENSE).

---

## Acknowledgements

This repository is the Capstone Project for the **IBM Data Science Professional Certificate** on Coursera.

It is an educational project and is **not affiliated with SpaceX**.  
SpaceX® is a trademark of Space Exploration Technologies Corp.

---

<p align="center">
  <img src="images/crash.gif" width="450">
</p>

<p align="center"><i>"The goal was simple: predict this outcome."</i></p>
