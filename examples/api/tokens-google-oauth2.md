# /tokens/google/oauth2

## Redirect user to google for oauth2.0

### GET /tokens/google/oauth2

### CURL

```bash
curl -- "$URL/tokens/google/oauth2"
```

### Response: 302 Found

#### Headers

* location: https://accounts.google.com/o/oauth2/v2/auth?client_id=foobarbaz&response_type=code&scope=openid%20email%20profile&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2Ftokens%2Fgoogle%2Fcb&state=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjQ2OTgyODIsInJlZHVybCI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImlkIjoiZjgyNTEwOTMzYjAwMTliOTE4MmY2ZDAxNWEwODYxYWEzNzk1M2ZkZjViZWIxNzlmZGJlZTA0ODViMTQyOTlmOCJ9.z_vmLYQTw7PUeX3yhB7Sdec7puuqvH24ne5nR_hY4JY&access_type=offline
* set-cookie: yhttp-csrf-token=f82510933b0019b9182f6d015a0861aa37953fdf5beb179fdbee0485b14299f8; HttpOnly; Max-Age=60; Path=/tokens/google/oauth2; SameSite=Strict; Secure
* content-length: 0

---

## WHEN: Obtain OAuth2.0 token with refresh token

### GET /tokens/google/oauth2

### Request Headers

* cookie: yhttp-refresh-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwicmVmcmVzaCI6dHJ1ZSwiZXhwIjoxNzI2ODgxMzcxLCJlbWFpbCI6ImdvZEBheW90Lm5ldCJ9.XcLGlUF65ZNZiyohF-h-mWJWm9zry9iGS22L8Wwf0Jc

### CURL

```bash
curl -H "cookie: yhttp-refresh-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwicmVmcmVzaCI6dHJ1ZSwiZXhwIjoxNzI2ODgxMzcxLCJlbWFpbCI6ImdvZEBheW90Lm5ldCJ9.XcLGlUF65ZNZiyohF-h-mWJWm9zry9iGS22L8Wwf0Jc" -- "$URL/tokens/google/oauth2"
```

### Response: 302 Found

#### Headers

* location: https://accounts.google.com/o/oauth2/v2/auth?client_id=foobarbaz&response_type=code&scope=openid%20email%20profile&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2Ftokens%2Fgoogle%2Fcb&state=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjQ2OTgyODIsInJlZHVybCI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImlkIjoiM2ZhYWQ0NDQ2YjAxY2UzNGNiOThjNGYyOWVkNWEwNTIwZDQxNGYwMDJlZmM2OTUzYmE3MjVkNWNkYjBjZTU3NCJ9.pkQ_qK19cDEJAWScWlGnyPijPRu0J-_TOOIGP1aXRi0&access_type=offline&login_hint=god%40ayot.net
* set-cookie: yhttp-csrf-token=3faad4446b01ce34cb98c4f29ed5a0520d414f002efc6953ba725d5cdb0ce574; HttpOnly; Max-Age=60; Path=/tokens/google/oauth2; SameSite=Strict; Secure
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

