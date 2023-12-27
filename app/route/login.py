# モデルアフィルからUserクラスをimport
from models import User
from flask import flash, redirect, render_template, request, url_for

# current_userとlogin_userをimport
from flask_login import current_user, login_user

from . import main


@main.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    if request.method == "GET":
        return render_template("login.html")
    # if not validation.check:
    # 	return render_template("login.html", title="Sign In")

    user = User.query.filter_by(username=form.username.data).one_or_none()
    # 合致するユーザーが存在しないもしくはパスワードが誤っている場合
    if user is None or not user.check_password(form.password.data):
        # flashを表示
        flash("Invalid username or password")
        # loginページにリダイレクト
        return redirect(url_for("login"))
    # 取得したユーザーをloginユーザーとして登録
    login_user(user, remember=form.remember_me.data)
    # 本機能実装前に記述していたトップページへのリダイレクトは不要なので削除する
    # return redirect(url_for('index'))
    # ログイン後の遷移先(アクセスしようとしていたページ)のurlを取得
    next_page = request.args.get("next")
    # 遷移先が存在しない場合もしくはそのurlのnetloc(ファーストレベルのドメイン)がある場合
    if not next_page:
        # トップページにリダイレクト
        next_page = url_for("index")
    # アクセスしようとしていたページにリダイレクトバック
    return redirect(next_page)
