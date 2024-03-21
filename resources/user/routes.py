from flask import request
from flask.views import MethodView


from . import bp
from db import users

@bp.route('/user')
class UserList(MethodView):
    
    def get(self):
        return { 'users' : list(users.values()) }, 200
    
    def post(self):
        data = request.get_json()

        users[data['id']] = data
        return { 'user created successfully': users[data['id']] }, 201

@bp.route('/user/<int:id>')
class User(MethodView):
    
    def get(self, id):
        if id in users:
            return {'user' : users[id] }, 200
        return {
            'UH OH, something went wrong' : "invalid user id"
        }, 400

    def put(self, id):
        data = request.get_json()
        if id in users:
            users[id] = data
            return { 'user updated' : users[id] }, 201
        return {'err' : 'no user found with that id'}, 401

    def delete(self, id):
        data = request.get_json()
        if id in users:
            del users[id]
            return { 'user gone': f"{data['username']} is no more. . . " }, 202
        return { 'err' : "can't delete that user they aren't there. . . " } , 400

