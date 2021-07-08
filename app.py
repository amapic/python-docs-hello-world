from flask import Flask, jsonify

@app.route('/a')
def meteo():
	print('ee')
	return "hello"
