# Engineering Layer

This directory contains the **engineering layer** of the project — a space for
experimental, infrastructural, and automation-oriented work that extends the
core Data Science notebooks.

While the main project focuses on exploratory analysis, visualization, and
machine learning using Jupyter notebooks (as required by the IBM Applied Data
Science Capstone), this layer explores how such work can evolve toward more
structured, automated, and production-aware solutions.

The contents of this directory are **not part of Coursera autograding** and are
intentionally separated from the educational notebook workflow.

---

## Purpose

The Engineering Layer serves several goals:

- Bridge exploratory notebook-based work with engineering practices
- Experiment with DevOps / MLOps concepts in a low-risk environment
- Prototype automation, monitoring, and cross-language ideas
- Prepare a clean foundation for future expansion beyond the course scope

This layer reflects a mindset shift from *“completing assignments”* to
*“building systems”*.

---

## Structure

```
engineering/
├── ENGINEERING.md
│
├── java/
│   └── README.md
│
├── monitoring/
│   └── README.md
│
└── pipelines/
    ├── README.md
    └── sync_notebook_data.py
```

---

## Subdirectories Overview

### `java/`

Java-based utilities and experimental components.

This directory is reserved for:
- Java prototypes related to data processing or monitoring
- Cross-language experiments (Python ↔ Java)
- Early exploration of JVM-based tooling for analytics or infrastructure tasks

The intent is **not** to replace Python-based Data Science workflows, but to
explore complementary engineering approaches.

See details in: `engineering/java/README.md`

---

### `monitoring/`

Concepts, drafts, and experiments related to **system monitoring and stability**.

Primary focus areas:
- Observing CPU, memory, and disk usage during model training
- Understanding failure modes on limited hardware
- Exploring ideas for crash prevention and adaptive workload control

This directory is closely related to future DevOps / MLOps work and may later
evolve into standalone monitoring components or services.

See details in: `engineering/monitoring/README.md`

---

### `pipelines/`

Lightweight engineering pipelines and automation utilities.

Current and planned topics include:
- Data ingestion helpers
- ETL-style transformations
- Synchronization between notebook outputs and structured data directories
- Early notebook-to-production transition experiments

#### Current utility

**`sync_notebook_data.py`**  
A standalone script that synchronizes data artifacts generated in `notebooks/`
(e.g., CSV files, SQLite databases) into `data/processed/`, while preserving
full compatibility with Coursera autograding requirements.

This script demonstrates a minimal but practical example of engineering
automation layered on top of exploratory work.

See details in: `engineering/pipelines/README.md`

---

## Design Principles

- **Separation of concerns**  
  Educational notebooks remain untouched; engineering experiments live here.

- **Low coupling**  
  Nothing in this layer is required for the core project to run or be graded.

- **Incremental evolution**  
  Scripts and ideas start simple and can later grow into more formal pipelines
  or services.

- **Transparency**  
  All automation is explicit, readable, and easy to reason about.

---

## Future Directions

Possible future extensions of this layer include:
- Dataset versioning strategies
- Reproducible ETL pipelines
- Resource-aware model training helpers
- Monitoring dashboards or background services
- Deeper integration with DevOps / MLOps workflows

This directory is intentionally open-ended and evolves alongside the author's
learning path.

---

## Relation to the Main Project

The Engineering Layer complements — but does not replace — the core Data Science
work of the project.

It exists to demonstrate **engineering thinking**, system awareness, and
long-term architectural considerations beyond the scope of the original course.
