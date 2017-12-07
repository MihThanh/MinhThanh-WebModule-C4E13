from flask import Flask, render_template
import mlab
from mongoengine import *
app = Flask(__name__)
mlab.connect()
class Item(Document):
    title= StringField()
    image = StringField()
    description = StringField()
    price = IntField()
food = Item(
    title = 'Món ăn Việt Nam',
    image = 'https://media.foody.vn/res/g18/178106/prof/s640x400/foody-mobile-t1-jpg-559-635809453498630683.jpg',
    description = 'Bánh cuốn',
    price = 250000
)
food.save()
@app.route('/')
def index():
    data = Item.objects()
    return render_template('index.html', items= data)

if __name__ == '__main__':
  app.run(debug=True)
