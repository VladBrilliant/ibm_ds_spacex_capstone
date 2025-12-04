<h1 align="center">SpaceX Falcon 9 Data Science Project</h1>

This repository contains the complete SpaceX Falcon 9 analysis, visualizations, and machine learning workflow.
The project includes the original analytical work (data collection, web scraping, wrangling, SQL EDA, visualization, modeling) 
and an extended engineering layer (pipelines, monitoring systems, and Java-based tools).

<p align="center">
  <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/landing_1.gif" alt="Falcon 9 landing">
</p>

---

# Table of Contents
- [Project Structure](#project-structure)
- [Notebooks](#notebooks)
- [Data Files](#data-files)
- [Reports](#reports)
- [Engineering Layer](#engineering-layer)
- [Environment](#environment)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

# Project Structure

```
spacex_project/
├── notebooks/           # Jupyter notebooks (API, scraping, EDA, SQL, ML)
├── reports/             # Presentation (PDF, PPTX)
├── engineering/         # Extended engineering modules
│   ├── java/            # Java utilities and integrations
│   ├── monitoring/      # Monitoring concepts & load-control ideas
│   └── pipelines/       # Early MLOps/DevOps pipeline drafts
└── README.md
```

---

# Notebooks

### Data acquisition
- **jupyter-labs-spacex-data-collection-api.ipynb** — Collects launch data from the SpaceX REST API.
- **jupyter-labs-webscraping.ipynb** — Scrapes additional Falcon 9 launch information from Wikipedia.

### Wrangling & preprocessing
- **labs-jupyter-spacex-Data wrangling.ipynb** — Cleaning, transforming datasets, feature engineering.

### SQL-based EDA
- **jupyter-labs-eda-sql-coursera_sqllite.ipynb** — Exploratory SQL analysis on SQLite database.

### Visualization EDA
- **edadataviz.ipynb** — Seaborn/Matplotlib visual analysis.

### Launch site mapping
- **lab_jupyter_launch_site_location.ipynb** — Folium interactive maps.

### Machine learning prediction
- **SpaceX_Machine Learning Prediction_Part_5.ipynb** — ML workflow (LogReg, SVM, DT, KNN).

---

# Data Files

Located in `notebooks/`:

- dataset_part_1.csv  
- dataset_part_3.csv  
- spacex_web_scraped.csv  
- features_one_hot.csv  
- my_data1.db — SQLite database

---

# Reports

Located in `reports/`:

- ds-capstone-template-coursera.pptx  
- spacex_capstone_presentation.pdf  

---

# Engineering Layer

### engineering/java/
Java-based processing utilities.

### engineering/monitoring/
Concepts for system monitoring & load-control tools.

### engineering/pipelines/
Early drafts of DevOps/MLOps workflows.

---

# Environment

```
pip install -r requirements.txt
```

---

# License

Apache License 2.0 — see LICENSE file.

---

# Acknowledgements

Based on IBM Data Science Professional Certificate (Coursera).
Not affiliated with SpaceX.

<p align="center">
  <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/crash.gif" alt="Falcon 9 crash">
</p>

<p align="center">
  <i>“The goal was simple: predict this outcome.”</i>
</p>
