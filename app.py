from flask import Flask,render_template,jsonify
from random import sample
app = Flask(__name__)


@app.route('/')
def index():
    return "please visit other routes i have created. Regards, Raghav."


@app.route('/overview')
def overview():

    data1 = {
        "1 Jan 2015":17325,
        "1 Jan 2016":16325,
        "1 Jan 2017":18325,
        "1 Jan 2018":19325,        
        "1 Jan 2019":17456,
    }
    data2 = {
        "1 Jan 2015": 55000,
        "1 Jan 2016": 22000,
        "1 Jan 2017": 11000,
        "1 Jan 2018": 44000,
        "1 Jan 2019": 33000,
        "1 Jan 2020": 10000,

    }
    return render_template('index1.html',data1=data1,data2=data2)

@app.route('/realtime')
def realtime():

    data1 = {
        "raghav":49,
        "rohit":78,
        "rachit":90,
        "pooja":52
    }
    data2 = {
        "raghav":49,
        "rohit":67,
        "rachit":90,
        "pooja":52
    }

    data3 ={
        "Organic":38,
        "Direct":8,
        "Paid":12,
        "Referral":7
    } 
    return render_template('index2.html',data1=data1,data2=data2,data3=data3)



@app.route('/data')
def data():

    return jsonify({"results":sample(range(1,10),5)})

if __name__ == '__main__':
    app.run(debug=True)