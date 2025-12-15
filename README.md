Installation (Local Setup)
1️⃣ Clone repository
git clone https://github.com/shyam-maurya/ecommerce-backend.git
cd ecommerce-backend

2️⃣ Create Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate


Mac/Linux:

python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

🔐 Environment Variables

Rename .env.example to .env:

cp .env.example .env


Edit .env:

SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=127.0.0.1,localhost
ACCESS_TOKEN_LIFETIME_MINUTES=60

🔧 Running Migrations
python manage.py makemigrations
python manage.py migrate

👤 Creating Superuser
python manage.py createsuperuser


Login at:

👉 http://127.0.0.1:8000/admin/

▶️ Running the Server
python manage.py runserver


Server starts at:

👉 http://127.0.0.1:8000/


Import Products from Excel

Create products.xlsx:

name	description	price	stock_quantity

Run import:

python manage.py import_products products.xlsx
