'''blabla'''
#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
@app.route("/", strict_slashes=False)
def web_flask():
    '''blabla comeback'''
    return "<p>Hello HBNB!</p>"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)