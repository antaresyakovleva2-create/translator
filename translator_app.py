import streamlit as st
import os

st.title("🚀 翻译器测试版")

# 先测试基础功能
name = st.text_input("输入测试文本:")
if name:
    st.write(f"你输入了: {name}")

# 测试openai导入
try:
    from openai import OpenAI
    st.success("✅ openai 包导入成功！")
    
    # 测试环境变量
    if "OPENAI_API_KEY" in os.environ:
        st.success("✅ 环境变量检测成功！")
    else:
        st.warning("⚠️ 环境变量未设置")
        
except ImportError:
    st.error("❌ openai 包导入失败")
