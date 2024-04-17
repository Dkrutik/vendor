from config import *
from flask import Flask, render_template
from models import db, User


# @app.route('/')
# def hello():
#     return 'Hello, Worldsssss!'


@app.route('/base')
def hello():
    return render_template("index.html")

@app.route('/list')
def addlist():
    return render_template("tables-general.html")


# @app.route('/')
# def basedata():
#     return render_template("base.html")

@app.route('/adduser', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    if not username or not email:
        return jsonify({'message': 'Both username and email are required'}), 400

    new_user = User(username=username, email=email)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Failed to add user: {str(e)}'}), 500
    finally:
        db.session.close()



@app.route("/", methods=["GET"])
def getdata():
    userdata = User.query.all()

    users = [{
        'id': user.id,
        'username': user.username,
        'email': user.email
    } for user in userdata]

    return render_template("userlist.html", users=users)



@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        new_user = User(username=name, email=email)
        db.session.add(new_user)
        db.session.commit()

        # return "User added successfully!"
    return render_template('adduser.html') 




@app.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)

    if user:
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
        return render_template("particularId.html", user=user_data)
    else:
        return "User not found", 404


### api in flask
# @app.route("/getdata",methods=["GET"])
# def getdata():
#     userdata=User.query.all()

#     serialized_users = []
#     for user in userdata:
#         serialized_user = {
#             'id': user.id,
#             'username': user.username,
#             'email': user.email
#         }
#         serialized_users.append(serialized_user)

#     return jsonify({"userdata": serialized_users})


