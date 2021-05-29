from flask import Flask,request,current_app,make_response,render_template
from jinja2 import Template
app = Flask(__name__,template_folder="D:\\Pycharm\\Test_orioks\\template")
app_context=app.app_context()
app_context.push()
def index():
    return render_template('index.html')
app.add_url_rule('/','index',index)
def books(genre):
    res = make_response("All Books in {} category".format(genre))
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'Foobar'
    return res
app.add_url_rule('/books/<genre>','books_and_genre',books)

if __name__ == "__main__":
    app.run()