#---------+
# Imports |
#-----------------------------------------------------------------------------------------
from flask  import Flask, render_template, request, session, redirect, url_for
from models import db, User
from forms  import SignupForm, LoginForm



#---------------------------------------------------------------+
# Instantiate a sub-class of the global Flask class.  Add hooks |
# for app to use sqlalchemy to connect to the app's database.   |
# Tie the app to our instance of SQLAlchemy.                    |
# Create secret key to protect against CSRF attacks.            |
#----------------------------------------------------------------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ca_tool:ca_tool@/ca_tool'
db.init_app(app)   
app.secret_key = 'development-key'



#------------------+
# '/' and '/index' |
#-----------------------------------------------------------------------------------------
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



#----------+
# '/about' |
#-----------------------------------------------------------------------------------------
@app.route('/about')
def about():
    return render_template('about.html')



#-----------+
# '/signup' |
#-----------------------------------------------------------------------------------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html', form=form)
        newuser = User(form.first_name.data,
                       form.last_name.data,
                       form.email.data,
                       form.password.data)
        db.session.add(newuser)
        db.session.commit()
        session['email'] = newuser.email
        return redirect(url_for('home'))
    return render_template('signup.html', form=form)



#-----------+
# '/home' |
#-----------------------------------------------------------------------------------------
@app.route('/home')
def home():
    return render_template('home.html')



#-----------+
# '/login' |
#-----------------------------------------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET' or form.validate() == False:
        return render_template('login.html', form=form)
    email    = form.email.data.lower()
    password = form.password.data
    user     = User.query.filter_by(email=email).first()
    if user is None:
        form.email.errors.append('No user matches email supplied')
        return render_template('login.html', form=form)
    if not user.check_password(password):
        form.password.errors.append("That's not the right passowrd")
        return render_template('login.html', form=form)
    session['email'] = email
    return redirect(url_for('home'))



#---------------------------------------+
# If running as a stand-alone program   |
# run app under the built-in web server |
#-----------------------------------------------------------------------------------------
if __name__ == '__main__':
    # import pdb; pdb.set_trace()
    app.run(host='0.0.0.0', port=8080, debug=True, ssl_context=None)
