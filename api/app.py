from flask import Flask,render_template,redirect

app = Flask(__name__)

mode = 'development'
# mode = 'production'

# the index page
@app.route('/')
def index():
    return redirect('/en/')

# the home (english) page
@app.route('/en/')
def en_home():
    return render_template('en-home.html')



if __name__ == '__main__':
    app.run(debug=True)