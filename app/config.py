import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "your_default_secret_key"
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_SESSION_TOKEN = os.environ.get("AWS_SESSION_TOKEN")
    AWS_DEFAULT_REGION = os.environ.get("AWS_DEFAULT_REGION", "us-east-1")
