# This is whre you can start you python file for your week1 web app
# Name: Kelly Chiang


#unsafe for practical use 
import flask, flask.views
import os #specifically do OS things, cant import things after eval? 
app = flask.Flask(__name__)

app.secret_key = "123piggypig@" #need secret key to code the data between user and webserver browsers, make the key hard to crack

class View(flask.views.MethodView):
	def get(self):   
		return flask.render_template('index.html') #flask defaults to a "templates" folder, remember to create a templates folder!

	def post(self): #when you have a get, should following with post if you want something to be displayed
		result = eval(flask.request.form['expression']) #links to the HTML form where the user types into the textbox named "expression"
		flask.flash(result)
		return self.get()

app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST']) #lets the app know youre using more views, methods is a list

app.debug = True
app.run()

