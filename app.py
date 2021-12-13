from flask import Flask, render_template, request
from make_prediction import make_prediction

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.htm")

@app.route('/prediction', methods=["post"])
def prediction():
    if request.method == "POST":
        kabupaten = request.form["kabupaten"]
        proyek = request.form["proyek"]
        tki = request.form["tki"]
        tka = request.form["tka"]

        prediction = make_prediction(kabupaten,proyek,tki,tka)

        return render_template("index.htm", prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)