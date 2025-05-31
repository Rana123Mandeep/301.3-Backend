from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import jsonify
from flask import request
from sqlalchemy import or_
from sqlalchemy import or_, cast, String
from datetime import date
from datetime import datetime, date
from decimal import Decimal
import sqlalchemy


app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mandeepsingh@localhost:5432/Shoes_haven_db'

db = SQLAlchemy()
db.init_app(app)
migrate=Migrate(app, db)

class Shoes(db.Model):

    __tablename__ = "Shoes"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    sizes = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    style = db.Column(db.String(100), nullable=False)
    brand= db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(1000), nullable=False)
    main_image = db.Column(db.String(100), nullable=False)
    Thumb_One =  db.Column(db.String(100), nullable=False)
    Thumb_Two =  db.Column(db.String(100), nullable=False)
    Thumb_Three =  db.Column(db.String(100), nullable=False)

    # def __init__(self, name_ = "", price_ = 0, gender_ = "" , main_image_ = "" ,Thumb_one_ = "" , Thumb_Two_ = "", Thumb_Three_ = "" ):
    #     self.name = name_
    #     self.price = price_
    #     self.gender = gender_
    #     self.main_image = main_image_
    #     self.Thumb_One =Thumb_one_
    #     self.Thumb_Two = Thumb_Two_
    #     self.Thumb_Three = Thumb_Three_

#table for sale
class Sale(db.Model):
    __tablename__ = "Sale"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    sizes = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    style = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(1000), nullable=False)
    discount_percentage = db.Column(db.Numeric(5, 2), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())


@app.route('/sale')
def add_sale():
    temp_title = "Puma Inverse Upgrade"
    temp_price = Decimal("240.00")
    temp_category = "men"
    temp_sizes = "7, 8, 9, 10, 11, 12"
    temp_model = "Inverse Upgrade"
    temp_style = "Lifestyle Shoes"
    temp_brand = "Puma"
    temp_image_url = "https://images.footlocker.com/is/image/FLEU/244221836604_01?wid=500&hei=500&fmt=png-alpha"
    temp_discount_percentage = Decimal("30.00")
    temp_start_date = datetime.strptime("2025-05-25", "%Y-%m-%d").date()
    temp_end_date = datetime.strptime("2025-06-25", "%Y-%m-%d").date()


    new_sale = Sale(
        title=temp_title,
        price=temp_price,
        category=temp_category,
        sizes=temp_sizes,
        model=temp_model,
        style=temp_style,
        brand=temp_brand,
        image_url=temp_image_url,
        discount_percentage=temp_discount_percentage,
        start_date=temp_start_date,
        end_date=temp_end_date
    )

    try:
        db.session.add(new_sale)
        db.session.commit()
    except: 
      return "Error comitting item"

    return "Added Sale Item"

    

    

    





@app.route('/add_product')#Add the data one by one in databse by get mesthod #
def add_product():
    temp_title = "Puma RS-X DRIFT PRM"
    temp_price = 220
    temp_category = "men"
    temp_sizes = "7, 8, 9, 10, 11, 12"
    temp_model = "RS-X DRIFT PRM"
    temp_style = "Lifestyle Shoes"
    temp_brand = "Puma"
    temp_image_url = "https://images.footlocker.com/is/image/FLEU/244205134604_01?wid=500&hei=500&fmt=png-alpha" 
    temp_main_image = "puma_rsxdrift_main.jpg"
    temp_Thumb_one = "puma_rsxdrift_thumb1.jpg"
    temp_Thumb_Two = "puma_rsxdrift_thumb2.jpg"
    temp_Thumb_Three = "puma_rsxdrift_thumb3.jpg"

    
    new_shoe = Shoes(
    title=temp_title,
    price=temp_price,
    category=temp_category,
    sizes=temp_sizes,
    model=temp_model,
    style=temp_style,
    brand=temp_brand,
    image_url=temp_image_url,
    main_image=temp_main_image,
    Thumb_One=temp_Thumb_one,
    Thumb_Two=temp_Thumb_Two,
    Thumb_Three=temp_Thumb_Three
    )
#this shows if shoes save in route it show message add item otherwise shows error#
    try:
        db.session.add(new_shoe)
        db.session.commit()
    except:
        return "Error comitting item"
    
    return "Added Item"



@app.route('/')
def home():
    return render_template("home.html")

@app.route('/product/<int:product_id>')
def product(product_id):
    print(product_id)
    shoes = Shoes.query.get(product_id)
    print(shoes.title)
    return render_template("product.html", shoe=shoes)

from datetime import date 

@app.route('/sale-items')
def sale_items():
    today = date.today() 

    # Fetch all sale items where today's date is within the sale period
    active_sales = Sale.query.filter(Sale.start_date <= today, Sale.end_date >= today).all()

    return render_template('sale_items.html', sales=active_sales)



     

@app.route('/productlisting')
def productlisting():
    return render_template("productlisting.html")

    return jsonify(all_shoes)


@app.route('/search')
def search():
    query = request.args.get('query', '').strip()

    if not query:
        return render_template("search_results.html", results=[], message="Please enter a search term.")

    results = Shoes.query.filter(
        or_(
            Shoes.title.ilike(f"%{query}%"),
            Shoes.model.ilike(f"%{query}%"),
            Shoes.brand.ilike(f"%{query}%"),
            Shoes.sizes.ilike(f"%{query}%"),
            cast(Shoes.price, String).ilike(f"%{query}%"),
            Shoes.image_url.ilike(f"%{query}%"),
            Shoes.style.ilike(f"%{query}%"),
            Shoes.category.ilike(f"%{query}%")
        )
    ).all()
       
    if not results:
        return render_template("search_results.html", results=[], message="No matching shoes found.")

    return render_template("search_results.html", results=results, message=f"Results for '{query}'")



if __name__ == '__main__':
    app.run(debug=True)
