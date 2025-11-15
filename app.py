from flask import Flask,render_template,url_for,request,session,redirect
import urllib.request
from db import Database
app=Flask(__name__)
db=Database()
app.secret_key='HEllo'
@app.route('/')
def index():
    return render_template('loging.html')
@app.route('/register',methods=['GET','POST'])
def register_page():
    
    return render_template('register.html')
@app.route('/perform_registration',methods=['POST'])
def perform_registration():
    name=request.form.get('user_name')
    email=request.form.get('user_email')
    password=request.form.get('user_password')
    user_type="user"
    print(name,email,password,user_type)
    response=db.insert(name,email,password,user_type)
    if response:
        message="Registration Succesful!Please Login."
        return redirect(url_for('login_page',message=message))
    else:
        message="Email already registered,please login"
        return redirect(url_for('login_page',message=message))
@app.route('/login',methods=['POST','GET'])
def login_page():
    message1=request.args.get('message')
    print('in if')
    return render_template('loging.html',message=message1)
@app.route('/perform_login',methods=['POST','GET'])
def perform_login():
    email=request.form.get('user_email')
    password=request.form.get('user_password')
    print(email,password)
    response=db.search(email,password)
    print('response',response)
    if response:
        session['user_type']=response
        
       
        return redirect(url_for('user_dashboard'))
    else:
        message="Email not in databse.Please register"
        return redirect(url_for('re_register',message=message))
@app.route('/re_register',methods=['POST','GET'])
def re_register():
    message=request.args.get('message')
    return render_template('re-register.html',message=message)
@app.route('/user_dashboard')
def user_dashboard():
    return "Welcome "

    

if __name__=='__main__':
    app.run(debug=True)