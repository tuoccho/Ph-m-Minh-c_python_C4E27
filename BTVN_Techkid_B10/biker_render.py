from flask import *
from database import biker_collection
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_biker',methods=["GET","POST"])
def new_biker():
    if request.method == 'GET':
      return render_template('new_biker.html')
    elif request.method == 'POST':
      form = request.form
      biker_model = form["input_model"]
      biker_fee = form["input_fee"]
      biker_image = form["input_image"]
      biker_year = form["input_year"]

      print(form)

      bikers = {

        "model" : biker_model,
        "fee" : biker_fee,
        "image" : biker_image,
        "year" : biker_year,
      }
      biker_collection.insert_one(bikers)
      return redirect("/new_biker")

      
      
if __name__ == '__main__':
  app.run(debug=True)
 