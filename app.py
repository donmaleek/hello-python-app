from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World from Eng.Mathias Flask App!"

if __name__ == '__main__':
    port = int (os.environ.get("port" ,5000))
    app.run(host='0.0.0.0', port=5000)

