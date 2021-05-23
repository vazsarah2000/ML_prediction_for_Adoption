from flask import Flask , render_template,request
import joblib
import save_data
import TableToCsv
import split_csv
import pandas as pd
import os


app =  Flask(__name__)

@app.route('/')
def Adoption_survey():
    return render_template('Adoption_survey.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    os.remove("C:/Users/Sara/PycharmProjects/Adoption_survey/templates/Adoption_data.csv")
    os.remove("C:/Users/Sara/PycharmProjects/Adoption_survey/common.csv")
    os.remove("C:/Users/Sara/PycharmProjects/Adoption_survey/child.csv")
    os.remove("C:/Users/Sara/PycharmProjects/Adoption_survey/adolescent.csv")
    if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)


@app.route('/save')
def save():
     return  save_data.save()

@app.route('/table')
def convert():
    return TableToCsv.conversion()

@app.route('/split')
def split():
    return split_csv.split()

@app.route('/pickle1')
def model1():
    load_model_1 = joblib.load(open('C:/Users/Sara/PycharmProjects/Adoption_survey/venv/saved_model1.pkl', 'rb'))
    # Make prediction using model loaded from disk as per the data.
    common = pd.read_csv(r'C:/Users/Sara/PycharmProjects/Adoption_survey/common.csv', encoding="latin1")
    predict = load_model_1.predict(common)
    prediction=str(predict.item(0))
    return prediction


@app.route('/pickle2')
def model2():
    load_model_2 = joblib.load(open('C:/Users/Sara/PycharmProjects/Adoption_survey/venv/saved_model2.pkl', 'rb'))
    # Make prediction using model loaded from disk as per the data.
    child = pd.read_csv(r'C:/Users/Sara/PycharmProjects/Adoption_survey/child.csv', encoding="latin1")
    predict = load_model_2.predict(child)
    prediction = str(predict.item(0))
    return prediction

@app.route('/pickle3')
def model3():
    load_model_3 = joblib.load(open('C:/Users/Sara/PycharmProjects/Adoption_survey/venv/saved_model3.pkl', 'rb'))
    # Make prediction using model loaded from disk as per the data.
    adolescent = pd.read_csv(r'C:/Users/Sara/PycharmProjects/Adoption_survey/adolescent.csv', encoding="latin1")
    predict = load_model_3.predict(adolescent)
    prediction = str(predict.item(0))
    return prediction

@app.route('/model')
def output():
    final=model1()+model2()+model3()
    if final=="111":
        statement="<h1>Congrats!,Child or Adolescent you would make a good parent for both ,Good Luck!</h1>"
    elif final =="110":
        statement = "<h1>Your compatiblity signals for a healthy bond with a child,Good Luck!</h1>"
    elif final =="101":
        statement="<h1>Your compatibility and Maturity would help shape a good Teen</h1>"
    elif final=="000":
        statement ="<h1>Sorry! your preparation points towards a poor knowledge and effort to deal with adoptees. Not Eligible for any</h1>"
    else:
        statement="<h1>Adoption is a life changing and serious decision and so should the effort and undersatnding be when it comes to it , Please consider researching and conselling on adoption , Currently Not Eligible!</h1>"
    return statement

if __name__=='__main__':
    app.run(debug=True)