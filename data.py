import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)

n = 1200

departments = ["Cardiology","Neurology","Orthopedics","Dermatology","ENT","Gynecology"]
diagnosis = ["Heart Disease","Stroke","Fracture","Migraine","Skin Infection","PCOS","Hypertension"]
status = ["Approved","Pending","Rejected"]
gender = ["Male","Female"]

start_date = datetime(2024,1,1)

data = {
    "patient_id": [f"P{i:04d}" for i in range(1,n+1)],
    "age": np.random.randint(18,80,n),
    "gender": np.random.choice(gender,n),
    "department": np.random.choice(departments,n),
    "diagnosis": np.random.choice(diagnosis,n),
    "billing_amount": np.random.randint(2000,35000,n),
    "insurance_claim": np.random.randint(1500,30000,n),
    "status": np.random.choice(status,n)
}

df = pd.DataFrame(data)

df["admission_date"] = [start_date + timedelta(days=random.randint(0,200)) for _ in range(n)]
df["discharge_date"] = df["admission_date"] + pd.to_timedelta(np.random.randint(1,10,n), unit="D")

df.to_csv("hospital_data.csv",index=False)

print("Dataset created: hospital_data.csv")