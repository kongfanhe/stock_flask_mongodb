from flask import Flask
from minip_user.routes import user_info_blue, toggle_favorite_blue
from stock_market.routes import stocks_blue, stock_predict_blue, market_predict_blue

app = Flask(__name__)

app.register_blueprint(user_info_blue)
app.register_blueprint(toggle_favorite_blue)
app.register_blueprint(stocks_blue)
app.register_blueprint(stock_predict_blue)
app.register_blueprint(market_predict_blue)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8856, debug=True)
