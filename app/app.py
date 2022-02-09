from flask import Flask,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy,sqlalchemy
from sqlalchemy import func,extract,and_

db_name='covid.db'

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Covid(db.Model):
    __tablename__='covid'
    SNo=db.Column(db.Integer,primary_key=True)
    ObservationDate=db.Column(db.Date)
    State=db.Column(db.String)
    Country=db.Column(db.String)
    LastUpdate=db.Column(db.String)
    Confirmed=db.Column(db.Integer)
    Deaths=db.Column(db.Integer)
    Recovered=db.Column(db.Integer)


test=Covid.query.filter(and_()).all()

for i in test:
    print(i.LastUpdate)

# @app.route('/')
# def welcome():
#     return "Welcome to HomePage. Query Results based on Country name and MMYYYY"

# @app.route('/covid/<country>/<ym>',methods=["GET"])
# def covid(country,ym):
#     try:
#         covid=Covid.query.filter(extract('year',Covid.ObservationDate)==int(ym[-4:])).filter(extract('month',Covid.ObservationDate)==int(ym[0:2]))
#         # covid=Covid.query.filter(func.lower(Covid.Country)==str.lower(country) and Covid.ObservationDate[0:2]+Covid.ObservationDate[-4:]==ym).all()
#         return render_template('test.html',covid=covid)

#     except Exception as e:
#         error_text = "<p>The error:<br>" + str(e) + "</p>"
#         hed = '<h1>Something is broken.</h1>'
#         return hed + error_text

# if __name__=='__main__':
#     app.run(host="0.0.0.0",debug=True)