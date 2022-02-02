# I use "line-bot-zzhou" as app name in Heroku 
# I use zzhou0543@gmail.com to do this project in Heroku

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('aGfknePFUkgN7DE3NCqFisVUXUIWa5qHtOUozzT09fYPn2hoEpijjTS7n+qH/9v7iIFD7F6x+evw956VAAKavBn8r+JxhViP09uI6wnBfGucqiC2fXo/YnR8rlvgLPsq1IfDyurXUqiQ2FP1EUjWNQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ab76dfbd55e57c219632343eaef1169a')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = 'I do not understand what you mean.'

    if msg == 'hi':
        r = 'hi'
    elif msg == 'Do you eat?':
        r = 'Not yet.'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()