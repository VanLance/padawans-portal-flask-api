from flask import Flask, request

app = Flask(__name__)

users = {
    1:{
        'id' : 1,
        'username' : 'bc',
        'email' : 'bc@ct.com'
    },
    2 : {
        'id' : 2,
        'username' : 'ds',
        'email' : 'ds@ct.com'
    }
}

posts = {
    1 : {
        'author' : 2,
        'title' : 'Welcome to Flask',
        'body' : 'Welcome to our first full-stack app, it\'s SUPER easy and simple!'
    },
    2 : {
        'author' : 1,
        'title' : 'Flask intro',
        'body' : 'I would\'nt say it is THAT simple'
    }
}

@app.route('/')
def land():
    return {
        "you've officially landed on the REAL PAGE!!!!" : "Welcome young Padawans to Flask!"
    }

@app.route('/users')
def get_users():
    return {
        'users' : list(users.values())
    }


@app.route('/user/<int:id>')
def get_ind_user(id):
    if id in users:
        return {
            'user' : users[id]
        }
    return {
        'UH OH, something went wrong' : "invalid user id"
    }



@app.route('/user', methods=["POST"])
def create_user():
    data = request.get_json()
    print(data)
    users[data['id']] = data
    return {
        'user created successfully': users[data['id']]
    }

@app.route('/user', methods=["PUT"])
def update_user():
    data = request.get_json()
    if data['id'] in users:
        users[data['id']] = data
        return {
            'user updated' : users[data['id']]
        }
    return {
        'err' : 'no user found with that id'
    }
    
@app.route('/user', methods=["DELETE"])
def del_user():
    data = request.get_json()
    if data['id'] in users:
        del users[data['id']]
        return {
            'user gone': f"{data['username']} is no more. . . "
        }
    return {
        'err' : "can't delete that user they aren't there. . . "
    }