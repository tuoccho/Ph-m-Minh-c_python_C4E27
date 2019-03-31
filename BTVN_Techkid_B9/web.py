from flask import Flask, render_template
from mlab import river_collection

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bai5')
def bai5():
    bai5_data = river_collection.find()
    return render_template('bai5.html', bai5_data = bai5_data)

@app.route('/bai6')
def bai6():
    bai6_data = river_collection.find()
    return render_template('bai6.html', bai6_data = bai6_data)

if __name__ == '__main__':
  app.run(debug=True)
 