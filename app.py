from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# ==========================================
# Load trained model
# ==========================================

try:

    with open("MLR.pkl", "rb") as file:
        model = pickle.load(file)

    print("Model loaded successfully")

except Exception as e:

    model = None
    print("Error loading model:", e)


# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ==========================================
# Prediction
# ==========================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # ======================================
        # Get values from HTML
        # ======================================

        year = int(
            request.form["year"]
        )

        month = int(
            request.form["month"]
        )

        day = int(
            request.form["day"]
        )

        bedrooms = float(
            request.form["bedrooms"]
        )

        bathrooms = float(
            request.form["bathrooms"]
        )

        sqft_living = float(
            request.form["sqft_living"]
        )

        sqft_lot = float(
            request.form["sqft_lot"]
        )

        floors = float(
            request.form["floors"]
        )

        waterfront = float(
            request.form["waterfront"]
        )

        view = float(
            request.form["view"]
        )

        condition = float(
            request.form["condition"]
        )

        sqft_above = float(
            request.form["sqft_above"]
        )

        sqft_basement = float(
            request.form["sqft_basement"]
        )

        yr_built = int(
            request.form["yr_built"]
        )

        yr_renovated = int(
            request.form["yr_renovated"]
        )

        city = int(
            request.form["city"]
        )

        country = int(
            request.form["country"]
        )


        # ======================================
        # Create 17 features
        # SAME ORDER AS model.py
        # ======================================

        test_point = np.array([

            [
                year,
                month,
                day,
                bedrooms,
                bathrooms,
                sqft_living,
                sqft_lot,
                floors,
                waterfront,
                view,
                condition,
                sqft_above,
                sqft_basement,
                yr_built,
                yr_renovated,
                city,
                country
            ]

        ])


        # ======================================
        # Prediction
        # ======================================

        prediction = model.predict(
            test_point
        )


        predicted_price = round(
            prediction[0],
            2
        )


        # ======================================
        # Send result to HTML
        # ======================================

        return render_template(
            "index.html",
            prediction=predicted_price
        )


    except Exception as e:

        return render_template(
            "index.html",
            error=str(e)
        )


# ==========================================
# Run Flask
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )