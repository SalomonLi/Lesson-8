from flask import Flask
from flask import render_template
from flask import request
from flask import redirect


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/mypage/me', methods=['GET', 'POST'])
def blog():
   if request.method == 'GET':
       print("We received GET")
       return render_template("index.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)