import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

st.title('🔖 Advertising Sales Predictor')

st.info('An app powered by a Machine Learning model, to forecast sales based on TV, Newspaper, and Online Advertising')

#st.write('Hello world!')
