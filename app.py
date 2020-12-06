import flask

app = flask.Flask(__name__)

# this is so its easier. i dont wanna do url 1 by one tho.

@app.route("/<url>")
@app.route("/<url>/")
def home(url):
    try:
        if url == "favicon.ico":
            return flask.send_from_directory('img', 'favicon.png')
        else:
            return flask.render_template(f"{url}.html")
    except:
        flask.abort(404)

@app.route("/")
def redirect():
    return flask.redirect(f"{flask.request.url}index", code=302)



if __name__ == "__main__":
    app.run(port=81, host="0.0.0.0")