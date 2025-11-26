# INSY 6500 – Global Air Quality EDA Project

## Project Overview
This repository contains work for the Global Air Quality Exploratory Data Analysis project. The purpose of the project is to apply the EDA workflow covered in class, including data loading, cleaning, transformation, visualization, and interpretation. The project is completed using Jupyter Notebook and follows practices demonstrated in HW3A.

## Course Information
Course: INSY 6500 – Modern Tools for Data Analysis  
Students: Osama Abu-Farsakh, Waleed Khasawneh  
Semester: Fall 2025  

## Dataset Description
This project analyzes an online dataset related to global air quality, with a focus on environmental and atmospheric pollutant measurements across major world cities. The dataset was sourced from the World Air Quality Index (WAQI) project and hosted on Kaggle. It contains 10,000 observations, with each record representing a unique combination of city and date, along with associated pollutant and climate values.

The dataset includes 12 variables describing measurement context and pollutant concentrations, including:

- City
- Country
- Date
- PM2.5
- PM10
- NO2
- SO2
- CO
- O3
- Temperature
- Humidity
- Pressure

Source: https://www.kaggle.com/datasets/waqi786/global-air-quality-dataset

## Repository Structure
data/ – dataset used in the project  
notebooks/ – EDA and analysis notebooks  
README.md – documentation  
.gitignore – excluded files and temporary content  

## How to Run the Project
1. Open Anaconda Prompt
2. Activate the course environment:
   conda activate insy6500
3. Navigate to the project directory:
   cd ~/insy6500/projects/global-air-quality-eda
4. Launch Jupyter Notebook:
   jupyter notebook
5. Open the notebook located in notebooks/

## Tools and Libraries Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Notes
This project applies everything taught in the Data Analysis course, including tools, techniques, workflows, and best practices, using a real dataset to demonstrate understanding and practical implementation.
