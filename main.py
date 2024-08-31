from flask import Flask
from datetime import datetime

# print(__name__)

app = Flask(__name__)

# if __name__==__main__:


@app.route("/")
def index():
    today = datetime.now()
    # print(today)
    return f"""<h1>hello<br>{today}</h1><br>
    <p>flask123</p><hr>
    """


books = {1: "Python book", 2: "Java book", 3: "Flask book"}


@app.route("/books")
def show_books():
    # return f"<h1>books<br>{today}</h1>"
    return books


@app.route("/book/<int:id>")
def show_book(id):
    # 輸出有書 <h1>第一本書:xxx</h1>
    # 無此編號
    try:
        return f"<h1>第{id}本書:{books[id]}</h1>"
    except KeyError:
        return f"<h1 style='color:red'>無此編號:{id}</h1>"


@app.route("/sum/x=<x>&y=<y>")
def my_sum(x, y):
    # return f"{x},{y}"
    try:
        total = eval(x) + eval(y)
        return f"<h1>{x}+{y}={total}</h1>"
    except Exception as e:
        print(e)

    return "<h1>參數錯誤</h1>"


@app.route("/bmi/name=<n>&height=<h>&weight=<w>")
def getBmi(n, h, w):
    try:
        h = eval(h)
        w = eval(w)
        bmi = w / ((h / 100) ** 2)
        return f"<h1>{n} BMI:{bmi:.2f}</h1>"
    except Exception as e:
        print(e)
    return "<h1 style='color:red'>參數錯誤</h1>"


app.run(debug=True)
