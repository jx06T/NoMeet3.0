from flask import Flask, jsonify, request
from flask_cors import CORS

class App:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route("/", methods=['GET'])
        def api():
            temp = AllMsg.copy()
            AllMsg.clear()  
            data["RoomCode"] = request.args.get('room_code')
            return jsonify(temp)

        @self.app.route("/get", methods=['POST'])
        def get():
            data_received = request.json
            data["people"] = data_received["people"]
            print(data_received)  
            return "ok"

    def run(self):
        self.app.run()

if __name__ == "__main__":
    data = {}
    AllMsg = []
    app = App()
    app.run()