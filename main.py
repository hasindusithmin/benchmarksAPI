

from fastapi import FastAPI
import pandas as pd

app = FastAPI(
    title="benchmarksAPI"
)


@app.get('/')
async def find_all():
    df = pd.read_csv('frameworks.csv')
    FRAMEWORKS = []
    for index, row in df.iterrows():
        FRAMEWORKS.append({
            "Index":index,
            "Rank": row['Rank'],
            "Framework": row['Framework'],
            "Json-serialization": row['Json-serialization'],
            "Single-query": row['Single-query'],
            "Multiple-query": row['Multiple-query'],
            "Fortunes": row['Fortunes'],
            "Updates": row['Updates'],
            "Plaintext": row['Plaintext'],
            "Weighted": row['Weighted'],
            "Year": row['Year']
        })
    return FRAMEWORKS
