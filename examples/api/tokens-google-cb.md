# /tokens/google/cb

## Redirect back from google oauth2.0 server and login

### GET /tokens/google/cb

### Query Strings

Name | Example
--- | ---
code | 4/0AX4XfWitAl4eZ2U7eJ7CYbFgl0HrKjUxrAuD5TiXfOV1ZHfcSWjxM1u6z_w8IZMXlLuJLg
scope | email+profile+https://www.googleapis.com/auth/userinfo.email+https://www.googleapis.com/auth/userinfo.profile+openid
state | eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjUxNDIwNDYsInJlZHVybCI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImlkIjoiNWNmNDI0ZjRhN2MwMzliZGFmZDA0YjIwODRiZTA4ODlkMDdjNTNkNjUwZGFlYWE4N2U3ZjEwNTgzODkzMzY1ZiJ9.pNaFh2VW78WMA0ls93eY4cBGlLNvUKxuVRe6fT1ZDaI

### Request Headers

* Cookie: yhttp-csrf-to...f10583893365f

### CURL

```bash
curl -H "Cookie: yhttp-csrf-to...f10583893365f" -- "$URL/tokens/google/cb?code=4%2F0AX4XfWitAl4eZ2U7eJ7CYbFgl0HrKjUxrAuD5TiXfOV1ZHfcSWjxM1u6z_w8IZMXlLuJLg&scope=email%2Bprofile%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile%2Bopenid&state=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjUxNDIwNDYsInJlZHVybCI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImlkIjoiNWNmNDI0ZjRhN2MwMzliZGFmZDA0YjIwODRiZTA4ODlkMDdjNTNkNjUwZGFlYWE4N2U3ZjEwNTgzODkzMzY1ZiJ9.pNaFh2VW78WMA0ls93eY4cBGlLNvUKxuVRe6fT1ZDaI"
```

### Response: 302 Found

#### Headers

* location: http://localhost:8080
* set-cookie: yhttp-refresh-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwicmVmcmVzaCI6dHJ1ZSwiZXhwIjoxNzI3NzMzOTg2LCJyb2xlcyI6WyJnb2QiXX0.3L2cAz1-WsTeZ2jvZyEReqlKnlbGYwcwoKw3w5hLGDA; HttpOnly; Max-Age=2592000; Path=/tokens/google/cb; SameSite=Strict; Secure
* content-length: 0

---

## WHEN: Login again

### GET /tokens/google/cb

### CURL

```bash
curl -H "Cookie: yhttp-csrf-to...f10583893365f" -- "$URL/tokens/google/cb?code=4%2F0AX4XfWitAl4eZ2U7eJ7CYbFgl0HrKjUxrAuD5TiXfOV1ZHfcSWjxM1u6z_w8IZMXlLuJLg&scope=email%2Bprofile%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile%2Bopenid&state=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjUxNDIwNDYsInJlZHVybCI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImlkIjoiNWNmNDI0ZjRhN2MwMzliZGFmZDA0YjIwODRiZTA4ODlkMDdjNTNkNjUwZGFlYWE4N2U3ZjEwNTgzODkzMzY1ZiJ9.pNaFh2VW78WMA0ls93eY4cBGlLNvUKxuVRe6fT1ZDaI"
```

### Response: 302 Found

#### Headers

* location: http://localhost:8080
* set-cookie: yhttp-refresh-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwicmVmcmVzaCI6dHJ1ZSwiZXhwIjoxNzI3NzMzOTg2LCJyb2xlcyI6WyJnb2QiXX0.3L2cAz1-WsTeZ2jvZyEReqlKnlbGYwcwoKw3w5hLGDA; HttpOnly; Max-Age=2592000; Path=/tokens/google/cb; SameSite=Strict; Secure
* content-length: 0

---

## WHEN: Google say 403 during key exchange

### GET /tokens/google/cb

### CURL

```bash
curl -H "Cookie: yhttp-csrf-to...f10583893365f" -- "$URL/tokens/google/cb?code=4%2F0AX4XfWitAl4eZ2U7eJ7CYbFgl0HrKjUxrAuD5TiXfOV1ZHfcSWjxM1u6z_w8IZMXlLuJLg&scope=email%2Bprofile%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile%2Bopenid&state=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjUxNDIwNDYsInJlZHVybCI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImlkIjoiNWNmNDI0ZjRhN2MwMzliZGFmZDA0YjIwODRiZTA4ODlkMDdjNTNkNjUwZGFlYWE4N2U3ZjEwNTgzODkzMzY1ZiJ9.pNaFh2VW78WMA0ls93eY4cBGlLNvUKxuVRe6fT1ZDaI"
```

### Response: 401 Unauthorized

#### Headers

* content-length: 846

---

## WHEN: Google say 400 during key exchange

### GET /tokens/google/cb

### CURL

```bash
curl -H "Cookie: yhttp-csrf-to...f10583893365f" -- "$URL/tokens/google/cb?code=4%2F0AX4XfWitAl4eZ2U7eJ7CYbFgl0HrKjUxrAuD5TiXfOV1ZHfcSWjxM1u6z_w8IZMXlLuJLg&scope=email%2Bprofile%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile%2Bopenid&state=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjUxNDIwNDYsInJlZHVybCI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImlkIjoiNWNmNDI0ZjRhN2MwMzliZGFmZDA0YjIwODRiZTA4ODlkMDdjNTNkNjUwZGFlYWE4N2U3ZjEwNTgzODkzMzY1ZiJ9.pNaFh2VW78WMA0ls93eY4cBGlLNvUKxuVRe6fT1ZDaI"
```

### Response: 401 Unauthorized

#### Headers

* content-length: 846

---

## WHEN: Token received from google is malformed

### GET /tokens/google/cb

### CURL

```bash
curl -H "Cookie: yhttp-csrf-to...f10583893365f" -- "$URL/tokens/google/cb?code=4%2F0AX4XfWitAl4eZ2U7eJ7CYbFgl0HrKjUxrAuD5TiXfOV1ZHfcSWjxM1u6z_w8IZMXlLuJLg&scope=email%2Bprofile%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile%2Bopenid&state=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjUxNDIwNDYsInJlZHVybCI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImlkIjoiNWNmNDI0ZjRhN2MwMzliZGFmZDA0YjIwODRiZTA4ODlkMDdjNTNkNjUwZGFlYWE4N2U3ZjEwNTgzODkzMzY1ZiJ9.pNaFh2VW78WMA0ls93eY4cBGlLNvUKxuVRe6fT1ZDaI"
```

### Response: 401 Unauthorized

#### Headers

* content-length: 846

