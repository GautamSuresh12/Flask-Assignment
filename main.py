from flask import Flask

app = Flask(__name__)

@app.route('/')
def name():
    return 'My name is Gautam'

@app.route('/')
def college():
    return 'Currently pursuing in Sethu Institue of Technology'

@app.route('/')
def address():
    return 'Address - Meenakshi nagar, Opp to fatima college, Vilangudi'

@app.route('/')
def city():
    return 'I live in Madurai City'

if __name__ == '__main__':
    app.run()