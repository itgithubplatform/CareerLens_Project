import streamlit as st
import pandas as pd
import pickle

# Load model and label encoders
model = pickle.load(open("career_model.pkl", "rb"))
label_encoders = pickle.load(open("label_encoders.pkl", "rb"))

# ✅ Step 1: Pull correct feature order from the model
expected_features = list(model.feature_names_in_)

st.title("CareerLens: Tech vs Non-Tech Career Predictor")
st.markdown("### Enter your information below:")

# ✅ Step 2: Collect inputs from user
age = st.slider("Age", 16, 60, 22)
gender = st.selectbox("Gender", label_encoders["Gender"].classes_)
gpa = st.slider("High School GPA", 0.0, 4.0, 3.0)
sat = st.slider("SAT Score", 400, 1600, 1000)
ranking = st.slider("University Ranking (1 = Top)", 1, 500, 100)
uni_gpa = st.slider("University GPA", 0.0, 4.0, 3.0)
interns = st.slider("Internships Completed", 0, 10, 1)
projects = st.slider("Projects Completed", 0, 20, 3)
certs = st.slider("Certifications", 0, 10, 1)
soft_skills = st.slider("Soft Skills Score (1-5)", 1, 5, 3)
networking = st.slider("Networking Score (1-5)", 1, 5, 3)
offers = st.slider("Job Offers Received", 0, 5, 1)
salary = st.slider("Starting Salary (in thousands)", 0, 200, 50)
satisfaction = st.slider("Career Satisfaction (1-5)", 1, 5, 3)
promotion_years = st.slider("Years to Promotion", 0, 10, 2)
job_level = st.selectbox("Current Job Level", label_encoders["Current_Job_Level"].classes_)
balance = st.slider("Work-Life Balance (1-5)", 1, 5, 3)
entrepreneurship = st.selectbox("Entrepreneurship Interest", label_encoders["Entrepreneurship"].classes_)
coding = st.slider("Coding Proficiency (1-10)", 1, 10, 5)
extracurriculars = st.slider("Extracurricular Activities (1-5)", 1, 5, 3)
leadership = st.slider("Leadership Roles (1-5)", 1, 5, 3)
major = st.selectbox("Major", label_encoders["Major"].classes_)

# ✅ Step 3: Build full input dictionary
input_dict = {
    'Age': age,
    'Gender': gender,
    'High_School_GPA': gpa,
    'SAT_Score': sat,
    'University_Ranking': ranking,
    'University_GPA': uni_gpa,
    'Internships_Completed': interns,
    'Projects_Completed': projects,
    'Certifications': certs,
    'Soft_Skills_Score': soft_skills,
    'Networking_Score': networking,
    'Job_Offers': offers,
    'Starting_Salary': salary,
    'Career_Satisfaction': satisfaction,
    'Years_to_Promotion': promotion_years,
    'Current_Job_Level': job_level,
    'Work_Life_Balance': balance,
    'Entrepreneurship': entrepreneurship,
    'Coding_Proficiency': coding,
    'Extracurriculars': extracurriculars,
    'Leadership_Roles': leadership,
    'Major': major
}

# ✅ Step 4: Convert to DataFrame
input_df = pd.DataFrame([input_dict])

# ✅ Step 5: Apply label encoding to all categorical columns
for col in input_df.columns:
    if col in label_encoders and input_df[col].dtype == object:
        le = label_encoders[col]
        val = input_df[col].iloc[0]
        if val not in le.classes_:
            st.error(f"'{val}' is not a recognized value for '{col}'")
            st.stop()
        input_df[col] = le.transform([val])

# ✅ Step 6: Reorder columns to match the model
input_df = input_df[expected_features]

# ✅ Step 7: Make prediction
if st.button("Predict Career Path"):
    prediction = model.predict(input_df)[0]
    result = "💻 Tech" if prediction == 1 else "📘 Non-Tech"
    st.success(f"Recommended Career Path: **{result}**")
