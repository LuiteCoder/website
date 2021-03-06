import flask
import time

from jinja2 import TemplateNotFound

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
    except TemplateNotFound:
        return flask.render_template("404.html", url=f"{flask.request.url_root}{url}", title=site_title)

@app.route('/img/<path:path>')
def img(path):
    return flask.send_from_directory('img', path)

@app.route('/img/')
def img_home():
    return flask.render_template(f"img.html", title=site_title)

@app.errorhandler(404)
def site_not_found(e):
    return flask.render_template("404.html", url=f"{flask.request.url}", title=site_title), 404

@app.route("/")
def site():
    return flask.render_template('index.html', title=site_title)

@app.route("/glr/")
@app.route("/galaxylifereborn/")
def glr():
    return flask.redirect("https://galaxylifereborn.com/", code=302)

@app.route("/discord/")
def dc():
    return f"<html><body><p>Redirecting...</p><script>var timer = setTimeout(function() {{window.location='/sad/'}}, 1300);</script></body></html>" 

@app.route("/sad/")
def sad():
    return 'i have no discord server :( <iframe width="1" height="1" src="https://www.youtube.com/embed/6qpv9jbFQtg?autoplay=1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'

if __name__ == "__main__":
    app.run(port=81, host="0.0.0.0")