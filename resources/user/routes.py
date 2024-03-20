from flask import request

from app import app
from db import users

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
