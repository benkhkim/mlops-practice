from fastapi import FastAPI
import uvicorn
import joblib
import numpy as np
from pydantic import BaseModel

# 1. 입력 데이터 규격 정의 (MLflow Signature 대용)
class IrisInput(BaseModel):
    features: list  # 예: [5.1, 3.5, 1.4, 0.2]

app = FastAPI()

# 2. 서버 시작 시 모델 로드 (상대 경로 주의)
model = joblib.load("models/model.pkl")

@app.get("/")
def root():
    return {"message": "Iris Classification API is running!"}

@app.post("/predict")
def predict(data: IrisInput):
    # 데이터를 모델 입력에 맞게 변환 (1, 4)
    input_data = np.array(data.features).reshape(1, -1)
    prediction = model.predict(input_data)
    
    species = ["setosa", "versicolor", "virginica"]
    return {
        "prediction": int(prediction[0]),
        "species": species[int(prediction[0])]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
