
import joblib
import numpy as np
import pandas as pd
import redis
import json
import time

db =redis.Redis(
    host = 'redis',
    port = 6379,
    db = 0
)


DF = pd.read_csv('DataNew.csv',index_col=0)

DF = DF.drop(columns=['Text','NumberCategories'])

Y_train_columns = DF.columns

def modelFuction(text):
    
    

    m = joblib.load('ModeloSVC0.plk')

    tfidf_vectorizer = joblib.load('tfidf.plk')
    
    text_vectorizer = tfidf_vectorizer.transform([text])
    
    prediction = m.predict(text_vectorizer)
    
    re = []
   
    for pre in np.where(prediction==1)[1]:
    
        re.append(Y_train_columns[pre])

    return re



def classify_process():

    while True:

        id,job_data = db.brpop('job')

        tex = json.loads(job_data)

        p = modelFuction(tex['text'])

        dict = {
            'predictions':p
        }

        res = json.dumps(dict)

        db.set(tex['id'],res)

        time.sleep(0.05)

if __name__ == "__main__":
  
    classify_process()

