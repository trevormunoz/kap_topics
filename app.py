from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/kap'
db = SQLAlchemy(app)

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orig_label = db.Column(db.String(80), nullable=False)
    supplied_label = db.Column(db.String(80))
    terms_top = db.Column(db.Text)
    terms_all = db.Column(db.Text)

    def __repr__(self):
        return '<Topic {0}>'.format(self.orig_label)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/topics')
@app.route('/topics/<int:page>')
def show_topics(page=1):
    paged_response = Topic.query.paginate(page, 25, True)
    topics = paged_response.items

    return render_template('topics.html', topics=topics, paged_response=paged_response)
    