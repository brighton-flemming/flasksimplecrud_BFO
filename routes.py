from flask import Flask, current_app, make_response, request, jsonify, g
from models import db, User, Post
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)


    @app.before_request
    def app_path():
        g.path = os.path.abspath(os.getcwd())


    @app.route('/', methods=['GET'])
    def index():
     hoster = request.headers.get('Host')
     appname = current_app.name
     response_body = f'''
        <h1>The host for this page is {hoster}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
     '''

     status_code = 200
     headers = {}

     return make_response(response_body, status_code, headers)

    @app.route('/users', methods=['GET'])
    def get_users():
        users = User.query.all()
        users_data = [{'id': user.id, 'username': user.username} for user in users]
        return jsonify(users_data)

    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        username = data.get('username')
        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'})
    
    @app.route('/users/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        data = request.get_json()
        new_username = data.get('username')

        user = User.query.get(user_id)
        if user:
            user.username = new_username
            db.session.commit()
            return jsonify({'message': 'User updated successfully'})
        else:
            return jsonify({'message': 'User not found'})

    @app.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'User deleted successfully'})
        else:
            return jsonify({'message': 'User not found'})

    @app.route('/users/<int:user_id>/posts', methods=['GET'])
    def get_user_posts(user_id):
        posts = Post.query.filter_by(user_id=user_id).all()
        posts_data = [{'id': post.id, 'content': post.content} for post in posts]
        return jsonify(posts_data)

    @app.route('/users/<int:user_id>/posts', methods=['POST'])
    def create_post(user_id):
        data = request.get_json()
        content = data.get('content')
        new_post = Post(content=content, user_id=user_id)
        db.session.add(new_post)
        db.session.commit()
        return jsonify({'message': 'Post created successfully'})

    @app.route('/posts/<int:post_id>', methods=['PUT'])
    def update_post(post_id):
        data = request.get_json()
        new_content = data.get('content')

        post = Post.query.get(post_id)
        if post:
            post.content = new_content
            db.session.commit()
            return jsonify({'message': 'Post updated successfully'})
        else:
            return jsonify({'message': 'Post not found'})

    @app.route('/posts/<int:post_id>', methods=['DELETE'])
    def delete_post(post_id):
        post = Post.query.get(post_id)
        if post:
            db.session.delete(post)
            db.session.commit()
            return jsonify({'message': 'Post deleted successfully'})
        else:
            return jsonify({'message': 'Post not found'})

    return app

