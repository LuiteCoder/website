import flask

app = flask.Flask(__name__)
site_title = "Luite"

# this is so its easier. i dont wanna do url 1 by one tho.

@app.route("/<url>")
def home(url):
    try:
        if url == "favicon.ico":
            return flask.send_from_directory('img', 'favicon.png')
        else:
            return flask.render_template(f"{url}.html", title=site_title)
    except:
        return flask.render_template("404.html", url=f"{flask.request.url_root}{url}", title=site_title)

@app.route("/")
def redirect():
    return flask.render_template('index.html', title=site_title)



if __name__ == "__main__":
    app.run(port=83, host="0.0.0.0")