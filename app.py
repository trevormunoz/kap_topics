from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orig_label = db.Column(db.String(80), nullable=False)
    supplied_label = db.Column(db.String(80))
    terms_top = db.Column(db.Text)
    terms_all = db.Column(db.Text)

    def __repr__(self):
        return '<Topic {0}>'.format(self.orig_label)

class TopicForm(Form):
    supplied_label  = TextField('supplied_label', validators = [Required()])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/topics')
@app.route('/topics/<int:page>')
def show_topics(page=1):
    paged_response = Topic.query.order_by(Topic.id.asc()).paginate(page, 10, True)
    topics = paged_response.items

    return render_template('topics.html', topics=topics, paged_response=paged_response)
    