from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
   # Render the page
   return "Hello Python das ist der 40 Test des Python Programms !!!!!!!"

def add(a, b):
    return a + b

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)