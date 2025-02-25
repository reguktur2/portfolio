from flask import *
from postmanAPP import *
from supabase import create_client, Client

# Параметри для підключення до Supabase
url = "https://ijymkeznmbkodxexifmo.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlqeW1rZXpubWJrb2R4ZXhpZm1vIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzQ1MzQyNzMsImV4cCI6MjA1MDExMDI3M30.wVK0QAUVIR5X0htVs7yYFNhklUqB6CaWM0qBK2rvAJk"
supabase: Client = create_client(url, key)

# Створення Flask додатка
app = Flask(__name__, static_folder='static')

# Маршрут для головної сторінки
@app.route('/')
def home():
    return render_template('index.html')

# Маршрут для обробки форми
@app.route('/submit', methods=['POST'])
def submit():
    # Отримання даних з форми
    name = request.form.get('name')
    message = request.form.get('message')
    email = request.form.get('email')

    print(email)
    print(message)
    print(name)
    res = f"Ім'я{name}\nПошта роботодавця: {email}\nКоментар: {message}"
    message = sendMesage('Новий відгук!', res)

    result = mailjet.send.create(data=message)
    print (result.json())
    return redirect(url_for('home'))


# Запуск додатка
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)








# app = Flask(__name__)

# @app.route('/submit', methods=['POST'])
# def submit_form():
#     name = request.form.get('name')
#     message = request.form.get('message')
#     email = request.form.get('email')

#     # Example: print the data (for testing)
#     print(f"Name: {name}")
#     print(f"Message: {message}")
#     print(f"Email: {email}")

#     # You can also process or store this data as needed
#     return render_template('thank_you.html', name=name)

# if __name__ == '__main__':
#     app.run(debug=True)




