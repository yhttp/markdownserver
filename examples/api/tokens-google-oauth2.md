# /tokens/google/oauth2

## Redirect user to google for oauth2.0

### GET /tokens/google/oauth2

### CURL

```bash
curl -- "$URL/tokens/google/oauth2"
```

### Response: 302 Found

#### Headers

* location: https://accounts.google.com/o/oauth2/v2/auth?client_id=foobarbaz&response_type=code&scope=openid%20email%20profile&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2Ftokens%2Fgoogle%2Fcb&state=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjUxNDIwNDYsInJlZHVybCI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImlkIjoiZDI5ZWU5ZTc5ZWJmYTVkNGFkMmZhMTViMjcxOWY4OTNiZjNlY2FiYTdhODNkMDNmYTUyYjdmMzk1OGJkMmJjYyJ9.0xtCx-LA2F_MMJAuY5ceYnZlf6euQVQlgVc2etmJeLU&access_type=offline
* set-cookie: yhttp-csrf-token=d29ee9e79ebfa5d4ad2fa15b2719f893bf3ecaba7a83d03fa52b7f3958bd2bcc; HttpOnly; Max-Age=60; Path=/tokens/google/oauth2; SameSite=Strict; Secure
* content-length: 0

---

## WHEN: Obtain OAuth2.0 token with refresh token

### GET /tokens/google/oauth2

### Request Headers

* cookie: yhttp-refresh...iGS22L8Wwf0Jc

### CURL

```bash
curl -H "cookie: yhttp-refresh...iGS22L8Wwf0Jc" -- "$URL/tokens/google/oauth2"
```

### Response: 302 Found

#### Headers

* location: https://accounts.google.com/o/oauth2/v2/auth?client_id=foobarbaz&response_type=code&scope=openid%20email%20profile&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2Ftokens%2Fgoogle%2Fcb&state=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjUxNDIwNDYsInJlZHVybCI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImlkIjoiNWNmNDI0ZjRhN2MwMzliZGFmZDA0YjIwODRiZTA4ODlkMDdjNTNkNjUwZGFlYWE4N2U3ZjEwNTgzODkzMzY1ZiJ9.pNaFh2VW78WMA0ls93eY4cBGlLNvUKxuVRe6fT1ZDaI&access_type=offline&login_hint=god%40ayot.net
* set-cookie: yhttp-csrf-token=5cf424f4a7c039bdafd04b2084be0889d07c53d650daeaa87e7f10583893365f; HttpOnly; Max-Age=60; Path=/tokens/google/oauth2; SameSite=Strict; Secure
* content-length: 0

---

## WHEN: `redurl` has invalid format

### GET /tokens/google/oauth2

### Query Strings

Name | Example
--- | ---
redurl | maformed

### CURL

```bash
curl -- "$URL/tokens/google/oauth2?redurl=maformed"
```

### Response: 702 redurl: Invalid Format

#### Headers

* content-length: 877

---

## WHEN: `redurl` is empty

### GET /tokens/google/oauth2

### Query Strings

Name | Example
--- | ---
redurl | 

### CURL

```bash
curl -- "$URL/tokens/google/oauth2?redurl="
```

### Response: 701 redurl: Length must be between 7 and 2048 characters

#### Headers

* content-length: 937

