from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  

app = Flask(__name__)

client = MongoClient('localhost', 27017)  
db = client.stat418  


## HTML
@app.route('/')
def home():
    return render_template('index.html')



## API 
@app.route('/review', methods=['POST'])
def write_review():
    # title_receive 
    title_receive = request.form['title_give']
    # author_receive
    author_receive = request.form['author_give']
    # review_receive
    review_receive = request.form['review_give']

    # create review for db
    review = {
        'title': title_receive,
        'author': author_receive,
        'review': review_receive
    }
    # reviews 
    db.reviews.insert_one(review)
    # return success
    return jsonify({'result': 'success', 'msg': 'successfully added.'})


@app.route('/review', methods=['GET'])
def read_reviews():
    reviews = list(db.reviews.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
