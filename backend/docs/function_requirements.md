# 機能要件

ルーティングには DjnagoRestFramework を利用する。<br>
Model, Serializer, View を利用し、API を実装する。<br>
追加した Model は Admin に追加する。

## 認証認可

#### 認証方法

JWT による認証を実施する。

#### 保存場所

サーバーサイド。HttpOnlyCookie を利用する。

#### JWT の設定について（setting.py）

- ACCESS_TOKEN: 15 分有効
- REFRESH_TOKEN: 30 日有効
- ROTATE_REFRESH_TOKENS: 有効
- UPDATE_LAST_LOGIN: 有効

#### Backend APIs

[Backend APIs](./api.md)

## swagger-ui による API ドキュメントの自動生成

Django アプリに swagger-ui をインストールする。

#### 利用方法

Django アプリを起動し、下記のルーティングをブラウザに記入する。

routing

```
http://localhost:8000/swagger/
```

#### swagger-ui から生成した API ドキュメント

###### 開発環境

[openapi.json](./apis/openapi.json)
