# Docker の 説明

> このプロジェクトで使う,Docker の説明をしています。

- 更新が来たとき
  - `docker compose up -d --build`
- 起動
  - `docker compose up -d`
- 停止
  - `docker compose down`
- ログの見方
  - `docker compose logs app` (`app` の部分を `db` に変えることで database のログを見れます)<br>
  - `docker compose logs app -f` とすることで、ログをずっと表示して置けるので、こっちを推奨
- docker の 中で実行
  - `docker compose exec app flask db migrate -m "Add: ~~~~~~~~"`
