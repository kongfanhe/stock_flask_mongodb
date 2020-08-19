from flask import request, Blueprint
import requests
from pymongo import MongoClient


user_info_blue = Blueprint("user_info", __name__)
toggle_favorite_blue = Blueprint("toggle_favorite", __name__)


app_id = "fill-in-your-appid"
app_secret = "fill-in-your-app-secret"


def mongo_collection(db_name, collection_name):
    client = MongoClient('mongodb://localhost:27017/')
    db = client[db_name]
    collection = db[collection_name]
    return collection


def openid_by_wxcode(wxcode):
    url = "https://api.weixin.qq.com/sns/jscode2session"
    url += "?appid=" + app_id
    url += "&secret=" + app_secret
    url += "&js_code=" + wxcode
    url += "&grant_type=authorization_code"
    response = requests.get(url)
    data = response.json()
    openid = data["openid"]
    return openid


def get_user_by_openid(openid):
    users = mongo_collection("minip", "users")
    user = users.find_one({"openid": openid})
    if user is None:
        user = {"openid": openid, "my_codes": []}
        users.insert_one(user)
    return user


@user_info_blue.route("/user_info", methods=["POST"])
def user_info():
    data = request.get_json()
    wxcode = data["wxcode"]
    openid = openid_by_wxcode(wxcode)
    u = get_user_by_openid(openid)
    del u["_id"]
    return u


@toggle_favorite_blue.route("/toggle_favorite", methods=["POST"])
def toggle_favorite():
    data = request.get_json()
    wxcode = data["wxcode"]
    openid = openid_by_wxcode(wxcode)
    u = get_user_by_openid(openid)
    code = data["code"]
    my_codes = u["my_codes"].copy()
    if code in my_codes:
        my_codes.remove(code)
    else:
        my_codes.append(code)
    users = mongo_collection("minip", "users")
    users.update_one(u, {"$set": {"my_codes": my_codes}})
    u = get_user_by_openid(openid)
    del u["_id"]
    return u
