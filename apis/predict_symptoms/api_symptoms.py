import boto3
import os
import tarfile
import tempfile
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import xgboost as xgb

app = Flask(__name__)
CORS(app)

# Retrieve AWS region from environment variable
aws_region = os.getenv("AWS_DEFAULT_REGION")

# Initialize AWS S3 client with region
s3_client = boto3.client("s3", region_name=aws_region)


def modelo_s3(access_point_arn, model_key):
    try:
        print("Iniciando download do S3...")
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        )
        response = s3_client.get_object(Bucket=access_point_arn, Key=model_key)
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(response["Body"].read())
            tmp_file.flush()
            tmp_file_path = tmp_file.name

        with tarfile.open(tmp_file_path, "r:gz") as tar:
            model_file = tar.extractfile("model.xgb")
            if model_file is not None:
                with tempfile.NamedTemporaryFile(delete=False) as tmp_model_file:
                    tmp_model_file.write(model_file.read())
                    tmp_model_file.flush()
                    return tmp_model_file.name
    except s3_client.exceptions.NoSuchBucket as e:
        print(f"Erro: O bucket especificado não existe. {e}")
        raise e
    except Exception as e:
        print(f"Erro ao carregar o modelo do S3: {e}")
        raise e


# Access Point ARN and model key
access_point_arn = "arn:aws:s3:us-east-1:590183838859:accesspoint/symptoms"
model_key = "sagemaker-xgboost-2024-11-04-23-55-27-440/output/model.tar.gz"

try:
    # Load model from S3
    model_path = modelo_s3(access_point_arn, model_key)
    if model_path is None:
        raise Exception("Falha ao carregar o modelo do S3")

    # Load the model into XGBoost
    global xgb_model
    xgb_model = xgb.Booster()
    xgb_model.load_model(model_path)

    # Clean up temporary file
    os.unlink(model_path)

except Exception as e:
    print(f"Error loading model: {e}")
    raise e


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict_symptoms", methods=["POST"])
def predict():
    try:
        data = request.json
        print(f"Received data: {data}")

        # Map received data to expected DataFrame format
        df = pd.DataFrame(
            [
                {
                    "FEBRE": int(data["febre"]),
                    "MIALGIA": int(data["dor_corpo"]),
                    "CEFALEIA": int(data["dor_cabeca"]),
                    "EXANTEMA": int(data["erupcao"]),
                    "VOMITO": int(data["vomito"]),
                    "NAUSEA": int(data["nausea"]),
                    "DOR_COSTAS": int(data["dor_costas"]),
                    "FEBRE_MIALGIA": int(data["febre"]) * int(data["dor_corpo"]),
                    "NAUSEA_VOMITO": int(data["nausea"]) * int(data["vomito"]),
                    "FEBRE_squared": int(data["febre"]) ** 2,
                    "VOMITO_squared": int(data["vomito"]) ** 2,
                    "NAUSEA_squared": int(data["nausea"]) ** 2,
                    "MIALGIA_squared": int(data["dor_corpo"]) ** 2,
                }
            ]
        )

        print(f"DataFrame for prediction: {df}")

        # Convert DataFrame to DMatrix for prediction
        dmatrix = xgb.DMatrix(df)

        # Make prediction using the loaded model
        prediction = xgb_model.predict(dmatrix)
        print(f"Prediction: {prediction}")

        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
