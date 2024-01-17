from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')


@app.route("/order",methods=['POST'])
def order():
	name = request.form.get('name')
	number = request.form.get('mobile')
	dishcode = request.form.get('dishcode')
	entry = f"{name},{number},{dishcode}\n"
	with open ("order.cvs",'a') as db:
		db.write(entry)
	return """
	thanks 
	<a href="/">go back</a>
	"""
app.run(debug=True)

