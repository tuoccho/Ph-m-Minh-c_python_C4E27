from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def users(username):
    users = {
        "duc" :{
            "name" : "Phạm Minh Đức",
            "age" : "21",
            "gender" : "Male",
            "hobbies" : "Game",
        },
        "nhat" :{
            "name" : "Nguyen Quang Nhat",
            "age" : "21",
            "gender" : "Male",
            "hobbies" : "Gái",
        },
    }
    if username in users:  
        return render_template('user.html',users=users[username])
    else:
        return 'User not found'

if __name__ == '__main__':
  app.run(debug=True)
 