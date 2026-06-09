# Employee Attrition Prediction

## 🎓 Internship Details

**Internship Provider:** CodeTech IT Solutions

**Intern ID:** CITS1618

**Full Name:** Nuka Aravindh

**Duration:** 4 Weeks

## Project Overview

Employee Attrition Prediction is a Machine Learning project that predicts whether an employee is likely to leave a company. The project uses the IBM HR Analytics Employee Attrition dataset and applies data preprocessing, feature engineering, class imbalance handling, and machine learning techniques to build a predictive model.

## Problem Statement

Employee attrition can significantly impact an organization's productivity and costs. The goal of this project is to identify employees who are at risk of leaving so that HR departments can take proactive measures to improve employee retention.

## Dataset

* Dataset: IBM HR Analytics Employee Attrition Dataset
* Total Records: 1470
* Target Variable: Attrition

  * Yes = Employee leaves the company
  * No = Employee stays in the company

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Imbalanced-Learn (SMOTE)
* Streamlit
* Joblib

## Project Workflow

1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Label Encoding
6. Train-Test Split
7. Random Forest Classification
8. Class Imbalance Analysis
9. SMOTE Oversampling
10. Hyperparameter Tuning using GridSearchCV
11. Feature Importance Analysis
12. Prediction on New Employee Data
13. Streamlit Application Development

## Feature Engineering

The following features were created:

* IncomePerYear
* ExperienceRatio
* PromotionDelay
* CareerRatio
* IncomePerExperience
* ManagerRelationshipScore

## Model Performance

### Final Random Forest Model

* Accuracy: 86.73%
* Precision (Attrition = Yes): 50%
* Recall (Attrition = Yes): 36%
* F1-Score: 42%

### Confusion Matrix

```text
[[241 14]
 [25 14]]
```

## Important Features

Top factors influencing employee attrition:

1. StockOptionLevel
2. IncomePerYear
3. JobSatisfaction
4. MonthlyIncome
5. JobInvolvement
6. PromotionDelay
7. YearsInCurrentRole
8. EnvironmentSatisfaction
9. YearsWithCurrManager

## Business Insights

* Employees with lower stock option benefits are more likely to leave.
* Job satisfaction significantly influences retention.
* Monthly income plays an important role in employee decisions.
* Delayed promotions increase the likelihood of attrition.
* Work environment satisfaction affects employee retention.

## Project Structure

```text
Employee_Attrition_Prediction/
│
├── Data/
├── Notebook/
├── Screenshots/
├── employee_attrition_model.pkl
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

## Future Improvements

* Compare multiple machine learning algorithms.
* Add advanced feature engineering.
* Deploy using Streamlit Cloud.
* Improve recall using advanced ensemble methods.

## Author

**Aravindh Nuka**


## Conclusion

This project demonstrates an end-to-end Machine Learning workflow including data preprocessing, feature engineering, handling imbalanced datasets, model tuning, prediction, and deployment through a Streamlit application. The model can assist HR departments in identifying employees at risk of attrition and support data-driven retention strategies.
