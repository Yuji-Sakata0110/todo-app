# Backend APIs

#### swagger から生成した OpenApi ドキュメント

[openapi.json](./openapi.json)

1. /auth/token/access/
2. /auth/token/refresh/
3. /auth/signup/
4. /auth/signin/
5. /auth/signout/
6. /todos/
7. /todos/<int:pk>/

## 各 API の説明

### 1. POST: /auth/token/

#### Header

なし。

#### Body

```json
{
  "username": "sample2@gmail.com",
  "password": "aaa"
}
```

#### Response

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMjM2NDI3NiwiaWF0IjoxNjk5NzcyMjc2LCJqdGkiOiI1YjBmNDQxMzRjMDY0OTk2YWI5YTFkYWI0MWY3NTFiNCIsInVzZXJfaWQiOiJjZTY3OTU0MS1hYmI2LTRmOGQtOGJjYi0zMWFlNTBhYjU3NzUifQ.-9kxYc_jTq-vg9vxc_Ac_q_jLFKWiZDzpzz2vXowAww",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5NzczMTc2LCJpYXQiOjE2OTk3NzIyNzYsImp0aSI6ImNkN2ZmY2UzYzhkNzRkZTU5NDc5Yzg4ZGU0ZWYwYTA1IiwidXNlcl9pZCI6ImNlNjc5NTQxLWFiYjYtNGY4ZC04YmNiLTMxYWU1MGFiNTc3NSJ9.wn93kJhGL8kRPMvMjm9Sxr2eF0cr-g6gzLlU2GAPXJI"
}
```

### 3. POST: /auth/signin/

#### Header

```json
{
  "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5NzczMTc2LCJpYXQiOjE2OTk3NzIyNzYsImp0aSI6ImNkN2ZmY2UzYzhkNzRkZTU5NDc5Yzg4ZGU0ZWYwYTA1IiwidXNlcl9pZCI6ImNlNjc5NTQxLWFiYjYtNGY4ZC04YmNiLTMxYWU1MGFiNTc3NSJ9.wn93kJhGL8kRPMvMjm9Sxr2eF0cr-g6gzLlU2GAPXJI"
}
```

※　認証に有効な Token を生成し、挿入する。

#### Body

```json
{
  "username": "sample2@gmail.com",
  "password": "aaa"
}
```

#### Response

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5NzczMjUyLCJpYXQiOjE2OTk3NzIzNTIsImp0aSI6ImE5NjczYTMxMGI0OTRiMzk5MWZkZWNkNGRlOWUyOWViIiwidXNlcl9pZCI6ImFkZTU4Zjc0LWVkOTAtNDE3ZS04ZjY4LWQ1ZWE2YjZhMDdjYiJ9.A-TFo6dix9dLKcXET42nPHupIKn3G5I3b8Y8XVeR1HY",
  "login_status": true
}
```

#### API 機能概要

サインインを行う機能である。<br>
Header に JWTToken を利用する必要がある。<br>
Body に入力された username, password を利用し、バックエンドで認証を行う。<br>
401 エラーが発生し、Token が有効でない場合、Token の再生成を実施する。（1. /auth/token/ を実施）

#### エラーハンドリングについて

#### 関数テスト について

#### 非機能要件
