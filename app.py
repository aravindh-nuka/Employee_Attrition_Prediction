import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("employee_attrition_model.pkl")

st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Employee Attrition Prediction System")
st.markdown("Predict whether an employee is likely to leave the company.")

st.header("Employee Details")

age = st.number_input("Age", 18, 60, 30)

monthly_income = st.number_input(
    "Monthly Income",
    min_value=1000,
    max_value=50000,
    value=5000
)

job_satisfaction = st.slider(
    "Job Satisfaction",
    1, 4, 3
)

job_involvement = st.slider(
    "Job Involvement",
    1, 4, 3
)

environment_satisfaction = st.slider(
    "Environment Satisfaction",
    1, 4, 3
)

stock_option_level = st.selectbox(
    "Stock Option Level",
    [0, 1, 2, 3]
)

years_at_company = st.number_input(
    "Years At Company",
    0, 40, 5
)

years_with_curr_manager = st.number_input(
    "Years With Current Manager",
    0, 20, 3
)

overtime = st.selectbox(
    "OverTime",
    ["No", "Yes"]
)

# Encoding
overtime = 1 if overtime == "Yes" else 0

# Feature Engineering
income_per_year = monthly_income * 12

experience_ratio = (
    years_at_company / age
    if age != 0 else 0
)

promotion_delay = max(
    years_at_company - 1,
    0
)

career_ratio = (
    (years_at_company + 5) / age
    if age != 0 else 0
)

income_per_experience = (
    monthly_income /
    (years_at_company + 1)
)

manager_relationship_score = (
    job_satisfaction + 3
)

# Input Data
input_data = pd.DataFrame([{
    'Age': age,
    'BusinessTravel': 2,
    'DailyRate': 800,
    'Department': 1,
    'DistanceFromHome': 5,
    'Education': 3,
    'EducationField': 1,
    'EnvironmentSatisfaction': environment_satisfaction,
    'Gender': 1,
    'HourlyRate': 60,
    'JobInvolvement': job_involvement,
    'JobLevel': 2,
    'JobRole': 4,
    'JobSatisfaction': job_satisfaction,
    'MaritalStatus': 1,
    'MonthlyIncome': monthly_income,
    'MonthlyRate': 15000,
    'NumCompaniesWorked': 2,
    'OverTime': overtime,
    'PercentSalaryHike': 15,
    'PerformanceRating': 3,
    'RelationshipSatisfaction': 3,
    'StockOptionLevel': stock_option_level,
    'TotalWorkingYears': years_at_company + 5,
    'TrainingTimesLastYear': 3,
    'WorkLifeBalance': 3,
    'YearsAtCompany': years_at_company,
    'YearsInCurrentRole': 3,
    'YearsSinceLastPromotion': 1,
    'YearsWithCurrManager': years_with_curr_manager,
    'IncomePerYear': income_per_year,
    'ExperienceRatio': experience_ratio,
    'PromotionDelay': promotion_delay,
    'CareerRatio': career_ratio,
    'IncomePerExperience': income_per_experience,
    'ManagerRelationshipScore': manager_relationship_score
}])

if st.button("Predict Attrition"):

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error(
            "⚠ Employee is likely to leave the company."
        )
    else:
        st.success(
            "✅ Employee is likely to stay in the company."
        )

    st.subheader("Prediction Probability")

    st.write(
        f"Probability of Leaving: {probability[0][1] * 100:.2f}%"
    )

    st.write(
        f"Probability of Staying: {probability[0][0] * 100:.2f}%"
    )