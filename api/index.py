from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Vercel! If you see this, the routing is working. Now I will restore the full app logic."

@app.route('/test')
def test():
    return "Test route works"
