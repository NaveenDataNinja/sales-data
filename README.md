# 📊 Sales Data Entry Web Application

🚀 A Sales Data Entry web application built using **Python, Flask, MySQL, HTML & CSS**.  
This project helps businesses **record and manage sales transactions efficiently**.

---

## 🛠️ Technologies Used  
- **Python** 🐍  
- **Flask** (Web framework)  
- **MySQL** (Database)  
- **HTML & CSS** (Frontend)  
- **VS Code** (Code editor)  
- **Git & GitHub** (Version control & project hosting)  

---

## 📌 Features  
✅ User-friendly **sales data entry form**  
✅ Stores sales data securely in **MySQL**  
✅ Flask-powered **backend for form submissions**  
✅ Scalable & extendable with **analytics & dashboards**  

---

## 🚀 Installation Guide  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/NaveenDataNinja/sales-data.git
cd sales-data
2️⃣ Create & Activate a Virtual Environment (Optional, but Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # (For macOS/Linux)
venv\Scripts\activate  # (For Windows)
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up MySQL Database
1️⃣ Open MySQL Command Line or MySQL Workbench
2️⃣ Run these SQL commands to create the database & table:

sql
Copy
Edit
CREATE DATABASE sales_db;
USE sales_db;

CREATE TABLE sales_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL
);
3️⃣ Update database credentials in app.py if necessary.

5️⃣ Run the Flask Application
bash
Copy
Edit
python app.py
✅ After running the above command, your Flask server will start, and you'll see:

csharp
Copy
Edit
 * Running on http://127.0.0.1:5000/
6️⃣ Open the Web Application
Open Google Chrome (or any browser)
Go to http://127.0.0.1:5000/
✅ Now, you can enter sales data into the form! 🎉
🛠️ Future Enhancements
🚀 Power BI Dashboard for data visualization
🔒 User Authentication & Role-based Access
📊 Export Sales Data to Excel/CSV

📌 Author
👨‍💻 Naveen Kumar Narasapuram
📌 Aspiring Data Analyst | Python | SQL | Power BI

📜 License
This project is licensed under the MIT License.

