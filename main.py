

from fastapi import FastAPI,HTTPException
import pandas as pd
from typing import Optional
from enum import Enum

app = FastAPI(
    title="benchmarksAPI",
    version="0.2.0",
    description="The BenchmarksAPI is a tool for measuring the performance of web frameworks. Using this API, users can obtain data on the performance of various web frameworks under various workloads, including JSON serialization, single and multiple database queries, rendering a list of fortunes, updating a database record, and rendering a simple plaintext message. These measurements can be useful for developers looking to choose a web framework for their application, as well as for comparing the performance of different frameworks."
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

class Column(Enum):
    Framework = "framework"
    Json = "json-serialization"
    Single = "single-query"
    Multi = "multiple-query"
    Fortunes = "fortunes"
    Updates = "updates"
    Plaintext = "plaintext"
    Weighted = "weighted"
    Year = "year"

@app.get('/sort/{column}')
async def sort_by_column(column:Column,asce:bool=True):
    df = pd.read_csv('frameworks.csv')
    if column.value not in list(df.columns.values):
        raise HTTPException(status_code=400,detail="Unrecognized key.")
    df = df.sort_values(by=column.value,ascending=asce)
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

@app.get('/{framework}/{column}')
async def find_one_and_sort(framework:str,column:Column,asce:bool=True):
    df = pd.read_csv('frameworks.csv')
    df = df.query(f"framework == '{framework}'")
    if column.value not in list(df.columns.values):
        raise HTTPException(status_code=400,detail="Unrecognized key.")
    df = df.sort_values(by=column.value,ascending=asce)
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
