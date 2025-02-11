from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods= ['GET', 'POST']) # What methods are needed?
def home():
	try:
		if request.method =='GET':
			return render_template('home.html')
		else:
			name=str(request.form["name"])
			age=int(request.form["age"])
			message=str(request.form["message"])
			login_session["name"]=name
			login_session["age"]=age
			login_session["message"]=message
			return render_template('thanks.html', n=name, a=age, m=message)
	except:
		
			return render_template('error.html')


	


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', n=login_session["name"], a=login_session["age"], m=login_session["message"]) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)


	