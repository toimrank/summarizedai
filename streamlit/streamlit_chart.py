import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

df = pd.read_excel("Project-Management-Sample-Data.xlsx", 
        sheet_name="Project Management Data")
st.dataframe(df)

st.subheader("Project Progress")
selected_df=pd.DataFrame({
    "Project Name" : df["Project Name"],
    "Progress" : df["Progress"]
})
st.dataframe(selected_df)

st.subheader("Task Poregress")
preogress_data = df.set_index("Task Name")["Progress"]
st.bar_chart(preogress_data)

st.subheader("Days Required Per Task")
days_data=df.set_index("Task Name")["Days Required"]
st.bar_chart(days_data)

st.subheader("Number of Tasks per project")
task_project=df["Project Name"].value_counts()
st.bar_chart(task_project)


st.line_chart(df["Progress"])
st.area_chart(preogress_data)
