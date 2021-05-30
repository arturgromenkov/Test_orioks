from flask import Flask,request,current_app,make_response,render_template,redirect,url_for
from jinja2 import Template
import db
app = Flask(__name__,template_folder="D:\\Pycharm\\Test_orioks\\template")

@app.route('/login_for_admin/', methods=['post', 'get'])
def login_for_admin():
    #message = ''
    username=''
    if request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')
    if (username=='' and password==None):
        message = "Заполните поля Логин и Пароль"
    else:
        print('записан')
    return render_template("Login_page_for_Admin.html",message=message)

@app.route('/login_for_student/', methods=['post', 'get'])
def login_for_student():
    #message = ''
    username=''
    if request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')
    if username == 'root' and password == 'pass':
        message = "Correct username and password"
    elif (username=='' and password==None):
        message = "Заполните поля Логин и Пароль"
    else:
        print(username)
        message = "Неправильный Логин или пароль"

    return render_template("Login_page_for_Student.html",message=message)


@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Student') == 'Студент':
            # pass
            print("Студент")
            return redirect((url_for('login_for_student')))
        elif request.form.get('Admin') == 'Администратор':
            # pass # do something else
            print("Админ")
            return redirect(url_for('login_for_admin'))
        else:
            # pass # unknown
            return render_template("Start_page.html")
    elif request.method == 'GET':
        print("No Post Back Call")
    return render_template("Start_page.html")


if __name__ == '__main__':
    app.run()