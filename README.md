# Solar Challenge Week 1

## Overview
This project performs data profiling, cleaning, EDA, and cross-country comparison for solar datasets from Benin, Sierra Leone, and Togo.

## Environment Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/abeelgetahun/solar-challenge-week1.git
    cd solar-challenge-week1
    ```
2. **Create and activate a virtual environment (recommended):**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Analysis

- Run notebooks in the `notebooks/` directory or scripts in `src/` as described below.
- Cleaned datasets are exported to `data/cleaned/` (not tracked by git).
- Visualizations and statistical results are saved in `outputs/`.

## Project Structure

```
solar-challenge-week1/
│
├── data/               # Raw datasets (not tracked by git)
├── data/cleaned/       # Cleaned datasets (not tracked by git)
├── notebooks/          # Jupyter Notebooks for EDA and analysis
├── src/                # Source code (functions, classes)
├── outputs/            # Generated plots, charts, reports (not tracked by git)
├── requirements.txt
├── .gitignore
├── .github/workflows/ci.yml
└── README.md
```

## GitHub Actions CI

- The workflow in `.github/workflows/ci.yml` validates environment setup and runs automated checks on code.

## Commit & Branching Policy

- All major features are implemented in feature branches and merged to `main` via Pull Requests, with descriptive commit messages.

## Contact

For questions, open an issue or contact the repo maintainer.