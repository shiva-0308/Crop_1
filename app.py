from flask import Flask, render_template,jsonify,request
import pickle

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/prediction',methods = ['GET','POST'])
def prediction():
    if request.method=='POST':
        N = request.form.get('nitrogen')
        P = request.form.get('phosphorus')
        K = request.form.get('potassium')
        T = request.form.get('temperature')
        H = request.form.get('humidity')
        PH = request.form.get('ph')
        R = request.form.get('rainfall')
        print(N,P,K,T,H,PH,R)
        with open('model.pkl','rb') as model_file:
            mlmodel = pickle.load(model_file)
        res =  mlmodel.predict([[float(N),float(P),float(K),float(T),float(H),float(PH),float(R)]])
        print(res)
        return jsonify({"result":str(res[0])})
    else:
        return render_template('prediction.html')    
    return render_template('prediction.html')

@app.route('/showdata')
def showdata():
    return render_template('showdata.html')
if __name__=='__main__':
    app.run()
