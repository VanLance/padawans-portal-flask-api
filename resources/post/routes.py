from flask import request, jsonify, json
from flask.views import MethodView
from uuid import uuid4

from . import bp

from db import users, posts

@bp.route('/post')
class PostList(MethodView):
    
    def post(self):
        post_data = request.get_json()
        if post_data['author'] not in users:
            return {"message": "user does not exist"}, 400
        post_id = uuid4().hex
        posts[post_id] = post_data
        return {
            'message': "Post created",
            'post-id': post_id
            }, 201

    def get(self):
        return posts, 200

@bp.route('/post/<post_id>')
class Post(MethodView):

    def get(self, post_id):
        try: 
            return posts[post_id], 200
        except KeyError:
            return {'message':"invalid post"}, 400

    def put(self, post_id):
        post_data = request.get_json()

        if post_id in posts:
            posts[post_id] = {k:v for k,v in post_data.items() if k != 'id'} 

            return {'message': f'post: {post_id} updated'}, 201
        
        return {'message': "invalid post"}, 400

    def delete(self, post_id):
        post_data = request.get_json()

        if post_id not in posts:
            return { 'message' : "Invalid Post"}, 400
        
        posts.pop(post_id)
        return {'message': f'Post: {post_id} deleted'}

