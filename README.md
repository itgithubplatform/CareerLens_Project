# 💼 PathWise AI – Tech vs Non-Tech Career Predictor

**PathWise AI** is a smart, machine learning–powered web application built with **Streamlit** that helps individuals discover whether they are more aligned with a **Tech** or **Non-Tech** career path, based on 18+ critical career and personal development indicators.

🚀 **Live Demo**: *(Add your Streamlit Cloud link here once deployed)*

---

## 📌 Features

- 🔍 Predicts career category: **Tech** or **Non-Tech**
- 🧠 Uses a trained Random Forest classification model
- 🧾 Takes into account over 18 academic, professional, and personal metrics
- 💬 Interactive and modern UI built with **Streamlit**
- 🧩 Efficient input system with dynamic slider and dropdown rendering
- 💾 Uses saved label encoders for categorical preprocessing
- ☁️ Easy to deploy on **Streamlit Cloud**

---

## 🧪 Model Inputs

The model uses the following input features:

- `Age`
- `Gender`
- `High_School_GPA`
- `SAT_Score`
- `University_Ranking`
- `University_GPA`
- `Internships_Completed`
- `Projects_Completed`
- `Certifications`
- `Soft_Skills_Score`
- `Networking_Score`
- `Job_Offers`
- `Starting_Salary`
- `Career_Satisfaction`
- `Years_to_Promotion`
- `Current_Job_Level`
- `Work_Life_Balance`
- `Entrepreneurship`

> 🔧 *Note: All categorical fields are label-encoded using pre-trained encoders.*

---

## 📂 Folder Structure
PathWiseAI/
├── app.py # Streamlit frontend (main file)
├── career_model.pkl # Trained classification model (RandomForest or similar)
├── label_encoders.pkl # Pre-fitted label encoders for categorical features
├── requirements.txt # Python dependencies
└── README.md # Project documentation



---

## ⚙️ Getting Started

### 🔧 Installation

```bash
pip install -r requirements.txt
```


### ▶️ Run the App Locally

```bash
streamlit run app.py
```

---

## ☁️ Deployment on Streamlit Cloud

1. Push this repo to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub and deploy your repo
4. App will go live in minutes!

---

## 👨‍💻 Author

- **Devendra Savalkar**  
  📧 [LinkedIn](https://www.linkedin.com/in/devendra-savalkar) | 🌐 *Add other links if you'd like*

---

## 📃 License

This project is open source and available under the [MIT License](LICENSE).
