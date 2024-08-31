from flask import Flask, render_template
from datetime import datetime
from scrape import scrape_stocks, scrape_pm25

# print(__name__)

app = Flask(__name__)

# if __name__==__main__:


@app.route("/")
@app.route("/index")
def index():
    today = datetime.now()
    # print(today)
    # return f"""<h1>hello<br>{today}</h1><br>
    # <p>flask123</p><hr>
    # """
    name = "Jay"
    return render_template("index.html", date=today, n=name)


# books = {1: "Python book", 2: "Java book", 3: "Flask book"}
books = {
    1: {
        "name": "Python book",
        "price": 299,
        "image_url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/CN1/136/11/CN11361197.jpg&v=58096f9ck&w=348&h=348",
    },
    2: {
        "name": "Java book",
        "price": 399,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/087/31/0010873110.jpg&v=5f7c475bk&w=348&h=348",
    },
    3: {
        "name": "C# book",
        "price": 499,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/036/04/0010360466.jpg&v=62d695bak&w=348&h=348",
    },
    4: {
        "name": "??? book",
        "price": 599,
        "image_url": "data:image/jpeg;base64,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",
    },
}


@app.route("/pm25")
def get_pm25():
    today = datetime.now()
    columns, values = scrape_pm25()
    data = {
        "columns": columns,
        "values": values,
        "today": today.strftime("%Y/%m/%d %M:%H:%S"),
    }
    return render_template("pm25.html", data=data)


@app.route("/stocks")
def get_stocks():
    datas = scrape_stocks()
    return render_template("stocks.html", stocks=datas)


@app.route("/books")
def show_books():
    # return f"<h1>books<br>{today}</h1>"
    # print(books)
    for key in books:
        print(books[key])
    return render_template("books.html", books=books)


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
