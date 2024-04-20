# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZjFD6SZa82j0QdXAnliZxKZoP7EAErL_
"""

import pandas as pd
import streamlit as st
import plotly.express as px

# Mount Google Drive to Colab
from google.colab import drive
drive.mount('/content/drive')

data = pd.read_csv('/content/drive/My Drive/Data_Visualization_Final/dav_dataset.csv')

# Sidebar with options
st.sidebar.title('Dashboard Pages')
page = st.sidebar.radio('Select a page', ['Exploratory Data Analysis', 'COVID-19 Impact', 'Expense Concerns'])

# Page: Exploratory Data Analysis
if page == 'Exploratory Data Analysis':
    st.header('Exploratory Data Analysis')

    # Visualization: Age Distribution
    st.subheader('Age Distribution')
    age_distribution = px.bar(data['Age_Group'].value_counts(), title='Age Distribution')
    st.plotly_chart(age_distribution)

    # Visualization: Employment Type Distribution
    st.subheader('Employment Type Distribution')
    employment_type_distribution = px.bar(data['EmploymentType'].value_counts(), title='Employment Type Distribution')
    st.plotly_chart(employment_type_distribution)

    # Visualization: Gender Distribution
    st.subheader('Gender Distribution')
    gender_distribution = px.bar(data['Gender'].value_counts(), title='Gender Distribution')
    st.plotly_chart(gender_distribution)

# Page: COVID-19 Impact
elif page == 'COVID-19 Impact':
    st.header('COVID-19 Impact Analysis')

    # Visualization: Impact of Job Loss
    st.subheader('Impact of Job Loss due to COVID-19')
    job_loss_impact = px.bar(data['JobLoss'].value_counts(), title='Impact of Job Loss due to COVID-19')
    st.plotly_chart(job_loss_impact)

    # Visualization: Income Change Distribution
    st.subheader('Distribution of Income Change due to COVID-19')
    income_change_distribution = px.bar(data['IncomeChange'].value_counts(), title='Distribution of Income Change due to COVID-19')
    st.plotly_chart(income_change_distribution)

# Page: Expense Concerns
elif page == 'Expense Concerns':
    st.header('Expense Concerns Analysis')

    # Visualization: Top Priority Expenses
    st.subheader('Top Priority Expenses')
    top_priority_expenses = px.bar(data['TopPriority'].value_counts(), title='Top Priority Expenses')
    st.plotly_chart(top_priority_expenses)

    # Visualization: Low Priority Expenses
    st.subheader('Low Priority Expenses')
    low_priority_expenses = px.bar(data['LowPriority'].value_counts(), title='Low Priority Expenses')
    st.plotly_chart(low_priority_expenses)

