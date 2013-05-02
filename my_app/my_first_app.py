# This is whre you can start you python file for your week1 web app
# Name: Kelly Chiang


#unsafe for practical use 
import flask, flask.views
import os #specifically do OS things, cant import things after eval? 
app = flask.Flask(__name__)

app.secret_key = "123piggypig@" #need secret key to code the data between user and webserver browsers, make the key hard to crack

#/users/ #each of these are separate views, which can handle multiple routes
#/remote/
#/charts/

users = {'kelly':'cosmoseesyou2'} #dictionary database of username and passwords

class Main(flask.views.MethodView): #new view called main, changed following view to "remote"
	def get(self):
		return flask.render_template('index.html')

	def post(self):
		required = ['username', 'passwd']
		for r in required:
			if r not in flask.request.form:
				flask.flash("ERROR: {0} is required.".format(r))
				return flask.redirect(flask.url_for('index')) #return back to indexhtml
		#flask.request.form[] #username and password will go ehre
		username = flask.request.form['username']
		passwd = flask.request.form['passwd']
		if username in users and users[username] == passwd: flask.session['username'] = username
		else:
			flask.flash("Username doesn't exist or incorrect password")
		return flask.redirect(flask.url_for('index')) 

class Remote(flask.views.MethodView):
	def get(self):   
		return flask.render_template('remote.html') #flask defaults to a "templates" folder, remember to create a templates folder!

	def post(self): #when you have a get, should following with post if you want something to be displayed
		result = eval(flask.request.form['expression']) #links to the HTML form where the user types into the textbox named "expression"
		flask.flash(result)
		return flask.redirect(flask.url_for('remote')) #return back to indexhtml

app.add_url_rule('/',
			view_func=Main.as_view('index'),
			methods=['GET', 'POST'])

app.add_url_rule('/remote/', #changed the route to remote to match the above class view
			view_func=Main.as_view('remote'),
			methods=['GET', 'POST']) #lets the app know youre using more views, methods is a list

app.debug = True
app.run()

