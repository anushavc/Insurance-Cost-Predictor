from flask import Flask,render_template,request
import pickle
app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/form")
def form():
    return render_template('form.html')

@app.route('/result',methods=['POST'])
def insurance_cost():
    age=int(request.form['age'])
    bmi=float(request.form['bmi'])
    children=int(request.form['no_of_children'])
    sex=request.form['gender']
    smoker=request.form['smoker']
    region=request.form['region']
    r1=0
    r2=0
    r3=0
    if(region==1):
        r1=1
        r2=0
        r3=0
    elif(region==2):
        r1=0
        r2=0
        r3=0
    elif(region==3):
        r1=0
        r2=1
        r3=0
    elif(region==4):
        r1=0
        r2=0
        r3=1
    
    print(r1,r2,r3)
    filename = 'model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    result = round(float(loaded_model.predict([[age,bmi,children,sex,smoker,r1,r2,r3]])),2)
    return render_template('result.html',result=result)

if __name__=='__main__':
    app.run(debug=True)