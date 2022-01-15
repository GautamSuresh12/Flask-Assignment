from flask import Flask

app = Flask(__name__)

@app.route('/')
def myname():
    return 'My name is Gautam'

@app.route('/college')
def college():
    return 'Currently pursuing in Sethu Institue of Technology'

@app.route('/address')
def address():
    return 'Address - Meenakshi nagar, Opp to fatima college, Vilangudi'

@app.route('/city')
def city():
    return 'I live in Madurai City'

if __name__ == '__main__':
    app.run()
