from flask import Flask, jsonify
from models.user import User
from models.api_client import Steam
from models.transformers import User_transformer

app = Flask(__name__)

@app.route('/howmuchtimehaveiwasted/<steamid>')
def get_user(steamid):
    data = Steam.get_user(steamid)

    user = User_transformer().transform(data)

    return jsonify(user.to_json())

if __name__ == '__main__':
    app.run()
