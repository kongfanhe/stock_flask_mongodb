# Flask and MongoDB backend API

## Introduction
This repo serves as a backend API for [Wechat Miniprogram Stock repo](https://github.com/kongfanhe/stock_weixin_miniprogram). It also requires the stock prediction results from [this repo](https://github.com/kongfanhe/stock_lstm_tensorflow). Make sure you have read the previously mentioned repos and continue.


## How to Use
1. Install Python >= 3.6, MongoDB.
2. Install necessary packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Go to [Wechat Platform](https://mp.weixin.qq.com/), register or find your AppID and [AppSecret](https://developers.weixin.qq.com/doc/offiaccount/en/Getting_Started/Getting_Started_Guide.html).

4. Modify the following two lines of code:
    ```python
    app_id = "fill-in-your-appid"
    app_secret = "fill-in-your-app-secret"
    ```
    in the file **/minip_user/routes.py**

5. Deploy the Flask server:
    ```bash
    python flask_server.py
    ```
    It will start listening to port *8856*, if you need to change the port number, or set to production mode, modify this line of code:
    ```python
    app.run(host="127.0.0.1", port=8856, debug=True)
    ```
    in the file **/flask_server.py**

## Note
* In case you want to **publish your APP**, Wechat requires [HTTPS certificate and ICP license](https://developers.weixin.qq.com/miniprogram/en/dev/framework/ability/network.html) for the backend API.
* In case you want to deploy locally, there is no restriction on the HTTPS and ICP. However you need to setup this option on the [Wechat Devtools](https://developers.weixin.qq.com/miniprogram/en/dev/devtools/settings.html#Appearance-Settings).

