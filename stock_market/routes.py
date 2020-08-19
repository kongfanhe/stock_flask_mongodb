from flask import request, Blueprint
from pymongo import MongoClient


stocks_blue = Blueprint("stocks", __name__)
stock_predict_blue = Blueprint("stock_predict", __name__)
market_predict_blue = Blueprint("market_predict", __name__)


def mongo_collection(db_name, collection_name):
    client = MongoClient('mongodb://localhost:27017/')
    db = client[db_name]
    collection = db[collection_name]
    return collection
    

def get_mongo_document():
    coll = mongo_collection("predict", "record")
    doc = coll.find_one({})
    return doc, coll


@stocks_blue.route("/stocks", methods=["POST"])
def stocks():
    record, _ = get_mongo_document()
    return record["stock_dict"]


@stock_predict_blue.route("/stock_predict", methods=["POST"])
def stock_predict():
    data = request.get_json()
    code = data["code"]
    record, _ = get_mongo_document()
    n = record["predicts"]["codes"].index(code)
    predict = {
        "name": record["stock_dict"][code],
        "code": code,
        "dates": record["predicts"]["dates"],
        "features": ["收盘价", "成交量"],
        "data": [record["predicts"]["close"][n], record["predicts"]["volume"][n]]
    }
    return predict


@market_predict_blue.route("/market_predict", methods=["POST"])
def market_predict():
    record, _ = get_mongo_document()
    sectors = record["sectors"]
    rise = record["rankings"]["rise"]
    fall = record["rankings"]["fall"]
    volume = record["rankings"]["volume"]
    date = record["date"]
    market = {
        "sectors": sectors,
        "rankings": [
            {"title": "涨幅榜", "content": rise},
            {"title": "跌幅榜", "content": fall},
            {"title": "成交量榜", "content": volume}
        ],
        "date": date
    }
    return market
