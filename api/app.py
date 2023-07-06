from flask import Flask,render_template,redirect

app = Flask(__name__)

mode = 'development'
# mode = 'production'

website_full = 'Yusuph Events planning & Planning'
website_short = 'yepc'

if mode == 'production':
    home = 'https://yepc.vercel.app/'
elif mode == 'development':
    home = 'localhost:5000/'


# the index page
@app.route('/')
def index():
    return redirect('/en/')

# the home (english) page
@app.route('/en/')
def en_home():
    return render_template('en-home.html')



if __name__ == '__main__':
    if mode == 'development':
        app.run(debug=True)
    elif mode == 'production':
        #never show the errors to the users!
        app.run()
    