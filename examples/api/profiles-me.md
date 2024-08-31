# /profiles/me

## Get authenticated user's profile

### GET /profiles/me

### Request Headers

* Authorization: Bearer eyJhbG...vjN0In58SH-kc

### CURL

```bash
curl -H "Authorization: Bearer eyJhbG...vjN0In58SH-kc" -- "$URL/profiles/me"
```

### Response: 200 OK

#### Headers

* content-length: 232

#### Body

Content-Type: application/json

```json
{
  "nickname": "god",
  "nickname_isdirty": true,
  "timezone": "00:00",
  "locale": null,
  "avatar": null,
  "roles": [
    "god"
  ],
  "created_at": "2024-08-22T03:30:00",
  "modified_at": "2024-08-22T03:30:00",
  "id": 1,
  "email": "god@ayot.net",
  "name": "God",
  "phone": null
}
```

---

## WHEN: Authorization header is not passed

### GET /profiles/me

### CURL

```bash
curl -- "$URL/profiles/me"
```

### Response: 401 Unauthorized

#### Headers

* content-length: 703

---

## WHEN: User is already deleted

### GET /profiles/me

### CURL

```bash
curl -H "Authorization: Bearer eyJhbG...vjN0In58SH-kc" -- "$URL/profiles/me"
```

### Response: 404 Not Found

#### Headers

* content-length: 1160

## Updating profile by the owner

### UPDATE /profiles/me

### Form

Name | Required | Type | Example
--- | --- | --- | ---
name | ? | ? | Bob
phone | ? | ? | +98 (912) 111 1111

### Request Headers

* Authorization: Bearer eyJhbG...vjN0In58SH-kc

### CURL

```bash
curl -X UPDATE -F "name=Bob" -F "phone=+98 (912) 111 1111" -H "Authorization: Bearer eyJhbG...vjN0In58SH-kc" -- "$URL/profiles/me"
```

### Response: 200 OK

#### Headers

* content-length: 248

#### Body

Content-Type: application/json

```json
{
  "nickname": "god",
  "nickname_isdirty": true,
  "timezone": "00:00",
  "locale": null,
  "avatar": null,
  "roles": [
    "god"
  ],
  "created_at": "2024-08-22T03:30:00",
  "modified_at": "2024-08-22T03:30:00",
  "id": 1,
  "email": "god@ayot.net",
  "name": "Bob",
  "phone": "+98 (912) 111 1111"
}
```

---

## WHEN: Short nickname

### UPDATE /profiles/me

### Form

Name | Required | Type | Example
--- | --- | --- | ---
nickname | ? | ? | 

### CURL

```bash
curl -X UPDATE -F "nickname=" -H "Authorization: Bearer eyJhbG...vjN0In58SH-kc" -- "$URL/profiles/me"
```

### Response: 701 nickname: Length must be between 1 and 12 characters

#### Headers

* content-length: 1077

---

## WHEN: Long nickname

### UPDATE /profiles/me

### Form

Name | Required | Type | Example
--- | --- | --- | ---
nickname | ? | ? | xxxxxxxxxxxxx

### CURL

```bash
curl -X UPDATE -F "nickname=xxxxxxxxxxxxx" -H "Authorization: Bearer eyJhbG...vjN0In58SH-kc" -- "$URL/profiles/me"
```

### Response: 701 nickname: Length must be between 1 and 12 characters

#### Headers

* content-length: 1077

---

## WHEN: Update nickname

### UPDATE /profiles/me

### Form

Name | Required | Type | Example
--- | --- | --- | ---
nickname | ? | ? | Bob

### CURL

```bash
curl -X UPDATE -F "nickname=Bob" -H "Authorization: Bearer eyJhbG...vjN0In58SH-kc" -- "$URL/profiles/me"
```

### Response: 200 OK

#### Headers

* content-length: 249

#### Body

Content-Type: application/json

```json
{
  "nickname": "Bob",
  "nickname_isdirty": false,
  "timezone": "00:00",
  "locale": null,
  "avatar": null,
  "roles": [
    "god"
  ],
  "created_at": "2024-08-22T03:30:00",
  "modified_at": "2024-08-22T03:30:00",
  "id": 1,
  "email": "god@ayot.net",
  "name": "Bob",
  "phone": "+98 (912) 111 1111"
}
```

---

## WHEN: Update locale

### UPDATE /profiles/me

### Form

Name | Required | Type | Example
--- | --- | --- | ---
locale | ? | ? | en-US

### CURL

```bash
curl -X UPDATE -F "locale=en-US" -H "Authorization: Bearer eyJhbG...vjN0In58SH-kc" -- "$URL/profiles/me"
```

### Response: 200 OK

#### Headers

* content-length: 252

#### Body

Content-Type: application/json

```json
{
  "nickname": "Bob",
  "nickname_isdirty": false,
  "timezone": "00:00",
  "locale": "en-US",
  "avatar": null,
  "roles": [
    "god"
  ],
  "created_at": "2024-08-22T03:30:00",
  "modified_at": "2024-08-22T03:30:00",
  "id": 1,
  "email": "god@ayot.net",
  "name": "Bob",
  "phone": "+98 (912) 111 1111"
}
```

---

## WHEN: Update timezone

### UPDATE /profiles/me

### Form

Name | Required | Type | Example
--- | --- | --- | ---
timezone | ? | ? | +03:30

### CURL

```bash
curl -X UPDATE -F "timezone=+03:30" -H "Authorization: Bearer eyJhbG...vjN0In58SH-kc" -- "$URL/profiles/me"
```

### Response: 200 OK

#### Headers

* content-length: 253

#### Body

Content-Type: application/json

```json
{
  "nickname": "Bob",
  "nickname_isdirty": false,
  "timezone": "+03:30",
  "locale": "en-US",
  "avatar": null,
  "roles": [
    "god"
  ],
  "created_at": "2024-08-22T03:30:00",
  "modified_at": "2024-08-22T03:30:00",
  "id": 1,
  "email": "god@ayot.net",
  "name": "Bob",
  "phone": "+98 (912) 111 1111"
}
```

---

## WHEN: Member deleted

### UPDATE /profiles/me

### CURL

```bash
curl -X UPDATE -F "name=Bob" -F "phone=+98 (912) 111 1111" -H "Authorization: Bearer eyJhbG...vjN0In58SH-kc" -- "$URL/profiles/me"
```

### Response: 404 Not Found

#### Headers

* content-length: 1163

