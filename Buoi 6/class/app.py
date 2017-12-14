from flask import Flask, render_template, request, flash
import mlab
from mongoengine import *
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mt'

# 1.Connect to database
mlab.connect()
# 2.Design collection
class Item(Document):
    title = StringField()
    image = StringField()
    description = StringField()
    price = IntField()
# 3.Try insert an item
# new_item = Item(
#     title="Đài cũ",
#     image="http://audioidiots.com/Sony/catalogi/1986%20hifi/middel/p037i1.jpg",
#     description="Đài cũ giá cao",
#     price=500000
# )
# new_item.save()

@app.route('/')
def index():
    items = Item.objects()
    return render_template('index.html', items = items)

@app.route('/add_item', methods=['GET','POST'])
def add_item():
    if request.method == 'GET':
        return render_template('add_item.html')
    elif request.method == 'POST':
        #1 Lấy data từ form
        form = request.form
        title = form['title']
        image = form['image']
        description = form['description']
        price = form['price']
        #2 Thêm vào database
        new_item = Item(title = title, image = image, description = description, price = price)
        new_item.save()

        return "Ok baby"

@app.route('/admin')
def admin():
    return render_template('admin.html', items = Item.objects())

@app.route('/edit_item/<item_id>', methods = ['GET', 'POST'])
def edit_item(item_id):
    item = Item.objects().with_id(item_id)
    if request.method == 'GET':
        return render_template('edit_item.html', item=item)
    elif request.method == 'POST':
        form = request.form
        title = form['title']
        description = form['description']
        image = form['image']
        price = form['price']

        item.update(title = title, description = description, image = image, price = price)
        flash("Đã sửa thành công!")
        return render_template('edit_item.html', item = Item.objects().with_id(item_id))

if __name__ == '__main__':
  app.run(debug=True)
