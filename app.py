# 簡単なindexページの作成を行っています。
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "index page"

# WARN: これを開発する時は、ryamaを閉じてください。 (docker-compose の contianer-name と port が 競合するため。)
# TODO: あと tailwind css を入れてさっさと開発しよう。
