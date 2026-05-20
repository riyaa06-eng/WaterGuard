# WaterGuard AI: Advanced Water Quality Prediction System

WaterGuard AI is a premium, professional-grade water safety analysis platform designed to provide real-time water quality assessment. It combines a machine learning powered backend with a modern and responsive web interface to deliver fast, intelligent, and user-friendly water safety predictions.

---

## 🚀 Features

- **Modern Responsive UI** — Clean and professional interface with smooth user experience.
- **Real-time Water Analysis** — Instant prediction of water safety based on selected chemical parameters.
- **Machine Learning Integration** — Predictive analysis using trained classification models.
- **Dynamic Prediction Results** — Displays whether the water is **Safe** or **Unsafe** instantly.
- **Feature Selection Pipeline** — Optimized prediction using selected important features.
- **Interactive Input Forms** — User-friendly forms with validation and tooltips.
- **FastAPI Backend Integration** — High-performance API for real-time predictions.

---

## 🛠️ Tech Stack

### Frontend
- **Framework:** HTML5 + Jinja2 Templates
- **Styling:** CSS3
- **Icons:** Font Awesome
- **Templating Engine:** Jinja2

### Backend
- **Framework:** FastAPI (Python)
- **Server:** Uvicorn

### Machine Learning
- **Library:** Scikit-learn
- **Algorithms Used:**
  - K-Nearest Neighbors (KNN)
  - Logistic Regression
  - Random Forest Classifier
- **Data Processing:** NumPy & Pandas
- **Feature Selection:** SelectKBest
- **Scaling:** StandardScaler
- **Serialization:** Pickle

---

## 📁 Project Structure

```bash
ANTIGRAVITY_WATER_QUALITY_PROJECT/
│
├── backend/                     # FastAPI Backend
│   ├── __pycache__/
│   ├── features.pkl             # Selected feature names
│   ├── main.py                  # Main FastAPI application
│   ├── model.pkl                # Trained ML model
│   ├── scaler.pkl               # StandardScaler object
│   └── requirements.txt         # Python dependencies
│
├── frontend/                    # Frontend UI
│   ├── static/
│   │   ├── css/
│   │   │   └── main.css         # Main stylesheet
│   │   │
│   │   ├── images/
│   │   │   └── hero-water.png   # UI assets
│   │   │
│   │   └── js/
│   │
│   ├── templates/
│   │   ├── about.html
│   │   ├── index.html
│   │   ├── layout.html
│   │   ├── predict.html
│   │   └── result.html
│   │
│   └── package-lock.json
│
├── notebook/
│   └── water_analysis.ipynb     # Model training notebook
│
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Activate virtual environment:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI server:

```bash
uvicorn main:app --reload
```

---

## 🌐 Open Application

Open browser and visit:

```bash
http://127.0.0.1:8000
```

---

## 📊 ML Model Details

The system utilizes multiple machine learning models trained on water quality datasets to determine whether water is safe for consumption.

### Models Trained
- K-Nearest Neighbors (KNN)
- Logistic Regression
- Random Forest Classifier

### ✅ Final Selected Model
**Random Forest Classifier**

### Selected Features Used
- Aluminium
- Arsenic
- Barium
- Cadmium
- Chloramine
- Chromium
- Viruses
- Nitrates
- Radium
- Silver

---

## 📈 Model Performance

| Model | Accuracy |
|------|------|
| KNN | 89.7% |
| Logistic Regression | 89.41% |
| Random Forest | 91.91% |

Random Forest achieved the highest accuracy and was selected for deployment.

---

## 🔮 Future Enhancements

- Cloud Deployment
- Real-time IoT Sensor Integration
- Water Quality Report Generation
- Historical Prediction Tracking
- User Authentication System
- Interactive Analytics Dashboard

---

## 📄 License

This project is developed for educational and learning purposes.

---

*Disclaimer: This project is intended for educational purposes only and should not be used as a substitute for professional laboratory water testing.*