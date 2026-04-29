<<<<<<< HEAD
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="public")


@app.route("/")
def index():
    return send_from_directory("public", "index.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("public", path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
=======
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="public")


@app.route("/")
def index():
    return send_from_directory("public", "index.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("public", path)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
>>>>>>> aa4e107e081c9951a176cd917952f3a9595c390e
