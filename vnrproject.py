from flask import Flask,render_template,request,redirect,session
from db import Database
app=Flask(__name__)
db=Database()
@app.route('/')
def index():
    return render_template('pwd1.html')
@app.route('/Option_selection',methods=['POST'])
def option_selection():
    option=request.form.get('option')
    if option == 'PwD':
        return render_template('registerpwd.html')
    elif option == 'Volunteer':
        return render_template('registerpwd.html')
    elif option == 'Ngo':
        return render_template('registerpwd.html',user_type=option)
    else:
        return render_template('pwd1.html',message="Select Any Option")
@app.route('/register',methods=['GET','POST'])
def register_page():
    return render_template('registerpwd.html')
@app.route('/perform_registration',methods=['POST'])
def perform_registration():
    name=request.form.get('user_name')
    email=request.form.get('user_email')
    password=request.form.get('user_password')
    response=db.insert(name,email,password)
    if response:
        return render_template('login.html',message="Logged in Successfully")
    else:
        return render_template('registerpwd.html',message="Registration Not Done,Please try again")
@app.route('/login',methods=['POST'])
def login_page():
    email=request.form.get('user_email')
    password=request.form.get('user_password')
    response=db.search(email,password)
    print('response',response)
    if response:
        return render_template('p_Dashboard.html')
    else:
        return render_template('login.html',message="Log in not done")
@app.route('/p_Dashboard',methods=['GET'])
def pwd_dashboard():
    option=request.form.get('option')
    if option in ['Pwd','Volunteer','Ngo']:
        return render_template('registerpwd.html',user_type=option)
    else:    
        return "Plzz selct one option"
@app.route('/help_request')
def help_request_page():
    return render_template('help_request.html')

        
    
                              
        
if __name__=='__main__':
    app.run(debug=True)

