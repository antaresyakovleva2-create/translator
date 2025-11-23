import os
import streamlit as st
from openai import OpenAI
from langdetect import detect

# Hugging Face环境变量读取方式
api_key = os.environ.get("")
if not api_key:
    st.error("🔑 OpenAI API key not found! Please set it in Hugging Face secrets.")
    st.stop()

client = OpenAI(api_key=api_key)

LANG_MAP = {
    "zh-cn": "Chinese",
    "en": "English",
    "ru": "Russian"
}


def translate_with_gpt(text, target_language):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system",
                 "content": f"Translate the text into {target_language} in a natural, fluent tone."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"翻译错误: {str(e)}"


st.title("Tara's Translator App 💜")

# Input box
text = st.text_area("Enter text to translate:")

if st.button("Translate"):
    if text.strip():
        try:
            detected = detect(text)
            input_lang = LANG_MAP.get(detected, "English")

            st.write(f"**Detected Language:** {input_lang}")

            targets = [lang for lang in LANG_MAP.values() if lang != input_lang]

            for target in targets:
                st.subheader(target)
                translation = translate_with_gpt(text, target)
                st.write(translation)

        except Exception as e:
            st.error(f"检测语言时出错: {str(e)}")
    else:
        st.warning("Please enter some text.")

