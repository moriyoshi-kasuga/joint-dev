```mermaid
erDiagram
  USER ||--|| PROFILE : profile
  USER ||--o{ THREAD: "作成したスレッド"
  THREAD }o--o{ TAG: "そのスレッドのカテゴリー"
  THREAD ||--o{ COMMENT: "そのスレッドのコメント"
  USER {
    UUID id
    String name
    String email
    String password
    THREAD[] threads

    DATA created_at
  }
  PROFILE {
    UUID id
    UUID userID
    JSONB settings
  }
  THREAD {
    UUID id
    USER user
    String title
    String content

    COMMENT[] comments
    TAG[] tags

    DATA created_at
  }
  COMMENT {
    UUID id
    String content
    USER user
    THREAD thread
    Integer number

    DATA created_at
  }
  TAG {
    String name
    String description
  }
```
