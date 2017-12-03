from flask import Flask, render_template
import requests


app=Flask(__name__)
#app.debug=True

@app.route('/')
def Index():
	return  render_template('home.html')


if __name__=='__main__':
	app.run(port=8082,debug=True)