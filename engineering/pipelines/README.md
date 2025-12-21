# ⚙️ Pipelines & Automation

This directory contains **lightweight engineering pipelines and automation
utilities** that support the notebook-based workflow.

The focus is on practical, transparent tools that improve structure without
interfering with Coursera autograding.

## Current Tools

### sync_notebook_data.py

Synchronizes data artifacts generated in `notebooks/` (CSV files, SQLite
databases, etc.) into `data/processed/`.

**Usage:**
```bash
python engineering/pipelines/sync_notebook_data.py
```

This script is intentionally standalone and safe to run manually.

## Planned Directions

- Reproducible ETL helpers
- Dataset organization and versioning
- Notebook-to-structured-pipeline transitions
- Early MLOps-style automation experiments

## Design Philosophy

- Minimal complexity
- Explicit behavior
- No hidden side effects
