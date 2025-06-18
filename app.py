from flask import Flask, render_template ,json
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
from sqlalchemy.sql.expression import func
from datetime import date 
from werkzeug.security import generate_password_hash, check_password_hash




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
    # main_image = db.Column(db.String(1000), nullable=False)
    Thumb_One =  db.Column(db.String(1000), nullable=False)
    Thumb_Two =  db.Column(db.String(1000), nullable=False)
    Thumb_Three =  db.Column(db.String(1000), nullable=False)

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


#table for New Arivial
class Newarrivals(db.Model):
    __tablename__ = "Newarrivals"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    sizes = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    style = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(1000), nullable=False)
    

@app.route('/newarrivals')
def add_newarrivals():
    temp_title = "ASICS Gel-Kayano 28"
    temp_price = Decimal("160.00")
    temp_category = "men"
    temp_sizes = "7, 8, 9, 10, 11, 12"
    temp_model = "Gel-Kayano 28"
    temp_style = "Running"
    temp_brand = "ASICS"
    temp_image_url = "https://cdn.asics.com/media/catalog/product/2/1/2111A037_020_SR_RT_GLB.jpg"
    temp_category = "newarrival" 

    new_item = Newarrivals(
        title=temp_title,
        price=temp_price,
        category=temp_category,
        sizes=temp_sizes,
        model=temp_model,
        style=temp_style,
        brand=temp_brand,
        image_url=temp_image_url,
    )

    try:
        db.session.add(new_item)
        db.session.commit()
    except: 
      return "Error comitting item"
      return "Added New Item"

    

class User(db.Model):
    __tablename__= "users"

    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(255))
    password = db.Column(db.String(512), nullable=False)


@app.route('/user')
def add_user():
    temp_first_name = "mandeep"
    temp_last_name = "singh"
    temp_email = "writetomandeeprana@gmail.com"
    temp_phone = "1234567890"
    temp_address = "14,wellinton"
    temp_password = "123456"  

    new_user = User(
        first_name=temp_first_name,
        last_name=temp_last_name,
        email=temp_email,
        phone=temp_phone,
        address=temp_address,
        password=temp_password,
    )

    try:
        db.session.add(new_user)
        db.session.commit()
        return "Added New user"
    except Exception as e:
        db.session.rollback()
        return f"Error: {e}"

   




    

    

#Home page Api's
    
@app.route('/women')
def women():
    womens_shoes = db.session.query(Shoes).filter(Shoes.category == "women").all()
    print(womens_shoes)
    for w in womens_shoes:
        print(w.title)

    return render_template('category.html', products = womens_shoes ,category="women")

    
@app.route('/men')
def men():
    men_shoes = db.session.query(Shoes).filter(Shoes.category == "men").all()
    print(men_shoes)
    for m in men_shoes:
        print(m.title)

    return render_template('category.html' , products = men_shoes , category ="men")

    
@app.route('/kids')
def kids():
    kids_shoes = db.session.query(Shoes).filter(Shoes.category == "kids").all()
    print(kids_shoes)
    for k in kids_shoes:
        print(k.title)

    return render_template('category.html' , products = kids_shoes , category ="kids")

@app.route('/brand/<brand_name>')
def brand_filter(brand_name):
    brand_shoes =Shoes.query.filter(func.lower(Shoes.brand) == brand_name.lower()).all()
    return render_template('category.html', products=brand_shoes, category=f"Brand: {brand_name}")


@app.route('/style/<style_name>')
def style_filter(style_name):
    style_shoes =Shoes.query.filter(func.lower(Shoes.style) == style_name.lower()).all()
    return render_template('category.html', products=style_shoes, category=f"Style: {style_name}")

@app.route('/newarrival')
def newarrival():
    newarrival_shoes = Newarrivals.query.filter().all()

    for shoe in newarrival_shoes:
        print(shoe.title, shoe.category)

    # Pass the result to the template
    return render_template('category.html', products=newarrival_shoes, category="NewArrivials")





@app.route('/filterbar' , methods =['POST'])
def filterbar():
    brand = request.json.get('brand')
    model = request.json.get('model')
    style = request.json.get('style')
    price = request.json.get('price')
    print(brand, model , style , price)

    query = db.session.query(Shoes)

    if brand:
        query = query.filter(Shoes.brand == brand)
    if model:
        query = query.filter(Shoes.model == model)
    if style:
        query = query.filter(Shoes.style == style)


    if price:
        if price == "0-50":
             filter_shoes = db.session.query(Shoes).filter(Shoes.price < 50)

        elif price=="50-100":
             filter_shoes = db.session.query(Shoes).filter(Shoes.price .between (50,100))

            
        elif price=="50-100":
             filter_shoes = db.session.query(Shoes).filter(Shoes.price .between (100,150))

            
        elif price=="150+":
             filter_shoes = db.session.query(Shoes).filter(Shoes.price > (150))

            
    filter_shoes = query.all()


    # filter_shoes = db.session.query(Shoes).filter(Shoes.brand == brand, Shoes.model == model , Shoes.style == style  , Shoes.price == price).all()
    return render_template('productlisting.html',  products = filter_shoes  )
    



@app.route('/add_product')#Add the data one by one in databse by get mesthod #
def add_product():
    temp_title = "New Balance 574 Kids' Shoes"
    temp_price = 170
    temp_category = "kids"
    temp_sizes = "3, 4, 5, 6, 7"
    temp_model = "574"
    temp_style = "Lifestyle Shoes"
    temp_brand = "New Balance"
    temp_image_url = "https://www.footlocker.co.nz/en/category/kids/shoes/new-balance/574.html"
    # temp_main_image = "new_balance_574_kids_main.jpg"
    temp_Thumb_one = "new_balance_574_kids_thumb1.jpg"
    temp_Thumb_Two = "new_balance_574_kids_thumb2.jpg"
    temp_Thumb_Three = "new_balance_574_kids_thumb3.jpg"
    temp_Thumb_Four = "new_balance_574_kids_thumb3.jpg"

    new_shoe = Shoes(
        title=temp_title,
        price=temp_price,
        category=temp_category,
        sizes=temp_sizes,
        model=temp_model,
        style=temp_style,
        brand=temp_brand,
        image_url=temp_image_url,
        # main_image=temp_main_image,
        Thumb_One=temp_Thumb_one,
        Thumb_Two=temp_Thumb_Two,
        Thumb_Three=temp_Thumb_Three,
        
        )
#this shows if shoes save in route it show message add item otherwise shows error#
    try:
            db.session.add(new_shoe)
            db.session.commit()
    except:
            return "Error comitting item"
        
    return "Added Item"



@app.route('/cart')
def cart():
    return render_template("cart.html")

@app.route('/checkout')
def checkout():
    return render_template("checkout.html")


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/product/<int:product_id>')#api product
# def product(product_id):
#     print(product_id)
#     shoes = Shoes.query.get(product_id)
#     print(shoes.title)
#     return render_template("product.html", shoe=shoes)
def product(product_id):
    # Get the main product
    shoe = Shoes.query.get_or_404(product_id)

    # Get 3 random shoes excluding the current one
    related_shoes = Shoes.query.filter(Shoes.id != product_id).order_by(func.random()).limit(5).all()#shows some romdam pic fom databse

    return render_template("product.html", shoe=shoe, related_shoes=related_shoes)



@app.route('/sale-items')#api sale
def sale_items():
    today = date.today() 

    # Fetch all sale items where today's date is within the sale period
    active_sales = Sale.query.filter(Sale.start_date <= today, Sale.end_date >= today).all()

    return render_template('sale_items.html', sales=active_sales)



     

@app.route('/productlisting')
def productlisting():
    all_shoes = Shoes.query.all()  # Fetch all products from DB
    print(all_shoes)
    return render_template("productlisting.html", products=all_shoes)


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
