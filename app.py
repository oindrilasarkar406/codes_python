from flask import Flask,render_template,request

app=Flask(__name__)


@app.route("/partha")
def hello():
    return render_template('atryei.html')


@app.route("/amitava")
def calculate():
    n1=int(request.args.get("t1"))
    n2=int(request.args.get("t2"))
    sum=n1+n2
    return "<body bgcolor='blue' text='white'><center><h2>The sum is {}</h2></center></body>".format(sum)
    





if __name__=='__main__':
    app.run(debug=True)

