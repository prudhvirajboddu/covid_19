from operator import index
from flask import Flask,request,g,render_template,json,Response,jsonify
import sqlite3
from json import dumps

from numpy import cov

db_path='db/cdata.db'
app=Flask(__name__)

def open_connection():
    connection = getattr(g, '_connection', None)
    if connection is None:
        connection = g._connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection

def execute_sql(sql, values=(), commit=False, single=False):
    connection = open_connection()
    cursor = connection.execute(sql, values)
    if commit is True:
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()
    cursor.close()
    return results

@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()

@app.route('/')
@app.route('/covid')
def covid():
    covid = execute_sql(
        'SELECT ObservationDate , State , Country , Confirmed , Deaths  FROM covid '
        )
    # print(covid)
    # return jsonify(Response(json.dumps(covid),mimetype='application/json'))
    # return None
    return dumps(covid)

if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)