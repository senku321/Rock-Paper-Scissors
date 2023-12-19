from flask import Flask,render_template,url_for
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    return render_template("main.html",title="rps")

if __name__ == "__main__":
    app.run(debug=True)