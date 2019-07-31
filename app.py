from flask import Flask, render_template
app = Flask(__name__)
food = "water"

@app.route('/')
def home_page():
    return render_template(
    	"index.html",  food = "milk")

if __name__ == '__main__':
   app.run(debug = True)
