from flask import request
from flask.views import MethodView
from uuid import uuid4

from schemas import UserSchema
from . import bp
from db import users

@bp.route('/user')
class UserList(MethodView):
    
    @bp.response(200, UserSchema(many=True))
    def get(self):
        return list(users.values())
    
    @bp.arguments(UserSchema)
    @bp.response(201, UserSchema)
    def post(self, data):
 
        user_id = uuid4().hex
        users[user_id] = data
        return users[user_id]

@bp.route('/user/<int:id>')
class User(MethodView):
    
    @bp.response(200, UserSchema)
    def get(self, id):
        if id in users:
            return users[id]
        return {
            'UH OH, something went wrong' : "invalid user id"
        }, 400

    @bp.arguments(UserSchema)
    def put(self, data, id):
        data = request.get_json()
        if id in users:
            users[id] = data
            return { 'user updated' : users[id] }, 201
        return {'err' : 'no user found with that id'}, 401

    def delete(self, id):
        
        if id in users:
            del users[id]
            return { 'user gone': f" is no more. . . " }, 202
        return { 'err' : "can't delete that user they aren't there. . . " } , 400

