from flask import Flask, render_template, request, redirect

app = Flask(__name__)

data = [
    {
        'name': 'アントリューズ',
        'comment': 'まあまあ、やれるんでは？'
    },
    {
        'name': 'デスティニーソング',
        'comment': '菜々子やねー'
    }
]


def add_horse(horse):
    data.append(horse)


def get_horse_list():
    return data

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/index") #アプリケーション/indexにアクセスが合った場合
def index():
    return render_template('index.html', title='俺の馬', horses = get_horse_list())

@app.route("/register")
def register():
    return render_template('register.html', title='俺の馬登録')

@app.route("/registerpost", methods=['GET','POST'])
def registerpost():
    print('request :',request)
    print('form : ', request.form)
    name = request.form['name']
    comment = request.form['comment']

    print('name :', name, 'comment :', comment)

    add_horse({'name': name, 'comment': comment})

    return redirect("/index", code=302)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
