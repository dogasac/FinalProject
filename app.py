from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news_portal.db'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))
    profile_pic = db.Column(db.String(255))

class UserInterest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    interest = db.Column(db.String(50))


class News(db.Model):
    __tablename__ = 'news'
    __table_args__ = {'extend_existing': True}  # Allow redefinition of the table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(300), nullable=False)
   
    category = db.Column(db.String(100), nullable=False)
    source = db.Column(db.String(100), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Şifre', validators=[DataRequired()])
    remember = BooleanField('Beni Hatırla')
    submit = SubmitField('Giriş Yap')

class RegistrationForm(FlaskForm):
    name = StringField('İsim', validators=[DataRequired()])
    surname= StringField('Soyisim', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Şifre', validators=[
        DataRequired(), 
        Length(min=8, message='Password must be at least 8 characters long.'),
        Regexp('(?=.*\d)(?=.*[^\w\s])', message='Password must contain at least one number and one special character.')
    ])
    confirm = PasswordField('Şifre Tekrarı', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    city = StringField('Şehir', validators=[DataRequired()])
    country = StringField('Ülke', validators=[DataRequired()])
    submit = SubmitField('Kayıt Ol')

@app.route('/')
def home():
    return render_template('index.html',)

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and user.password == login_form.password.data:
            login_user(user, remember=login_form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', login_form=login_form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        user = User(name =registration_form.name.data,surname = registration_form.surname.data,email=registration_form.email.data, password=registration_form.password.data, 
                    city=registration_form.city.data, country=registration_form.country.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home'))
    return render_template('register.html', registration_form=registration_form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/set_language', methods=['POST'])
def set_language():
    language = request.form.get('language')
    session['language'] = language
    return redirect(url_for('home'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    category = request.args.get('category', default="All")
    if category == "All":
        news_items = News.query.all()
    else:
        news_items = News.query.filter_by(category=category).all()
    return render_template('search_results.html', news_items=news_items, selected_category=category)


@app.route('/fetch_news', methods=['POST'])
def fetch_news():
    category = request.form.get('category')
    news_items = News.query.filter(News.category == category).all()
    return render_template('partials/news_items.html', news_items=news_items)


@app.route('/news/<int:news_id>')
def news_detail(news_id):
    news = News.query.get_or_404(news_id)
    return render_template('news_detail.html', news=news)

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'), nullable=False)
    like_type = db.Column(db.String(10), nullable=False)  # 'like' or 'dislike'

    user = db.relationship('User', backref=db.backref('likes', lazy=True))
    news = db.relationship('News', backref=db.backref('likes', lazy=True))

@app.route('/like_news', methods=['POST'])
def like_news():
    news_id = request.form.get('news_id')
    like_type = request.form.get('like_type', 'like')  # Default to 'like' if not specified

    existing_like = Like.query.filter_by(user_id=current_user.id, news_id=news_id).first()

    if existing_like:
        if existing_like.like_type != like_type:
            existing_like.like_type = like_type
        else:
            db.session.delete(existing_like)
    else:
        new_like = Like(user_id=current_user.id, news_id=news_id, like_type=like_type)
        db.session.add(new_like)

    db.session.commit()
    return redirect(url_for('news_detail', news_id=news_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
