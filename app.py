from flask import Flask
from flask import send_from_directory

app = Flask(__name__, static_folder='client')

@app.route('/')
def index():
  return send_from_directory('client', 'index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
