import datetime

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
# GETメソッドでのアクセスは以下が実行される．
def cookie():
    count = request.cookies.get("count")
    if count is None:
        # クッキー変数"count"が存在しない場合は，countに"1"を代入する．
        count = id
    id = "あなたはこのサイトに{}回アクセスしました．".format(count)
    max_age = 60 * 60 * 24 * 120
    # クッキーの賞味期限を120日にする
    response = make_response(render_template("a4-1.html", title="クッキーの利用", id=id, max_age=max_age))

    # クッキー変数"count"にcountに1加えたものを代入する．
    return response



@app.route("/", methods=["POST"])
# POSTメソッドでのアクセスは以下が実行される．
def output():
    id = request.form["id"]
    # フォームからnameデータを取得する．
    try:
        if id == "1":
                name="桜祭り"
                time="2022/3/20"
                place="1号公園"
                color="black"
        elif id == "2":
                name="夏祭り"
                time="2023/8/5"
                place="2号公園"
                color="red"
        elif id == "3":
                name="冬祭り"
                time="2023/12/30"
                place="3号公園"
                color="red"
                
        else:
                message="idが正しくありません"
                color = "black"
        
        message = "{}は{}に{}で開催".format(name, time, place)
    except Exception:
        message = "idが正しくありません"
        color = "black"
    return render_template("a4-2out.html", title="フォームの利用", message=message, color = color)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")