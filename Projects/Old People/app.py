import streamlit as st
import pandas as pd
import numpy as nu
import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn import datasets
st.set_option('deprecation.showPyplotGlobalUse', False)

st.write("""
# Boston House Price Prediction App

This app predicts the **Boston House Price**!
""")

st.write('---')
boston = datasets.load_boston()
x = pd.DataFrame(boston.data, columns= boston.feature_names)
y = pd.DataFrame(boston.target, columns= ["MEDV"])

# Side BAr
st.sidebar.header('Specity Input Parameters')

def user_input_features():
    CRIM = st.sidebar.slider('CRIM', x.CRIM.min(), x.CRIM.max(), x.CRIM.mean())
    ZN=  st.sidebar.slider('ZN', x.ZN.min(), x.ZN.max(), x.ZN.mean())
    INDUS = st.sidebar.slider('INDUS', x.INDUS.min(), x.INDUS.max(), x.INDUS.mean())
    CHAS = st.sidebar.slider('CHAS', x.CHAS.min(), x.CHAS.max(), x.CHAS.mean())
    NOX = st.sidebar.slider('NOX', x.NOX.min(), x.NOX.max(), x.NOX.mean())
    RM = st.sidebar.slider('RM', x.RM.min(), x.RM.max(), x.RM.mean())
    AGE = st.sidebar.slider('AGE', x.AGE.min(), x.AGE.max(), x.AGE.mean())
    DIS = st.sidebar.slider('DIS', x.DIS.min(), x.DIS.max(), x.DIS.mean())
    RAD = st.sidebar.slider('RAD' , x.RAD.min(), x.RAD.max(), x.RAD.mean())
    TAX = st.sidebar.slider('TAX', x.TAX.min(), x.TAX.max(), x.TAX.mean())
    PTRATIO = st.sidebar.slider('PTRATIO', x.PTRATIO.min(), x.PTRATIO.max(), x.PTRATIO.mean())
    B = st.sidebar.slider('B', x.B.min(), x.B.max(), x.B.mean())
    LSTAT = st.sidebar.slider('LSTAT', x.LSTAT.min(), x.LSTAT.min() , x.LSTAT.mean())
    data = {'CRIM':CRIM,
           'ZN':ZN,
           'INDUS':INDUS,
           'CHAS':CHAS,
           'NOX':NOX,
           'RM':RM,
           'AGE':AGE,
           'DIS':DIS,
           'RAD':RAD,
           'TAX':TAX,
           'PTRATIO':PTRATIO,
           'B':B,
           'LSTAT':LSTAT}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# Main Panel
st.header('Specified Input Parameters')
st.write(df)
st.write('----')

# Build Regression Model
model = RandomForestRegressor()
model.fit(x,y)
# Apply model to make prediction
prediction = model.predict(df)
st.header('Prediction of MEDV')
st.write(prediction)
st.write('---')

# explaining prediction value provided by shap library
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(x)

st.header('Feature Importance')
st.title('Feature importance based on SHAP values.')
shap.summary_plot(shap_values, x)
st.pyplot(bbox_inches='tight')
st.write('---')

plt.title('Feature importance based on SHAP value (Bar)')
shap.summary_plot(shap_values, x, plot_type='bar')
st.pyplot(bbox_inches='tight')