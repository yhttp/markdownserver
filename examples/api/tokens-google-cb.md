# /tokens/google/cb

## Redirect back from google oauth2.0 server and login

### GET /tokens/google/cb

### Query Strings

Name | Example
--- | ---
code | 4/0AX4XfWitAl4eZ2U7eJ7CYbFgl0HrKjUxrAuD5TiXfOV1ZHfcSWjxM1u6z_w8IZMXlLuJLg
scope | email+profile+https://www.googleapis.com/auth/userinfo.email+https://www.googleapis.com/auth/userinfo.profile+openid
state | eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjQ2OTgyODIsInJlZHVybCI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImlkIjoiM2ZhYWQ0NDQ2YjAxY2UzNGNiOThjNGYyOWVkNWEwNTIwZDQxNGYwMDJlZmM2OTUzYmE3MjVkNWNkYjBjZTU3NCJ9.pkQ_qK19cDEJAWScWlGnyPijPRu0J-_TOOIGP1aXRi0

### Request Headers

* Cookie: yhttp-csrf-token=3faad4446b01ce34cb98c4f29ed5a0520d414f002efc6953ba725d5cdb0ce574

### CURL

```bash
curl -H "Cookie: yhttp-csrf-token=3faad4446b01ce34cb98c4f29ed5a0520d414f002efc6953ba725d5cdb0ce574" -- "$URL/tokens/google/cb?code=4%2F0AX4XfWitAl4eZ2U7eJ7CYbFgl0HrKjUxrAuD5TiXfOV1ZHfcSWjxM1u6z_w8IZMXlLuJLg&scope=email%2Bprofile%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile%2Bopenid&state=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjQ2OTgyODIsInJlZHVybCI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImlkIjoiM2ZhYWQ0NDQ2YjAxY2UzNGNiOThjNGYyOWVkNWEwNTIwZDQxNGYwMDJlZmM2OTUzYmE3MjVkNWNkYjBjZTU3NCJ9.pkQ_qK19cDEJAWScWlGnyPijPRu0J-_TOOIGP1aXRi0"
```

### Response: 302 Found

#### Headers

* location: http://localhost:8080
* set-cookie: yhttp-refresh-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwicmVmcmVzaCI6dHJ1ZSwiZXhwIjoxNzI3MjkwMjIyLCJyb2xlcyI6WyJnb2QiXX0.vAXoLxsLp8TnwZV5O50IPoiOU2T9LXw2GdO-FTV-T_Y; HttpOnly; Max-Age=2592000; Path=/tokens/google/cb; SameSite=Strict; Secure
* content-length: 0

---

## WHEN: Login again

### GET /tokens/google/cb

### CURL

```bash
curl -H "Cookie: yhttp-csrf-token=3faad4446b01ce34cb98c4f29ed5a0520d414f002efc6953ba725d5cdb0ce574" -- "$URL/tokens/google/cb?code=4%2F0AX4XfWitAl4eZ2U7eJ7CYbFgl0HrKjUxrAuD5TiXfOV1ZHfcSWjxM1u6z_w8IZMXlLuJLg&scope=email%2Bprofile%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile%2Bopenid&state=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjQ2OTgyODIsInJlZHVybCI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImlkIjoiM2ZhYWQ0NDQ2YjAxY2UzNGNiOThjNGYyOWVkNWEwNTIwZDQxNGYwMDJlZmM2OTUzYmE3MjVkNWNkYjBjZTU3NCJ9.pkQ_qK19cDEJAWScWlGnyPijPRu0J-_TOOIGP1aXRi0"
```

### Response: 302 Found

#### Headers

* location: http://localhost:8080
* set-cookie: yhttp-refresh-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwicmVmcmVzaCI6dHJ1ZSwiZXhwIjoxNzI3MjkwMjIyLCJyb2xlcyI6WyJnb2QiXX0.vAXoLxsLp8TnwZV5O50IPoiOU2T9LXw2GdO-FTV-T_Y; HttpOnly; Max-Age=2592000; Path=/tokens/google/cb; SameSite=Strict; Secure
* content-length: 0

---

## WHEN: Google say 403 during key exchange

### GET /tokens/google/cb

### CURL

```bash
curl -H "Cookie: yhttp-csrf-token=3faad4446b01ce34cb98c4f29ed5a0520d414f002efc6953ba725d5cdb0ce574" -- "$URL/tokens/google/cb?code=4%2F0AX4XfWitAl4eZ2U7eJ7CYbFgl0HrKjUxrAuD5TiXfOV1ZHfcSWjxM1u6z_w8IZMXlLuJLg&scope=email%2Bprofile%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile%2Bopenid&state=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjQ2OTgyODIsInJlZHVybCI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImlkIjoiM2ZhYWQ0NDQ2YjAxY2UzNGNiOThjNGYyOWVkNWEwNTIwZDQxNGYwMDJlZmM2OTUzYmE3MjVkNWNkYjBjZTU3NCJ9.pkQ_qK19cDEJAWScWlGnyPijPRu0J-_TOOIGP1aXRi0"
```

### Response: 401 Unauthorized

#### Headers

* content-length: 846

---

## WHEN: Google say 400 during key exchange

### GET /tokens/google/cb

### CURL

```bash
curl -H "Cookie: yhttp-csrf-token=3faad4446b01ce34cb98c4f29ed5a0520d414f002efc6953ba725d5cdb0ce574" -- "$URL/tokens/google/cb?code=4%2F0AX4XfWitAl4eZ2U7eJ7CYbFgl0HrKjUxrAuD5TiXfOV1ZHfcSWjxM1u6z_w8IZMXlLuJLg&scope=email%2Bprofile%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile%2Bopenid&state=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjQ2OTgyODIsInJlZHVybCI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImlkIjoiM2ZhYWQ0NDQ2YjAxY2UzNGNiOThjNGYyOWVkNWEwNTIwZDQxNGYwMDJlZmM2OTUzYmE3MjVkNWNkYjBjZTU3NCJ9.pkQ_qK19cDEJAWScWlGnyPijPRu0J-_TOOIGP1aXRi0"
```

### Response: 401 Unauthorized

#### Headers

* content-length: 846

---

## WHEN: Token received from google is malformed

### GET /tokens/google/cb

### CURL

```bash
curl -H "Cookie: yhttp-csrf-token=3faad4446b01ce34cb98c4f29ed5a0520d414f002efc6953ba725d5cdb0ce574" -- "$URL/tokens/google/cb?code=4%2F0AX4XfWitAl4eZ2U7eJ7CYbFgl0HrKjUxrAuD5TiXfOV1ZHfcSWjxM1u6z_w8IZMXlLuJLg&scope=email%2Bprofile%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile%2Bopenid&state=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjQ2OTgyODIsInJlZHVybCI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImlkIjoiM2ZhYWQ0NDQ2YjAxY2UzNGNiOThjNGYyOWVkNWEwNTIwZDQxNGYwMDJlZmM2OTUzYmE3MjVkNWNkYjBjZTU3NCJ9.pkQ_qK19cDEJAWScWlGnyPijPRu0J-_TOOIGP1aXRi0"
```

### Response: 401 Unauthorized

#### Headers

* content-length: 846

