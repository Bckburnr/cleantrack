from flask import Flask, render_template, redirect, request
from models import db, Equipment
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleantrack.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

@app.route('/')
def index():
    equipments = Equipment.query.all()
    return render_template('index.html', equipments=equipments)

@app.route('/add', methods=['POST'])
def add_equipment():
    name = request.form['name']
    due_date = request.form['due_date']
    new_item = Equipment(name=name, due_date=due_date)
    db.session.add(new_item)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
