from flask import Flask, render_template, request
import mlab;
from mongoengine import *

mlab.connect()
class Item(Document):
    title = StringField()
    image = StringField()
    description = StringField()
    price = IntField()

app = Flask(__name__)


@app.route('/')
def index():
    data = Item.objects()
    return render_template('index.html', items = data)

@app.route('/add_item', methods = ['GET', 'POST'])
def add_item():
    if request.method == 'GET':
        return render_template('add_item.html')
    elif request.method == 'POST':
        form = request.form
        title = form['title']
        image = form['image']
        description = form['description']
        price = form['price']
        new_item = Item(title = title, image = image, description = description, price = price)
        new_item.save()
        
    return("Đã thêm thành công")



if __name__ == '__main__':
  app.run(debug=True)
