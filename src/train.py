import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import mlflow
import yaml

with open("params.yaml", "r") as f:
    config = yaml.safe_load(f)

train = pd.read_csv("data/processed/train.csv")
X = train.drop("Survived", axis=1, errors='ignore')
y = train["Survived"]

# Настройка локального лога
mlflow.set_tracking_uri("sqlite:///mlflow.db")

with mlflow.start_run():
    model = LogisticRegression(max_iter=config['train']['max_iter'])
    model.fit(X, y)
    
    # Записываем результаты в MLflow
    mlflow.log_param("max_iter", config['train']['max_iter'])
    mlflow.log_metric("accuracy", model.score(X, y))
    
    # Сохраняем модель
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
    mlflow.log_artifact("model.pkl")