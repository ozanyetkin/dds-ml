# dds-ml

Machine learning and data science examples for Digital Design Studio workshops and tutorials.

## Overview

This repository contains practical Python examples covering data analysis, visualization, and machine learning fundamentals. It includes hands-on exercises for learning essential data science workflows.

## Contents

### Data Analysis (`data_analysis.py`)

Statistical analysis examples using weather data:

- Mean, median, and standard deviation calculations
- Pearson correlation coefficient
- Manual implementations vs. using the `statistics` library

### Data Visualization (`data_visualization.py`)

Creating various chart types with matplotlib:

- Histograms
- Bar charts
- Pie charts
- Time series plots
- Scatter plots with color coding

### Data Preprocessing (`data_preprocessing.py`)

Complete ML pipeline using the California housing dataset:

- Handling missing values (dropna vs. fillna)
- Encoding categorical features (one-hot encoding, label encoding)
- Feature scaling (StandardScaler, MinMaxScaler, MaxAbsScaler)
- Train-test split
- Linear regression model training and evaluation

### Preprocessing Workshop (`preprocessing_workshop.py`)

Focused preprocessing exercise:

- Loading data with pandas
- Handling missing values
- Encoding categorical variables
- Exporting preprocessed data to CSV

## Datasets

- `weather_data.txt` - Temperature data for statistical analysis
- `housing.csv` - California housing dataset
- `housing_preprocessed.csv` - Preprocessed version of housing data

## Requirements

```txt
pandas
numpy
matplotlib
scikit-learn
```

Install dependencies:

```bash
pip install pandas numpy matplotlib scikit-learn
```

## Python Setup Instructions

For Python setup and introduction guide, visit the [Introduction to Python Programming guide](https://mysterious-snowman-10b.notion.site/Introduction-to-Python-Programming-Outline-2ea01d12b64649128a55c7939dde1df1).
