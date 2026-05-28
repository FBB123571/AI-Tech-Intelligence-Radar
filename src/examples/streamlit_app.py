"""Streamlit 看板示例 — 与报告 §7.2 对应（PoC）"""
import streamlit as st
import requests

st.set_page_config(page_title="AI 情报雷达", layout="wide")
st.title("AI 技术情报每日初筛看板")


@st.cache_data(ttl=3600)
def fetch_data():
    response = requests.get("http://localhost:8000/api/v1/daily_insights", timeout=10)
    return response.json().get("data", [])


insights = fetch_data()

for item in insights:
    with st.expander(f"{item['title']}"):
        st.write(f"**核心创新点**：{item['innovation']}")
        st.write(f"**潜在工程价值**：{item['eng_value']}")
        st.markdown(f"[访问原始信源]({item['url']})")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("准许入选周报", key=f"pass_{item['title']}"):
                st.success("已标记为高价值，将在周五自动聚合")
        with col2:
            if st.button("忽略此项", key=f"ignore_{item['title']}"):
                st.info("已忽略，同类语义情报将被抑制")
