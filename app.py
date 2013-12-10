from flask import Flask, request, make_response, render_template, redirect, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import TextField, HiddenField
from wtforms.validators import Required
import hashlib

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
    topic_id = HiddenField('id')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robots.txt')
def robots():
     return app.send_static_file('robots.txt')

@app.route('/topics', methods=['GET', 'POST'])
@app.route('/topics/<int:page>', methods=['GET', 'POST'])
def show_topics(page=1):
    paged_response = Topic.query.order_by(Topic.id.asc()).paginate(page, 10, True)
    topics = paged_response.items

    form = TopicForm()
    if form.validate_on_submit():
        existing_topic = Topic.query.get(form.topic_id.data)
        existing_topic.supplied_label = form.supplied_label.data
        db.session.commit()

        flash(\
            '<strong>{0}</strong> submitted as a new label for <a class="alert-link" href="#t{1}"> Topic {2}</a>'\
            .format(\
            form.supplied_label.data,\
            existing_topic.id,\
            existing_topic.id))
        
        return redirect('/topics/{0}'.format(page))

    token_value = hashlib.md5(app.config['SECRET_KEY']).hexdigest()
    resp = make_response(render_template('topics.html', topics=topics, paged_response=paged_response, form=form))
    resp.set_cookie('token', token_value)
    return resp

@app.route('/remove/topic/<int:topic_id>', methods=['POST'])
def drop_topic(topic_id):
    if request.form['token'] == hashlib.md5(app.config['SECRET_KEY']).hexdigest():
        target_topic = Topic.query.get(topic_id)
        db.session.delete(target_topic)
        db.session.commit()
        resp = make_response()
    return resp
