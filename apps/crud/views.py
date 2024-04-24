from flask import Blueprint,render_template

# Blueprint로 crud 앱을 생성한다
crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",

    static_folder="static",
)

@crud.route("/")
def index():
    return render_template("crud/index.html")