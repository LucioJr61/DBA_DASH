import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

@st.cache_resource
def get_engine():
    c = st.secrets["sqlserver"]
    url = URL.create(
        "mssql+pymssql",
        username=c["username"],
        password=c["password"],
        host=c["server"],
        port=c.get("port", 1433),
        database=c["database"],
    )
    return create_engine(url)

@st.cache_data(ttl=60)
def run_query(sql: str) -> pd.DataFrame:
    with get_engine().connect() as conn:
        return pd.read_sql(sql, conn)
