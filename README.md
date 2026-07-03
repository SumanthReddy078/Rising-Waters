# 🌊 Rising Waters: A Machine Learning Approach to Flood Prediction

An end-to-end **Machine Learning-based Flood Prediction System** developed using **Python, Scikit-learn, Flask, HTML, CSS, and Bootstrap**. The project predicts the likelihood of floods using historical weather and rainfall parameters, helping disaster management authorities make informed decisions through an easy-to-use web application.

---

# 📁 Project Structure

```
RisingWatersProject/
│
├── app/
│   ├── app.py                     # Flask application
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── images/
│   │       ├── flood.png
│   │       ├── no_flood.png
│   │       └── home.png
│   │
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── predict.html
│       ├── result.html
│       └── error.html
│
├── data/
│   └── flood dataset.csv                  # Flood prediction dataset
│
├── models/
│   ├── floods.save                # Trained Random Forest model
│   └── scaler.save                # StandardScaler object
│
├── notebooks/
│   ├── EDA.ipynb                  # Exploratory Data Analysis
│   └── Model_Training.ipynb       # Model Building & Evaluation
│
├── src/
│   ├── config.py                  # Configuration settings
│   ├── model_loader.py            # Load saved model & scaler
│   └── predictor.py               # Prediction logic
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ 1. Environment Setup

Create a virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 📊 2. Dataset

The project uses a historical flood prediction dataset containing weather-related parameters.

### Features

| Feature | Description |
|----------|-------------|
| Temp | Temperature (°C) |
| Humidity | Relative Humidity (%) |
| Cloud Cover | Cloud Cover (%) |
| ANNUAL | Annual Rainfall (mm) |
| Jan-Feb | Rainfall during Jan–Feb |
| Mar-May | Rainfall during Mar–May |
| Jun-Sep | Rainfall during Jun–Sep |
| Oct-Dec | Rainfall during Oct–Dec |
| avgjune | Average Rainfall in June |
| sub | Subdivision Rainfall |
| flood | Target Variable (0 = No Flood, 1 = Flood) |

---

# 📈 3. Exploratory Data Analysis (EDA)

EDA was performed using Jupyter Notebook to understand the dataset before model training.

The analysis includes:

- Dataset overview
- Missing value analysis
- Duplicate value analysis
- Descriptive statistics
- Univariate Analysis
- Multivariate Analysis
- Distribution plots
- Histograms
- Boxplots
- Correlation Heatmap
- Pair Plot
- Flood distribution visualization
- Feature importance analysis

Libraries used:

- Pandas
- NumPy
- Matplotlib
- Seaborn

---

# 🧹 4. Data Pre-processing

The dataset was preprocessed before training the Machine Learning models.

Steps performed:

- Checked missing values
- Removed duplicate records
- Split features and target
- Train-Test Split (80:20)
- Feature Scaling using StandardScaler
- Saved fitted scaler using Joblib

---

# 🤖 5. Model Building

The following Machine Learning algorithms were trained and compared:

- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)
- XGBoost Classifier

Each model was evaluated using:

- Accuracy Score
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

---

# 🏆 6. Best Model Selection

The **Random Forest Classifier** achieved the best overall performance on the dataset and was selected for deployment.

### Model Performance

| Model | Accuracy |
|--------|----------|
| Decision Tree | 95.65% |
| Random Forest | **95.65%** ✅ |
| KNN | 86.96% |
| XGBoost | 86.96% |

The trained model and scaler were saved using Joblib.

```python
joblib.dump(best_model, "models/floods.save")
joblib.dump(scaler, "models/scaler.save")
```

---

# 🌐 7. Flask Web Application

Run the application

```bash
python app/app.py
```

Open the browser

```
http://127.0.0.1:5000
```

---

## Application Pages

### 🏠 Home Page

- Project overview
- Features
- About the project
- Navigation to prediction page

---

### 🌧️ Prediction Page

Users enter:

- Temperature
- Humidity
- Cloud Cover
- Annual Rainfall
- Jan-Feb Rainfall
- Mar-May Rainfall
- Jun-Sep Rainfall
- Oct-Dec Rainfall
- Average June Rainfall
- Subdivision Rainfall

---

### 📊 Result Page

Displays

- Flood Risk Detected
- No Flood Risk Detected
- Prediction message

---

# ☁️ 8. IBM Cloud Deployment (Future Scope)

The application can be deployed on IBM Cloud using:

- IBM Cloud Foundry
- IBM Code Engine

Deployment Steps:

1. Push project to GitHub
2. Create IBM Cloud Application
3. Install dependencies
4. Deploy Flask application
5. Access public deployment URL

---

# 🔁 Run the Project

Install requirements

```bash
pip install -r requirements.txt
```

Run Flask application

```bash
python app/app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 🛠️ Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Random Forest
- Decision Tree
- KNN
- XGBoost

### Backend

- Flask

### Frontend

- HTML5
- CSS3
- Bootstrap 5

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Model Storage

- Joblib

---

# 📌 Future Enhancements

- Real-time Weather API Integration
- SMS & Email Alert System
- Flood Risk Map Visualization
- Mobile Application
- IBM Cloud Deployment
- Live Weather Dashboard

---
