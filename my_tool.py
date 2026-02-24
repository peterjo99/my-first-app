import streamlit as st
import requests

st.title("💰 极简汇率转换工具")

# 侧边栏：输入美金金额
usd_amount = st.number_input("请输入美金金额 (USD):", value=100.0)

# 实时获取汇率（使用一个免费接口）
try:
    response = requests.get("https://open.er-api.com/v6/latest/USD")
    rate = response.json()["rates"]["CNY"]
    cny_amount = usd_amount * rate
    
    st.metric(label="当前美金/人民币汇率", value=f"{rate:.2f}")
    st.success(f"换算结果：{usd_amount} USD = {cny_amount:.2f} CNY")
except:
    st.error("无法获取实时数据")