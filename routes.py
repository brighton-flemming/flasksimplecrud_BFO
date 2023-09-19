# routes.py
from flask import Flask, request, jsonify
from models import db, User

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

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

    return app
