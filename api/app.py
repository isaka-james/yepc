from flask import Flask,render_template,redirect
from datetime import date

app = Flask(__name__)

mode = 'development'
# mode = 'production'

# dealing with dates
today = date.today()
engDate = today.strftime("%B %d, %Y") # July 01,2023
year = today.strftime("%Y") # 2023

# website variables
website_full = 'Yusuph Events planning planning & Cartening'
website_short = 'yepc'
slogan = 'Make Your Event Memorable with Us'
developer = 'masterplan'

# mode of the website
if mode == 'production':
    home = 'https://yepc.vercel.app/'
elif mode == 'development':
    home = 'localhost:5000/'


# ------------ end of the variables of the website ---------- #







#################################################
## ******************************************* ##
# -------- starts of the functions ------------ #
## ***********codes*and*functions************** #
#################################################


# The index page
@app.route('/')
def index():
    return redirect('/en/')

# the home (english) page
@app.route('/en/')
def en_home():
    headers = {
        'title': website_full,
        'description':'Welcome to our comprehensive event planning and catering services website. From weddings to corporate events, our team of experienced professionals is here to bring your vision to life. Discover our wide range of services, including venue selection, event coordination, and exquisite catering options. Whether you\'re hosting an intimate gathering or a grand celebration, trust us to handle every detail with meticulous care. Visit us now and let us turn your event into an unforgettable experience.',
        'backend': developer,

    }
    return render_template('en-home.html',**context)















#########################################
#########################################
##### server configurations stuffs ######
#########################################
#########################################





# handling the 404 error
@app.errorhandler(404)
def page_404(error):
    #lets redirect home
    return redirect('/')

# redirecting to https (443)
@app.before_request
def forwarding_https():
    if not request.is_secure:
        url = request.url.replace('http://','https://',1)
        code = 301 #redirect code
        return redirect(url,code=code)

if __name__ == '__main__':
    if mode == 'development':
        app.run(debug=True)
    elif mode == 'production':
        #never show the errors to the users!
        app.run()
    