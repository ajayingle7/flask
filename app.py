from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def hello_world():
    tempalte_name = "index.html"
    return render_template(tempalte_name)


@app.route("/contact")
def contact():
    return "this is contact page"

@app.route("/about")
def about():
    return "about page"

@app.route("/blogs")
def blog():
    return "blog page"


if __name__=="__main__":
    app.run(debug=True)
    print("helllooooooo00000ooooooo")


