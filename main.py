from flask import Flask, render_template

app = Flask(__name__,template_folder='templates')


@app.route('/madurai-details')
def madurai_details():
    data = ('India',
            'Tamilnadu',
            'Madurai')

    return render_template('details.html',
                           madurai=data)


if __name__ == '__main__':
    app.run()
