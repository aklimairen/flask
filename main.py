
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main_view():
    return render_template("index.html")


@app.route("/about")
def about_view():
    return render_template("about.html")


@app.route("/blog-post")
def blog_post_view():
    return render_template("blog-post.html")


if __name__ == "__main__":
    app.run(debug=True)
