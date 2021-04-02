from flask import Flask,request,jsonify
import pickle
from sklearn.linear_model import LogisticRegression
app=Flask(__name__)
@app.route("/")
def index():
    Gender=request.args['gender']
    Credit_History=request.args['credit_History']
    Marital_status=request.args['Marital_status']
    Dependents=request.args['Dependents']
    Education=request.args['Education']
    Employment=request.args['Employment']
    Income=request.args['Income']
    Total_Income=request.args['Total_Income']
    LoanAmount=request.args['LoanAmount']
    Area=request.args['Area']
    Term=request.args['Term']
    data=[[float(Gender),float(Marital_status),float(Dependents),float(Education),float(Employment),float(Credit_History),float(Income),float(Total_Income),float(LoanAmount),float(Area),float(Term)]]
    lr=pickle.load(open('Banking_loan_prediction.pickle','rb')) 
    prediction=lr.predict(data)[0]
    if prediction==1:
        return "Approved"

    elif prediction!=1:
     return "Not_Approved"
          
if __name__=='__main__':
    app.run()
      
