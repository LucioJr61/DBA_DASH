import streamlit as st
import plotly.express as px
from db import run_query
import queries as q

st.set_page_config(page_title="Dashboard SQL Server", layout="wide")
st.title("📊 Monitoramento SQL Server")

st.caption(run_query(q.VERSAO).iloc[0, 0].split("\n")[0])

col1, col2 = st.columns(2)

with col1:
    st.subheader("Tamanho dos bancos (MB)")
    df = run_query(q.TAMANHO_BANCOS)
    st.plotly_chart(px.bar(df, x="banco", y="tamanho_mb"), use_container_width=True)

with col2:
    st.subheader("Top 10 esperas")
    st.dataframe(run_query(q.TOP_ESPERAS), use_container_width=True)

st.subheader("Sessões ativas")
st.dataframe(run_query(q.SESSOES_ATIVAS), use_container_width=True)
