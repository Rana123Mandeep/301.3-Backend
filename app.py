from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)  


db = SQLAlchemy()
db.init_app(app)
migrate=Migrate(app, db)

class Shoes(db.Model):

    __tablename__ = "Shoes"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    main_image = db.Column(db.String(50), nullable=False)
    Thumb_One =  db.Column(db.String(50), nullable=False)
    Thumb_Two =  db.Column(db.String(50), nullable=False)
    Thumb_Three =  db.Column(db.String(50), nullable=False)

    



@app.route('/Make_Shoes')
def make_shoes():

    new_shoe = Shoes(name = "Nike", price = 50, gender ="Male", main_image = "test.img", Thumb_One = "test.img",Thumb_Two = "test.img", Thumb_Three = "test.img")
 

    try:
            db.session.add(new_shoe)
            db.session.commit()
    except:
            return "There was an error adding the order"
       


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/product')
def product():
    return render_template("product.html")

@app.route('/productlisting')
def productlisting():
    return render_template("productlisting.html")


if __name__ == '__main__':
    app.run(debug=True)