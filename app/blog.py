from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Post, User

blog_bp = Blueprint('blog', __name__)

# Create a new blog post (JWT required)
@blog_bp.route('/posts', methods=['POST'])
@jwt_required()
def create_post():
    data = request.get_json()
    user_id = get_jwt_identity()
    
    new_post = Post(
        title=data['title'],
        content=data['content'],
        user_id=int(user_id)
    )
    db.session.add(new_post)
    db.session.commit()

    return jsonify({"message": "Post created successfully!"}), 201

# Get all blog posts (public)
@blog_bp.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    result = []
    for post in posts:
        result.append({
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "author": post.user.email
        })
    return jsonify(result)


@blog_bp.route('/myposts', methods=['GET'])
@jwt_required()
def my_posts():
    user_id = get_jwt_identity()
    posts = Post.query.filter_by(user_id=int(user_id)).all()

    result = []
    for post in posts:
        result.append({
            "id": post.id,
            "title": post.title,
            "content": post.content
        })

    return jsonify(result)


@blog_bp.route('/posts/<int:id>', methods=['PUT'])
@jwt_required()
def update_post(id):
    user_id = get_jwt_identity()
    post = Post.query.get(id)

    if not post:
        return jsonify({"error": "Post not found"}), 404

    if post.user_id != int(user_id):
        return jsonify({"error": "You are not authorized to update this post"}), 403

    data = request.get_json()
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)

    db.session.commit()
    return jsonify({"message": "Post updated successfully!"})


@blog_bp.route('/posts/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_post(id):
    user_id = get_jwt_identity()
    post = Post.query.get(id)

    if not post:
        return jsonify({"error": "Post not found"}), 404

    if post.user_id != int(user_id):
        return jsonify({"error": "You are not authorized to delete this post"}), 403

    db.session.delete(post)
    db.session.commit()

    return jsonify({"message": "Post deleted successfully!"})

