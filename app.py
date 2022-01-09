from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello():
    my_name = "Larry"
    return f'Hello, {my_name}!'

@app.route('/o-mnie')
def o_mnie():
    return f'Ja jestem tylko stronom internetowym'

@app.route('/blog')
def blog_main():
    return f"This is a main blog page"

@app.route('/blog/<id>')
def blog(id):
    return f"This is blog entry #{id}"

@app.route('/message', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("form.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

@app.route('/message_ugly', methods=['GET'])
def message_form_ugly():
    text = """
        <html>
            <head></head>

            <body>
                <form action="" method="POST">
                    <label>First Name</label>
                    <input name="firstname"/>
                    <input type="submit"/>
                </form>
            </body>
        </html  >
    """
    return text

@app.route('/index', methods=['POST'])
def index():
    return render_template('from.html')

@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    return '''
              <form method="POST">
                  <div><label>Language: <input type="text" name="language"></label></div>
                  <div><label>Framework: <input type="text" name="framework"></label></div>
                  <input type="submit" value="Submit">
              </form>'''