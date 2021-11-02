import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)


st.write("This web app will Predict the activity of the older healty people  on the basis of some input parameters.")
st.write('---')

df = pd.read_csv('real_data.csv')
x = df.drop(columns=['Activity Label'])
y = df.iloc[:, -1]

st.header('User input')


classifer_name = st.sidebar.selectbox('Select Classifier', ('DecisionTreeClassifier','KNN','LogisticRegression','SVC','BaggingClassifier','StackingClassifier'))
st.write("Number of classes ", len(np.unique(y)))
st.sidebar.header('User input Parameters.')
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

st.header('Specified User Input Parameters')
st.write(rs)
st.write('----')

# choose model:
def get_classifier(clf_name):
    if clf_name=='LogisticRegression':
        model = pickle.load(open('logistic_wh.pkl','rb'))
    elif clf_name=='SVC':

        model = pickle.load(open('svc_wiht.pkl','rb'))
    elif clf_name == 'KNN':
        model = pickle.load(open('knn_wih.pkl','rb'))
    elif clf_name == 'BaggingClassifier':
        model = pickle.load(open('bagginwRf.pkl','rb'))
    else:
        model = pickle.load(open('Stackingclf.pkl','rb'))
    return model

# Our prediction will happen here
clf = get_classifier(classifer_name)
pred = clf.predict(rs)

# Display Our prediction
#accuracy = accuracy_score(y_test, pred)
st.write(f"classifier = {classifer_name}")
st.write('Predictoin value is..')
st.write(pred)
#st.write(f"accuracy={accuracy}")

# PLOT
# pca = PCA(2)
# x_projected = pca.fit_transform(x)
# x1 = x_projected[:, 0]
# x2 = x_projected[:,1]
# plt.scatter(x1,x2,c=y, alpha= 0.8 , cmap='viridis')
# plt.xlabel('Principal Component 1')
# plt.ylabel('Pricipal component 2')
# plt.colorbar()

# # Plt.show()
# st.pyplot()



    
