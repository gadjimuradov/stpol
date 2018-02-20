from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    user = {'username': 'Mukhtar'}
    return render_template('main.html', title='Home', user=user)



@app.route('/contact/')
def contact_page():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
