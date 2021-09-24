import numpy as np
from sklearn.linear_model import LogisticRegression

import mlflow
import mlflow.sklearn


TRACKING_URI = "http://localhost:5000/"
EXPERIMENT = "ExampleModel"

mlflow.set_tracking_uri(TRACKING_URI)
mlflow.set_experiment(EXPERIMENT)

with mlflow.start_run():
    # Data
    X = np.array([-2, -1, 0, 1, 2, 1]).reshape(-1, 1)
    y = np.array([0, 0, 1, 1, 1, 0])
    
    # Train
    params = {
        'penalty': 'l2'
    }
    lr = LogisticRegression(**params)
    lr.fit(X, y)
    
    # Score
    score = lr.score(X, y)
    mlflow.log_metric("score", score)
    mlflow.log_params(params)