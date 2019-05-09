# import datetime
# import os

# from flask import Flask, render_template, redirect, url_for
# from forms import ItemForm
# from models import Items
# from database import db_session
# app = Flask(__name__)
# app.secret_key = os.environ['APP_SECRET_KEY']

# @app.route("/", methods=('GET', 'POST'))
# def add_item():
#     form = ItemForm()
#     if form.validate_on_submit():
#         item = Items(name=form.name.data, quantity=form.quantity.data, description=form.description.data, date_added=datetime.datetime.now())
#         db_session.add(item)
#         db_session.commit()
#         return redirect(url_for('success'))
#     return render_template('index.html', form=form)

# @app.route("/success")
# def success():
#     results = []
 
#     qry = db_session.query(Items)
    
#     results = qry.all()

#     return str(results)
  

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')

import datetime
import os

from flask import Flask, render_template, redirect, url_for, jsonify
from forms import ItemForm
from models import Items
from database import db_session, engine
from sqlalchemy import inspect

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

# add on
app.config['SQLALCHEMY_ECHO'] = True

print(db_session)
@app.route("/", methods=('GET', 'POST'))
def add_item():
    form = ItemForm()

    if form.validate_on_submit():
        item = Items(name=form.name.data, quantity=form.quantity.data, description=form.description.data, date_added=datetime.datetime.now())
        db_session.add(item)
        db_session.commit()
        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route("/success",methods=('GET', 'POST'))
def success():
    results = []
    qry = db_session.query(Items)
    # results = db_session.query(Items)
    # db_session.rollback()
    results = db_session.execute(qry)
    results = [u.__dict__ for u in qry.all()]
    return str(results)

  
  

  

if __name__ == '__main__':
    ## added a field for the port here
    app.run(host='0.0.0.0', port=5001, debug=True)



    # results = jsonify(results)
    # for i in results:
    #    a= [i.name,i.quantity,i.description, i.date_added]
    #    results.append(a)

    # qry = db_session.execute("select * from items")
    # file1 = open("myFile.txt","a") 
    # file1.write(str(qry)
    # file1.write(str(results)
    # file1.close() 
    # results = db_session.execute(qry)
    # results = inspector.get_columns(items)
    
    # table = Results(results)
    # table.border = True
    # print(results)