# ✅ STEP 1: Create or retrain the model and label encoders to match your local environment (scikit-learn 1.4.2)

import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# --- Step 1. Prepare synthetic dataset with all necessary fields ---
data = pd.DataFrame({
    'Age': np.random.randint(18, 50, 300),
    'Gender': np.random.choice(['Male', 'Female', 'Other'], 300),
    'High_School_GPA': np.random.uniform(2.0, 4.0, 300),
    'SAT_Score': np.random.randint(800, 1600, 300),
    'University_Ranking': np.random.randint(1, 500, 300),
    'University_GPA': np.random.uniform(2.0, 4.0, 300),
    'Internships_Completed': np.random.randint(0, 5, 300),
    'Projects_Completed': np.random.randint(0, 10, 300),
    'Certifications': np.random.randint(0, 5, 300),
    'Soft_Skills_Score': np.random.randint(1, 6, 300),
    'Networking_Score': np.random.randint(1, 6, 300),
    'Job_Offers': np.random.randint(0, 4, 300),
    'Starting_Salary': np.random.randint(30, 150, 300),
    'Career_Satisfaction': np.random.randint(1, 6, 300),
    'Years_to_Promotion': np.random.randint(0, 10, 300),
    'Current_Job_Level': np.random.choice(['Entry', 'Mid', 'Senior'], 300),
    'Work_Life_Balance': np.random.randint(1, 6, 300),
    'Entrepreneurship': np.random.choice(['Yes', 'No'], 300),
    'Major': np.random.choice(['Engineering', 'Arts', 'Business', 'Science'], 300),
    'Coding_Proficiency': np.random.choice(['Beginner', 'Intermediate', 'Advanced'], 300),
    'Leadership_Roles': np.random.randint(0, 3, 300),
    'Extracurriculars': np.random.randint(0, 5, 300),
    'Career_Path': np.random.choice([0, 1], 300)  # 0 = Non-Tech, 1 = Tech
})

# --- Step 2. Encode categorical features ---
label_encoders = {}
categorical_cols = ['Gender', 'Current_Job_Level', 'Entrepreneurship', 'Major', 'Coding_Proficiency']

for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# --- Step 3. Split data and train model ---
X = data.drop('Career_Path', axis=1)
y = data['Career_Path']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# --- Step 4. Evaluate ---
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# --- Step 5. Save model and encoders ---
with open("career_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("label_encoders.pkl", "wb") as f:
    pickle.dump(label_encoders, f)

print("✅ Model and encoders saved successfully.")
