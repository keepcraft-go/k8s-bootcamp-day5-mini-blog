from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "data.json"

def load_posts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf‑8") as f:
            return json.load(f)
    return []

def save_posts(posts):
    with open(DATA_FILE, "w", encoding="utf‑8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

posts = load_posts()

@app.route('/posts', methods=['GET', 'POST'])
def handle_posts():
    global posts
    if request.method == 'POST':
        data = request.get_json()
        post = {
            'id': len(posts) + 1,
            'title': data['title'],
            'content': data['content']
        }
        posts.append(post)
        save_posts(posts)
        return jsonify(post), 201
    else:
        return jsonify(posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
