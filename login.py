from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/admin')
def adminlogin():
   return 'welcome %s. You are logged in as admin.' % name

@app.route('/success/<name>')
def guestlogin(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['user']
      passwd = request.form['passwd']
      if user == 'admin':
          if passwd == 'admin': 
            return redirect(url_for('adminlogin'))
   else:
      user = request.args.get('user')
      return redirect(url_for('guestlogin',name = user))

if __name__ == '__main__':
   app.run(debug = True)