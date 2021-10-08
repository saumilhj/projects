from flask import *
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from forms import AddListForm, AddItemForm

app = Flask(__name__)
app.config['SECRET_KEY'] = YOUR_SECRET_KEY
app.config["MONGO_URI"] = "mongodb://localhost:27017/listsDB.db"
mongo = PyMongo(app)
db = mongo.db
lists = db.lists
bootstrap = Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def home():
    all_lists = list(db.lists.find())
    if request.method == "GET":
        return render_template("index.html", lists=all_lists)
    else:
        pass


@app.route("/create-list", methods=["GET", "POST"])
def create_list():
    form = AddListForm()
    if request.method == "GET":
        return render_template("create-list.html", form=form)
    else:
        if len(list(db.lists.find({'list': form.list_name.data}))) != 0:
            return {"error": "list already exists"}
        else:
            db.lists.insert_one({'list': form.list_name.data, 'items': []})
            return redirect(url_for("home"))


@app.route("/<list_name>", methods=["GET", "POST"])
def list_show(list_name):
    form = AddItemForm()
    des_list = list(db.lists.find({'list': list_name}))
    if request.method == "GET":
        return render_template("list.html", des_list=des_list, form=form)
    else:
        if request.form.get(list_name):
            print(list_name)
        else:
            db.lists.update_one({'list': list_name}, {'$push':{'items': form.item_name.data}})
            return redirect(url_for("home"))


@app.route("/del-list/<list_name>")
def del_list(list_name):
    db.lists.delete_many({'list': list_name})
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
