<h1 align="center">🏠 House Price Prediction</h1>

<p align="center">
  <b>Machine Learning Web Application using Multiple Linear Regression</b>
</p>

<h2>📌 About the Project</h2>

<p>
This project is a Machine Learning based House Price Prediction web application.
It uses <b>Multiple Linear Regression</b> to predict house prices from input features.
</p>

<p>
The project contains both a Machine Learning backend and an HTML frontend.
The backend is developed using Flask and the trained model is deployed on Render.
</p>

<hr>

<h2>🔄 Machine Learning Workflow</h2>

<pre>
Dataset
   ↓
Data Preprocessing
   ↓
City Mapping
   ↓
Country Mapping
   ↓
Date Processing
   ↓
X and y Separation
   ↓
Train-Test Split
   ↓
Multiple Linear Regression
   ↓
Model Training
   ↓
Training Evaluation
   ↓
Testing Evaluation
   ↓
Save Model
   ↓
Load Model
   ↓
Custom Test Point Prediction
   ↓
Flask Backend
   ↓
HTML Frontend
   ↓
Render Deployment
</pre>

<hr>

<h2>🛠️ Technologies Used</h2>

<ul>
  <li>Python</li>
  <li>Pandas</li>
  <li>NumPy</li>
  <li>Scikit-learn</li>
  <li>Flask</li>
  <li>HTML</li>
  <li>CSS</li>
  <li>Pickle</li>
  <li>Git</li>
  <li>GitHub</li>
  <li>Render</li>
</ul>

<hr>

<h2>📊 Machine Learning Model</h2>

<p>
The project uses <b>Multiple Linear Regression</b>.
</p>

<p>The general equation is:</p>

<pre>
y = m1x1 + m2x2 + m3x3 + ... + mnxn + c
</pre>

<ul>
  <li><b>y</b> = Predicted house price</li>
  <li><b>x1, x2, ..., xn</b> = Input features</li>
  <li><b>m1, m2, ..., mn</b> = Regression coefficients</li>
  <li><b>c</b> = Intercept</li>
</ul>

<hr>

<h2>🔢 Data Preprocessing</h2>

<h3>City Mapping</h3>

<p>
City categorical values are converted into numerical values using the
<code>map()</code> function.
</p>

<pre>
City A → 0
City B → 1
City C → 2
</pre>

<h3>Country Mapping</h3>

<p>
Country categorical values are also converted into numerical values.
</p>

<pre>
Country A → 0
Country B → 1
Country C → 2
</pre>

<hr>

<h2>📅 Date Processing</h2>

<p>
The date column is processed into numerical date components such as:
</p>

<ul>
  <li>Year</li>
  <li>Month</li>
  <li>Day</li>
</ul>

<p>For example:</p>

<pre>
2026-08-20

Year  = 2026
Month = 8
Day   = 20
</pre>

<hr>

<h2>🎯 Independent and Dependent Variables</h2>

<p>
The independent/input variables are stored in <code>X</code>.
</p>

<pre>
X = df.iloc[:, :-1]
</pre>

<p>
The dependent/target variable is stored in <code>y</code>.
</p>

<pre>
y = df.iloc[:, -1]
</pre>

<pre>
X → Independent Variables / Input Features

y → Dependent Variable / Target
</pre>

<hr>

<h2>✂️ Train-Test Split</h2>

<p>
The dataset is divided into training and testing data.
</p>

<pre>
X_train, X_test, y_train, y_test =
train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
</pre>

<p>
The training data is used to train the model and the testing data is used
to evaluate the model.
</p>

<hr>

<h2>🤖 Model Training</h2>

<pre>
from sklearn.linear_model import LinearRegression

reg = LinearRegression()

reg.fit(X_train, y_train)
</pre>

<h3>Regression Coefficients</h3>

<pre>
reg.coef_
</pre>

<h3>Intercept</h3>

<pre>
reg.intercept_
</pre>

<hr>

<h2>📈 Model Evaluation</h2>

<h3>Training Prediction</h3>

<pre>
train_prediction = reg.predict(X_train)
</pre>

<h3>Testing Prediction</h3>

<pre>
test_prediction = reg.predict(X_test)
</pre>

<hr>

<h2>📉 Root Mean Square Error (RMSE)</h2>

<p>
RMSE measures the difference between actual values and predicted values.
</p>

<p><b>Formula:</b></p>

<pre>
RMSE = √[ Σ(yi - ŷi)² / n ]
</pre>

<p>Where:</p>

<ul>
  <li><b>yi</b> = Actual value</li>
  <li><b>ŷi</b> = Predicted value</li>
  <li><b>n</b> = Number of observations</li>
</ul>

<p>
A lower RMSE generally indicates better prediction performance.
</p>

<hr>

<h2>📊 R² Score</h2>

<p>
R² score measures how well the regression model explains the variation
in the target variable.
</p>

<p><b>Formula:</b></p>

<pre>
R² = 1 - [ Σ(yi - ŷi)² / Σ(yi - ȳ)² ]
</pre>

<p>Python implementation:</p>

<pre>
from sklearn.metrics import r2_score

r2 = r2_score(y_test, test_prediction)
</pre>

<hr>

<h2>📋 Performance Metrics</h2>

<ul>
  <li>Training Loss</li>
  <li>Test Loss</li>
  <li>Test R² Score</li>
  <li>Root Mean Square Error (RMSE)</li>
</ul>

<p>
For regression problems, R² score is used as the main goodness-of-fit
metric rather than classification accuracy.
</p>

<hr>

<h2>💾 Model Saving</h2>

<p>
The trained model is saved using Python's <code>pickle</code> module.
</p>

<pre>
import pickle

with open("MLR.pkl", "wb") as file:
    pickle.dump(reg, file)
</pre>

<hr>

<h2>📂 Model Loading</h2>

<p>
The saved model can be loaded and used for prediction without training
the model again.
</p>

<pre>
with open("MLR.pkl", "rb") as file:
    model = pickle.load(file)
</pre>

<hr>

<h2>🧪 Custom Prediction</h2>

<p>
The application allows users to enter their own values through the
frontend and predict a house price using the trained model.
</p>

<pre>
prediction = model.predict(test_data)
</pre>

<hr>

<h2>🌐 Flask Backend</h2>

<p>
Flask is used to connect the Machine Learning model with the HTML
frontend.
</p>

<pre>
User
  ↓
HTML Form
  ↓
Flask Backend
  ↓
Machine Learning Model
  ↓
Prediction
  ↓
HTML Result
</pre>

<hr>

<h2>📁 Project Structure</h2>

<pre>
MLR M-1/
│
├── app.py
├── model.py
├── house price.csv
├── MLR.pkl
├── requirements.txt
├── README.md
│
└── templates/
    └── index.html
</pre>

<hr>

<h2>💻 Run Locally</h2>

<h3>1. Clone the Repository</h3>

<pre>
git clone YOUR_GITHUB_REPOSITORY_URL
</pre>

<h3>2. Enter the Project Folder</h3>

<pre>
cd MLR-M-1
</pre>

<h3>3. Create Virtual Environment</h3>

<pre>
python -m venv .venv
</pre>

<h3>4. Activate Virtual Environment</h3>

<p>Windows:</p>

<pre>
.venv\Scripts\activate
</pre>

<h3>5. Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<h3>6. Run the Application</h3>

<pre>
python app.py
</pre>

<p>Open:</p>

<pre>
http://127.0.0.1:5000
</pre>

<hr>

<h2>☁️ Render Deployment</h2>

<p>
The application is deployed using <b>Render</b>.
</p>

<p>
<a href="YOUR_RENDER_LINK_HERE">
  🚀 <b>Open Live Render Application</b>
</a>
</p>

<h3>Render Start Command</h3>

<pre>
gunicorn app:app
</pre>

<hr>

<h2>📦 Requirements</h2>

<pre>
Flask
pandas
numpy
scikit-learn
matplotlib
gunicorn
</pre>

<hr>

<h2>⭐ Features</h2>

<ul>
  <li>Multiple Linear Regression</li>
  <li>City and Country categorical mapping</li>
  <li>Date preprocessing</li>
  <li>Train-Test Split</li>
  <li>Training loss calculation</li>
  <li>Testing loss calculation</li>
  <li>R² score calculation</li>
  <li>RMSE calculation</li>
  <li>Model saving using Pickle</li>
  <li>Model loading</li>
  <li>Custom prediction</li>
  <li>Flask backend</li>
  <li>HTML frontend</li>
  <li>Render deployment</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>

<p>
<b>Anuharika</b>
</p>

<h2>🔗 Project Links</h2>

<h3>🌐 Deployment</h3>

<p>
    <a href=" https://mlr-houseprice-project1-1.onrender.com">
        Render Deployment
    </a>
</p>

<h3>💼 LinkedIn</h3>

<p>
    <a href="https://www.linkedin.com/in/anuharika/">
        LinkedIn Profile
    </a>
</p>

<hr>

<h2>⭐ Support</h2>

<p>
If you found this project useful, please consider giving the repository
a ⭐ on GitHub.
</p>
