from flask import Flask, render_template, request, url_for, redirect
from bson.objectid import ObjectId
import pymongo

app = Flask(__name__)
# client = MongoClient('localhost', 27017)
# client = MongoClient('localhost', 27017, username='username', password='password')



client = pymongo.MongoClient("mongodb+srv://MuGiWara785:zC4hJlqc7U0M5YXn@cluster0.prmk4o2.mongodb.net/?retryWrites=true&w=majority")
db = client.test


db = client.flask_db
todos = db.todos

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)


@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

@app.post('/<id>/edit/')
def edit(id):
    todos.update_one({"_id": ObjectId(id)}, {"$set": {"content": request.form['content'], "degree": request.form['degree']}})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
