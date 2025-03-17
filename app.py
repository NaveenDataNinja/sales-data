from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Change this to your MySQL username
    password="User password",  # Change this to your MySQL password
    database="sales_db"  # Change this to your database name
)                                                         


cursor = db.cursor()

# Route to display HTML form
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    date = request.form["date"]
    product_name = request.form["product_name"]
    quantity = int(request.form["quantity"])
    price = float(request.form["price"])

    sql = "INSERT INTO sales_data (date, product_name, quantity, price) VALUES (%s, %s, %s, %s)"
    values = (date, product_name, quantity, price)
    
    cursor.execute(sql, values)
    db.commit()

    return "Data saved successfully- ThankYou BY N@veen N!"

if __name__ == "__main__":
    app.run(debug=True)

"""
MIT License  

Copyright (c) 2025 Naveen Kumar Narasapuram  

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.


Copyright (c) 2024 Naveen Kumar Narasapuram
"""
