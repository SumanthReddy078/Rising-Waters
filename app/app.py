import sys
from pathlib import Path

# ============================================================
# Add Project Root Directory to Python Path
# ============================================================
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# ============================================================
# Imports
# ============================================================
from flask import Flask, render_template, request
from src.predictor import predict_flood

# ============================================================
# Flask Application Configuration
# ============================================================
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

app.config["SECRET_KEY"] = "rising_waters_project"

# ============================================================
# Home Page
# ============================================================
@app.route("/")
def home():
    """
    Display the Landing Page.
    """
    return render_template(
        "index.html",
        title="Rising Waters"
    )


# ============================================================
# Prediction Input Page
# ============================================================
@app.route("/predict", methods=["GET"])
def predict_page():
    """
    Display the Weather Parameter Input Form.
    """
    return render_template(
        "predict.html",
        title="Flood Prediction"
    )


# ============================================================
# Prediction Route
# ============================================================
@app.route("/predict", methods=["POST"])
def predict_result():
    """
    Receive user input, perform flood prediction,
    and display the prediction result.
    """

    try:

        # ----------------------------------------------------
        # Read User Inputs
        # ----------------------------------------------------
        temp = float(request.form["temp"])
        humidity = float(request.form["humidity"])
        cloud_cover = float(request.form["cloud_cover"])
        annual = float(request.form["annual"])
        jan_feb = float(request.form["jan_feb"])
        mar_may = float(request.form["mar_may"])
        jun_sep = float(request.form["jun_sep"])
        oct_dec = float(request.form["oct_dec"])
        avgjune = float(request.form["avgjune"])
        sub = float(request.form["sub"])

        # ----------------------------------------------------
        # Predict Flood Risk
        # ----------------------------------------------------
        prediction = predict_flood(
            temp=temp,
            humidity=humidity,
            cloud_cover=cloud_cover,
            annual=annual,
            jan_feb=jan_feb,
            mar_may=mar_may,
            jun_sep=jun_sep,
            oct_dec=oct_dec,
            avgjune=avgjune,
            sub=sub
        )

        # ----------------------------------------------------
        # Return Prediction Result
        # ----------------------------------------------------
        if prediction == 1:

            return render_template(
                "result.html",
                title="Flood Risk Detected",
                prediction=prediction,
                alert_class="danger",
                heading="⚠ Flood Risk Detected",
                message="The Machine Learning model predicts a HIGH probability of flooding based on the provided weather parameters.",
                recommendation=[
                    "Move to a safer location if necessary.",
                    "Follow local weather advisories.",
                    "Avoid flooded roads and low-lying areas.",
                    "Keep emergency supplies ready."
                ]
            )

        else:

            return render_template(
                "result.html",
                title="No Flood Risk",
                prediction=prediction,
                alert_class="success",
                heading="✅ No Flood Risk Detected",
                message="The Machine Learning model predicts NO significant flood risk based on the provided weather parameters.",
                recommendation=[
                    "Weather conditions appear normal.",
                    "Continue monitoring local forecasts.",
                    "Stay informed during heavy rainfall seasons."
                ]
            )

    except ValueError:

        return render_template(
            "error.html",
            title="Input Error",
            error_message="Please enter valid numeric values for all weather parameters."
        )

    except Exception as e:

        print(f"\nPrediction Error: {e}\n")

        return render_template(
            "error.html",
            title="Application Error",
            error_message="Something went wrong while processing your request. Please try again."
        )


# ============================================================
# 404 Error Handler
# ============================================================
@app.errorhandler(404)
def page_not_found(error):
    """
    Handle Page Not Found Error.
    """
    return render_template(
        "error.html",
        title="404 Error",
        error_message="The page you are looking for does not exist."
    ), 404


# ============================================================
# 500 Error Handler
# ============================================================
@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle Internal Server Error.
    """
    return render_template(
        "error.html",
        title="500 Error",
        error_message="An unexpected server error occurred."
    ), 500


# ============================================================
# Run Flask Application
# ============================================================
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )