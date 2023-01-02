

from fastapi import FastAPI,HTTPException
import pandas as pd
from typing import Optional

app = FastAPI(
    title="benchmarksAPI"
)


@app.get('/')
async def find_all():
    df = pd.read_csv('frameworks.csv')
    frameworkS = []
    for id, row in df.iterrows():
        frameworkS.append({
            "id":id,
            "rank": row['rank'],
            "framework": row['framework'],
            "json-serialization": row['json-serialization'],
            "single-query": row['single-query'],
            "multiple-query": row['multiple-query'],
            "fortunes": row['fortunes'],
            "updates": row['updates'],
            "plaintext": row['plaintext'],
            "weighted": row['weighted'],
            "year": row['year']
        })
    return frameworkS

@app.get('/{framework}')
async def find_one(framework:str,year:Optional[int]=None):
    df = pd.read_csv('frameworks.csv')
    df = df.query(f"framework == '{framework}'")
    if year:
        df = df.query(f"framework == '{framework}' & year == {year}")
    frameworks = []
    for id, row in df.iterrows():
        frameworks.append({
            "id":id,
            "rank": row['rank'],
            "framework": row['framework'],
            "json-serialization": row['json-serialization'],
            "single-query": row['single-query'],
            "multiple-query": row['multiple-query'],
            "fortunes": row['fortunes'],
            "updates": row['updates'],
            "plaintext": row['plaintext'],
            "weighted": row['weighted'],
            "year": row['year']
        })
    return frameworks

@app.get('/sort/{column}')
async def sort_by_column(column:str,asce:bool=True):
    df = pd.read_csv('frameworks.csv')
    if column not in list(df.columns.values):
        raise HTTPException(status_code=400,detail="Unrecognized key.")
    df = df.sort_values(by=column,ascending=asce)
    frameworks = []
    for id, row in df.iterrows():
        frameworks.append({
            "id":id,
            "rank": row['rank'],
            "framework": row['framework'],
            "json-serialization": row['json-serialization'],
            "single-query": row['single-query'],
            "multiple-query": row['multiple-query'],
            "fortunes": row['fortunes'],
            "updates": row['updates'],
            "plaintext": row['plaintext'],
            "weighted": row['weighted'],
            "year": row['year']
        })
    return frameworks

