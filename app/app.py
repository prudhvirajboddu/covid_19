from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import sqlite3

db_name='covid.db'

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Covid(db.Model):
    __tablename__='covid'
    SNo=db.Column(db.Integer,primary_key=True)
    ObservationDate=db.Column(db.String)
    State=db.Column(db.String)
    Country=db.Column(db.String)
    LastUpdate=db.Column(db.String)
    Confirmed=db.Column(db.Integer)
    Deaths=db.Column(db.Integer)
    Recovered=db.Column(db.Integer)



# @app.route('/')
# @app.route('/covid')
# def covid():
#     covid,fields = execute_sql(
#         'SELECT ObservationDate , State , Country , Confirmed , Deaths  FROM covid '
#         )
#     # print(covid)
#     # return jsonify(Response(json.dumps(covid),mimetype='application/json'))
#     # return None
#     column_list = []
#     for i in fields:
#         column_list.append(i[0])
#     print("print final colume_list",column_list)

#     jsonData_list = []

#     for row in covid:
#         data_dict = {}
#         for i in range(len(column_list)):
#             data_dict[column_list[i]] = row[i]
#         jsonData_list.append(data_dict)
#     # print(data_dict)
#     return jsonify({'covid': jsonData_list})


@app.route('/')
def covid():
    try:
        covid=Covid.query.filter_by().all()
        c_text='<ul>'
        for virus in covid:
            c_text+='<li>' + str(virus.State) + ',' + str(virus.Country) + '</li>'
        c_text+='</ul>'
        return c_text
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)