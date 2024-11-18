# train.py
import argparse
import os
import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_absolute_error, r2_score

def model_fn(model_dir):
    """Load model from the model_dir."""
    model = xgb.Booster()
    model.load_model(os.path.join(model_dir, "xgboost-model"))
    return model

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Hyperparameters sent by the client are passed as command-line arguments to the script.
    parser.add_argument("--subsample", type=float, default=0.6)
    parser.add_argument("--n_estimators", type=int, default=200)
    parser.add_argument("--max_depth", type=int, default=5)
    parser.add_argument("--learning_rate", type=float, default=0.1)
    parser.add_argument("--colsample_bytree", type=float, default=1.0)
    parser.add_argument("--objective", type=str, default='reg:squarederror')

    # SageMaker specific arguments. Defaults are set in the environment variables.
    parser.add_argument("--model-dir", type=str, default=os.environ["SM_MODEL_DIR"])
    parser.add_argument("--train", type=str, default=os.environ["SM_CHANNEL_TRAIN"])
    parser.add_argument("--test", type=str, default=os.environ["SM_CHANNEL_TEST"])

    args = parser.parse_args()

    print("Training data path:", args.train)
    print("Testing data path:", args.test)
    print("Model directory:", args.model_dir)

    # Load the training data
    train_data_path = os.path.join(args.train, "train_data.csv")
    test_data_path = os.path.join(args.test, "test_data.csv")

    if not os.path.exists(train_data_path):
        raise FileNotFoundError(f"Training data not found at {train_data_path}")
    if not os.path.exists(test_data_path):
        raise FileNotFoundError(f"Testing data not found at {test_data_path}")

    train_data = pd.read_csv(train_data_path)
    X_train = train_data.drop(columns=["CASOS"])
    y_train = train_data["CASOS"]

    # Load the testing data
    test_data = pd.read_csv(test_data_path)
    X_test = test_data.drop(columns=["CASOS"])
    y_test = test_data["CASOS"]

    # Train the model
    model = xgb.XGBRegressor(
        subsample=args.subsample,
        n_estimators=args.n_estimators,
        max_depth=args.max_depth,
        learning_rate=args.learning_rate,
        colsample_bytree=args.colsample_bytree,
        objective=args.objective
    )

    model.fit(X_train, y_train)

    # Save the model
    model.save_model(os.path.join(args.model_dir, "xgboost-model"))

    # Evaluate the model
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"MAE: {mae}, R²: {r2}")