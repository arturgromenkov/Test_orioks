from flask import Flask,request,current_app,make_response,render_template
from jinja2 import Template
app = Flask(__name__,template_folder="D:\\Pycharm\\Test_orioks\\template")


@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Encrypt') == 'Encrypt':
            # pass
            print("Encrypted")
        elif request.form.get('Decrypt') == 'Decrypt':
            # pass # do something else
            print("Decrypted")
        else:
            # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template("index.html")


if __name__ == '__main__':
    app.run()