<h1 align="center">SpaceX Falcon 9 Data Science Project</h1>

This repository contains the complete SpaceX Falcon 9 analysis, visualizations, and machine learning workflow.
The project includes the original analytical work (data collection, web scraping, wrangling, SQL EDA, visualization, modeling) 
and an extended engineering layer (pipelines, monitoring systems, Java utilities, and architecture experiments).

<p align="center">
  <![Falcon 9 landing](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/landing_1.gif)>
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

spacex_project/
├── notebooks/ # Jupyter notebooks (API, scraping, EDA, SQL, ML)
├── reports/ # Presentation (PDF, PPTX)
├── engineering/ # Extended engineering modules
│ ├── java/ # Java utilities and integrations
│ ├── monitoring/ # Monitoring concepts & load-control ideas
│ └── pipelines/ # Early MLOps/DevOps pipeline drafts
└── README.md


---

# Notebooks

### Data acquisition
- **[jupyter-labs-spacex-data-collection-api.ipynb](notebooks/jupyter-labs-spacex-data-collection-api.ipynb)**  
  Collects launch data from the SpaceX REST API.

- **[jupyter-labs-webscraping.ipynb](notebooks/jupyter-labs-webscraping.ipynb)**  
  Scrapes additional Falcon 9 launch information from Wikipedia.

### Wrangling & preprocessing
- **[labs-jupyter-spacex-Data wrangling.ipynb](notebooks/labs-jupyter-spacex-Data%20wrangling.ipynb)**  
  Cleaning and transforming launch datasets.  
  Feature engineering and categorical encoding.

### SQL-based EDA
- **[jupyter-labs-eda-sql-coursera_sqllite.ipynb](notebooks/jupyter-labs-eda-sql-coursera_sqllite.ipynb)**  
  Exploratory analysis using SQL on an SQLite database (`my_data1.db`).

### Visualization EDA
- **[edadataviz.ipynb](notebooks/edadataviz.ipynb)**  
  Seaborn/Matplotlib visual analysis of launch patterns.

### Launch site mapping
- **[lab_jupyter_launch_site_location.ipynb](notebooks/lab_jupyter_launch_site_location.ipynb)**  
  Folium-powered interactive maps showing launch sites, trajectories, and risk areas.

### Machine learning prediction
- **[SpaceX_Machine Learning Prediction_Part_5.ipynb](notebooks/SpaceX_Machine%20Learning%20Prediction_Part_5.ipynb)**  
  ML workflow:  
  - Logistic Regression  
  - SVM  
  - Decision Tree  
  - KNN  
  Includes hyperparameter tuning (GridSearchCV) and confusion matrices.

---

# Data Files

Located in `notebooks/`:

- `dataset_part_1.csv`  
- `dataset_part_3.csv`  
- `spacex_web_scraped.csv`  
- `features_one_hot.csv`  
- `my_data1.db` — SQLite database used for SQL EDA

Raw data is fetched automatically from IBM Skills Network URLs in the notebooks.

---

# Reports

Located in `reports/`:

- `ds-capstone-template-coursera.pptx` — Coursera-provided template  
- `spacex_capstone_presentation.pdf` — final submission-ready report (once exported)

---

# Engineering Layer

Additional engineering modules expanding the project beyond the Coursera scope.

### **[engineering/java/](engineering/java/)**  
Java-based experiments, utilities, data processing prototypes, integration tooling.

### **[engineering/monitoring/](engineering/monitoring/)**  
System monitoring concepts including:  
resource load tracking, automated throttling during ML training,  
early implementations inspired by the “Gorgon System”.

### **[engineering/pipelines/](engineering/pipelines/)**  
DevOps/MLOps drafts:  
scheduled data ingestion, ETL ideas, notebook → production transformations,  
early retraining pipeline concepts.

---

# Environment

Install all dependencies:

pip install -r requirements.txt


A full list of packages is stored in **requirements.txt** in the project root.

---

# License

This project is licensed under the **Apache License 2.0**.  
See the `LICENSE` file for details.

---

# Acknowledgements

Based on the **IBM Data Science Professional Certificate – Capstone Project** (Coursera).  
SpaceX® is a trademark of Space Exploration Technologies Corp.  
This work is for educational purposes only and is not affiliated with SpaceX.

---

<p align="center">
  <![Falcon 9 crash](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/crash.gif)
>
</p>

<p align="center">
  <i>“The goal was simple: predict this outcome.”</i>
</p>
