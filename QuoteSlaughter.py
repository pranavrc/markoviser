from flask import *
from scrape import *
app=Flask(__name__)

@app.route("/", methods=['GET','POST'])


#def hello():
#	return render_template('index.html')

def index():
	if request.method == 'GET':
		return render_template('index.html');
	if request.method == 'POST':
		return returnmarkovised() 
#	if request.method == 'POST':
#		original1=name
#		markovised1=name
#		return render_template('index.html',original=ioriginal1,markovised=markovised1)
	

if __name__=="__main__":
	app.run(debug=True)
