import pandas as pd
from sklearn.model_selection import train_test_split
import yaml
import os

# Читаем параметры из params.yaml
with open("params.yaml", "r") as f:
    config = yaml.safe_load(f)

# Читаем данные, за которыми следит DVC
df = pd.read_csv("data/raw/data.csv")
df = df.select_dtypes(include=['number']).dropna() # Оставляем только числа

# Делим на train и test
train, test = train_test_split(df, test_size=config['prepare']['split_ratio'], random_state=42)

# Сохраняем результат
os.makedirs("data/processed", exist_ok=True)
train.to_csv("data/processed/train.csv", index=False)
test.to_csv("data/processed/test.csv", index=False)