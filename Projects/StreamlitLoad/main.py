import streamlit as st
from sklearn import datasets
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)


st.title('Streamlit Example')
st.write("""
# Explore different classifier
 Which one is best?
""")
select_dataset = st.sidebar.selectbox('Select Dataset', ("Iris","Breast Cancer", "Wine dataset"))

classifer_name = st.sidebar.selectbox('Select Classifier', ('KNN', 'SVM', 'RandomForest'))

def get_dataset(dataset_name):
    if dataset_name == 'Iris':
        data = datasets.load_iris()
    elif dataset_name=='Breast Cancer':
        data = datasets.load_breast_cancer()
    else:
        data = datasets.load_wine()
    x = data.data
    y = data.target
    return x,y
x, y=get_dataset(select_dataset)
st.write("Dataset of Shape: ", x.shape)
st.write("Number of classes ", len(np.unique(y)))

def add_parameter_ui(clf_name):
    params = {}
    if clf_name == 'KNN':
        k = st.sidebar.slider("K", 1,15)
        params['k'] = k
    elif clf_name=='SVM':
        c = st.sidebar.slider('C', 0.01 , 10.0)
        params['c'] = c
    else:
        max_depth = st.sidebar.slider('max_depth', 2,15)
        n_estimators = st.sidebar.slider('n_estimator', 1,100)
        params['max_depth'] = max_depth
        params['n_estimators'] = n_estimators
    return params
params = add_parameter_ui(classifer_name)

def get_classifier(clf_name, params):
    
    if clf_name == 'KNN':
        clf = KNeighborsClassifier(n_neighbors=params['k'])
        
        
    elif clf_name=='SVM':
        clf = SVC(C = params['c'])
    else:
        clf = RandomForestClassifier(n_estimators=params['n_estimators'], max_depth=params['max_depth'], random_state=1234)
    return clf

clf = get_classifier(classifer_name, params)

# classification
x_train ,x_test ,y_train ,y_test = train_test_split(x,y,test_size=0.2, random_state=1234)
clf.fit(x_train, y_train)
y_predict = clf.predict(x_test)

accuracy = accuracy_score(y_test, y_predict)
st.write(f"classifier = {classifer_name}")
st.write(f"accuracy={accuracy}")

# PLOT
pca = PCA(2)
x_projected = pca.fit_transform(x)
x1 = x_projected[:, 0]
x2 = x_projected[:,1]
plt.scatter(x1,x2,c=y, alpha= 0.8 , cmap='viridis')
plt.xlabel('Principal Component 1')
plt.ylabel('Pricipal component 2')
plt.colorbar()

# Plt.show()
st.pyplot()