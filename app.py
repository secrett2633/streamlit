import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# 한글 깨짐 방지를 위해 폰트 설정
from matplotlib import font_manager, rc
# font_path = "C:/Windows/Fonts/NGULIM.TTF"
# font = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font)

st.title("Show Sparsity")
uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)
if uploaded_files is not None:
    files = {}
    for uploaded_file in uploaded_files:
      data = pd.read_csv(uploaded_file)
      files[uploaded_file.name] = data

datas = st.multiselect(
    "Choose data", list(files)
)
if datas:
    for file in datas:
        data = files[file]
        labels = 'Sparsity', 'Data'
        explode = (0, 0.1)
        sparsity = len(data.iloc[:, 2]) / (len(data.iloc[:, 0].unique()) * len(data.iloc[:, 1].unique())) * 100
        sizes = [100 - sparsity, sparsity]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, explode=explode, autopct='%1.3f%%', startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.legend(labels, loc="best")
        st.pyplot(fig1)