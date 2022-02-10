from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, extract

db_name = 'covid.db'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class Covid(db.Model):
    __tablename__ = 'covid'
    SNo = db.Column(db.Integer, primary_key=True)
    ObservationDate = db.Column(db.Date)
    State = db.Column(db.String)
    Country = db.Column(db.String)
    LastUpdate = db.Column(db.String)
    Confirmed = db.Column(db.Integer)
    Deaths = db.Column(db.Integer)
    Recovered = db.Column(db.Integer)


@app.route('/')
def welcome():
    return "Welcome to HomePage. Query Results based on Country name and MMYYYY"


@app.route('/covid/<country>/<ym>', methods=["GET"])
def covid(country, ym):
    try:
        covid = Covid.query.filter(func.lower(Covid.Country) == str.lower(country), #querying for the country name
                                   extract('year', Covid.ObservationDate) == int( #querying for year and month 
                                       ym[-4:]),
                                   extract('month', Covid.ObservationDate) == int(
                                       ym[0:2])
                                   ).all()
        if covid:
            return render_template('index.html', covid=covid)
        else:
            return "Search with Available data"

    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
