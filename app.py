from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import jsonify
from flask import request

app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mandeepsingh@localhost:5432/Shoes_haven_db'

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

    def __init__(self, name_ = "", price_ = 0, gender_ = "" , main_image_ = "" ,Thumb_one_ = "" , Thumb_Two_ = "", Thumb_Three_ = "" ):
        self.name = name_
        self.price = price_
        self.gender = gender_
        self.main_image = main_image_
        self.Thumb_One =Thumb_one_
        self.Thumb_Two = Thumb_Two_
        self.Thumb_Three = Thumb_Three_

@app.route('/')
def home():
    return render_template("home.html")
@app.route('/product/<int:shoe_id>', methods=['POST', 'GET'])
def product(shoe_id):
    shoe = Shoes.query.get_or_404(shoe_id)  # Fetch the shoe from the database

    # Handle the form submission for POST requests
    if request.method == "POST":
        selected_size = request.form.get("size")
        shipping_option = request.form.get("shippingOption")
        
        return jsonify({
            "message": "POST received",
            "selected_size": selected_size,
            "shipping_option": shipping_option
        })

    # Handle GET request, and render the template
    return render_template("product.html", shoe=shoe)  # Pass the shoe object to the template

     

@app.route('/productlisting')
def productlisting():
    return render_template("productlisting.html")



    return jsonify(all_shoes)


    


if __name__ == '__main__':
    app.run(debug=True)
