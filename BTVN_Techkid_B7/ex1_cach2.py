from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def BMI(weight,height):
    chieucao_met = height/100
    BMI = weight/(chieucao_met**2)
    return render_template('bmi.html',
                            BMI = BMI)

if __name__ == '__main__':
  app.run(debug=True)
 