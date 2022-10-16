from flask import Flask,render_template,request
#from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def hello():
    return "hello welcome to flask"

@app.route('/first/<name>')
def first(name):
    return "this is first ulr testing %s"%name

@app.route('/test/<user>')
def test_html(user):
    return render_template("index.html",name = user)

@app.route('/login',methods=['GET'])

def login():
    if (request.method == 'GET' != " "):
        uname=request.args.get('uname')
        password=request.args.get('pass')
        if uname=='swathi' and password=='12345':
            return render_template("afterlogin.html",name = uname)
    
    return render_template("login.html")
if __name__ =='__main__':
    app.run(debug=True)

