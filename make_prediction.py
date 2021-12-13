import numpy as np
import pickle

model = pickle.load(open('model.pkl','rb'))
scalerX = pickle.load(open('scalerX.pkl','rb'))
scalery = pickle.load(open('scalery.pkl','rb'))
encoder = pickle.load(open('encoder.pkl','rb'))

def make_prediction(kabupaten, proyek, tki, tka):
    encoded_kabupaten = encoder.transform([kabupaten])
    predictor = np.array([encoded_kabupaten[0], proyek, tki, tka])
    predictor = predictor.reshape(1,-1)
    X = scalerX.transform(predictor)
    
    y_predict = model.predict(X)
    y_predict = scalery.inverse_transform(y_predict.reshape(-1,1))
    return round(y_predict[0][0],2)