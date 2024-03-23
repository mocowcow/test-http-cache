from views import last_modified
from views import etag
from views import update

from flask import Flask


app = Flask(__name__)
app.register_blueprint(last_modified.bp)
app.register_blueprint(etag.bp)
app.register_blueprint(update.bp)


@app.route("/")
def index():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)
