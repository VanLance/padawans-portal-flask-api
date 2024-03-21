from flask import request, jsonify, json
from flask.views import MethodView
from flask_smorest import abort
from uuid import uuid4

from . import bp
from schemas import PostSchema
from db import users, posts

@bp.route('/post')
class PostList(MethodView):
    
    @bp.arguments(PostSchema)
    def post(self, post_data):
        if post_data['author'] not in users:
            return {"message": "user does not exist"}, 400
        post_id = uuid4().hex
        posts[post_id] = post_data

        return {
            'message': "Post created",
            'post-id': post_id
            }, 201

    @bp.response(200, PostSchema(many=True))
    def get(self):
        return list(posts.values())

@bp.route('/post/<post_id>')
class Post(MethodView):

    @bp.response(200, PostSchema)
    def get(self, post_id):
        try: 
            return posts[post_id]
        except KeyError:
            return {'message':"invalid post"}, 400

    @bp.arguments(PostSchema)
    def put(self, post_data, post_id):
        if post_id in posts:
            posts[post_id] = {k:v for k,v in post_data.items() if k != 'id'} 

            return {'message': f'post: {post_id} updated'}, 201
        
        return {'message': "invalid post"}, 400

    def delete(self, post_id):

        if post_id not in posts:
            return { 'message' : "Invalid Post"}, 400
        
        posts.pop(post_id)
        return {'message': f'Post: {post_id} deleted'}

