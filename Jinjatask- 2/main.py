from flask import Flask, render_template

app = Flask(__name__,template_folder='templates')


@app.route('/personalities')
def personalities():
    data = (
            ('Barrack Obama', 'Male', 60),
            ('Donald Trump', 'Male', 75),
            ('Joe Biden', 'Male', 79),
            ('Sundar Pichai', 'Male', 49),
            ('Simon Biles', 'Female', 24),
             )

    return render_template('person.html',
                           data=data)


if __name__ == '__main__':
    app.run()
