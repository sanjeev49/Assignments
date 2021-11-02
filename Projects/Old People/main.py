import streamlit as st
import pandas as pd
import pickle
import shap
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
st.set_option('deprecation.showPyplotGlobalUse', False)

st.write('Prediction of **Older People Age** which are very healthy')
st.write('---')

df = pd.read_csv('full_data.csv')
x = df.drop(columns = ['Activity Label'])

y = df.iloc[:, -1]
def user_input_faetures():
    Time = st.sidebar.slider('Time', x.Time.min(), x.Time.max(), x.Time.mean())
    AccFront = st.sidebar.slider('Acc. Front', x['Acc. Front'].min(), x['Acc. Front'].max(), x['Acc. Front'].mean())
    AccVert = st.sidebar.slider('Acc. vert', x['Acc. vert'].min(), x['Acc. vert'].max(), x['Acc. vert'].mean())
    AccLat = st.sidebar.slider('Acc. Lat', x['Acc. Lat'].min(), x['Acc. Lat'].max() , x['Acc. Lat'].mean())
    idd = st.sidebar.slider('id', 1, 4, 2)
    RSSI = st.sidebar.slider('RSSI', x['RSSI'].min(), x['RSSI'].max(), x['RSSI'].mean())
    Phase = st.sidebar.slider('Phase', x['Phase'].min(), x['Phase'].max(), x['Phase'].mean())
    Freq = st.sidebar.slider('Freq', x['Freq'].min(), x['Freq'].max(),   x['Freq'].mean())
    data = {
        "Time":Time,
        "Acc. Front":AccFront,
        "Acc. Vert":AccVert,
        "Acc. Lat":AccLat,
        "id":idd,
        "RSSI":RSSI,
        "Phase":Phase,
        "Freq":Freq
        
    }
    features = pd.DataFrame(data, index=[0])
    return features
    
    

rs =  user_input_faetures()

st.header('Specified Input Parameters')
st.write(rs)
st.write('----')

# Our model
model = pickle.load(open('logistic_b.pkl','rb'))
sc = StandardScaler()
sc.fit_transform(x)
y_pred = model.predict(sc.transform(rs))

# Now we will show the prediction

st.write("Prediction of Activity")
st.write((y_pred))
st.columns(1)
st.write('---')

# Feature importance using shap
explainer = shap
st.write('Feature importance using shap')

