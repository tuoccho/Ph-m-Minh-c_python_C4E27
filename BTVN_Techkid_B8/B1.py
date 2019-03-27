from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

bien = client.c4e

poem = bien['posts']
new_poem = {
    "title" : 'Gà',
    "author" : ' Phạm Minh Đức',
    "content" : 'Nhà em có một đàn gà \n Chúng thường đi bộ từ nhà ra sân \n Mỗi khi mưa bão ngập sân \n Chúng lại đi bộ từ sân vào nhà \n Bố mẹ em định bắt gà \n Chúng sợ nên chạy từ nhà ra sân \n Nhưng mà em đứng ở sân \n Đàn gà lại chạy từ sân vào nh \n Nói chung là cả đàn gà \n Cứ chạy mãi mãi từ nhà ra sân \n Thế rồi chúng đứng phân vân \n Không biết nên chạy ở sân hay nhà'
}

poem.insert_one(new_poem)