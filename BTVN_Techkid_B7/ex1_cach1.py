from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def BMI(weight,height):
    chieucao_met = height/100
    BMI = weight/(chieucao_met**2)
    if BMI < 16:
        return("BMI: " + str(BMI) + " -- Severely underweight")
    elif BMI < 18.5:
        return("BMI: " + str(BMI) + " -- Underweight")
    elif BMI < 25:
        return("BMI: " + str(BMI) + " -- Normal")
    elif BMI < 30:
        return("BMI: " + str(BMI) + " -- Overweight")
    else:
        return("BMI: " + str(BMI) + " -- Obese")


if __name__ == '__main__':
  app.run(debug=True)
 