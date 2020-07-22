# Jiji - Remix

This application exposes a jiji like restful api

## Create a user account
POST: `/api/v1/accounts/`

Data:

```json
{
    "first_name": "john",
    "last_name": "doe",
    "email": "johndoe@gmail.com",
    "password": "foobar",
    "residence_state": "lagos"
}
```
Response:
`status_code: 201`
```json
{
    "first_name": "johny",
    "last_name": "doe",
    "residence_state": "abuja",
    "email": "johny@gmail.com",
    "user_id": "0ede2bc8-c6d5-4f77-87ca-d1a8c7eef048"
}
```

## Login 
POST: `/api/v1/accounts/login/`

Data:

```json
{
    "email": "johndoe@gmail.com",
    "password": "foobar"
}
```
Response (JWT access & refresh tokens):
`status_code: 200`
```json

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU5NTU0MTU0NywianRpIjoiOWQwNTJhZDRmZmI3NGEyNjkxNWIxMzViNjBjMzg2ZDYiLCJ1c2VyX2lkIjoiZTQwYzM5YmUtZWY5Mi00NjhmLTljOTktY2M3MTQ5ZTdkMTY2In0.KtA3ylrtcmri7XWdnaclK-q4Lt-E7JlHx-RO92ZE6ks",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk1NDU2MDQ3LCJqdGkiOiJlZGRjMGM1ZmQxMTY0M2E3YjZiN2IyNTgwYzA2ZjA1MiIsInVzZXJfaWQiOiJlNDBjMzliZS1lZjkyLTQ2OGYtOWM5OS1jYzcxNDllN2QxNjYifQ.QOB9GO1hGq5dobcK6-3w0VsRvYwvMe_pBbQtDNwW7oE"
}
```

## Get profile (owner)
GET: `api/v1/accounts/me`

Headers: `Authorization: JWT access_token`

Response (Account profile with items they own and each item having a list of interested buyers): `status_code: 200`

```json
{
    "user_id": "e40c39be-ef92-468f-9c99-cc7149e7d166",
    "email": "john@gmail.com",
    "first_name": "john",
    "last_name": "doe",
    "residence_state": "abuja",
    "items": [
        {
            "item_id": "ITEM_02BT14",
            "sold_to": null,
            "owner": {
                "owner_id": "e40c39be-ef92-468f-9c99-cc7149e7d166",
                "first_name": "john",
                "last_name": "doe",
                "residence_state": "abuja"
            },
            "interested_buyers": [
                {
                    "id": 6,
                    "name": "joseph doe",
                    "email": "josephdoe@hotmail.com",
                    "location": "lagos",
                    "item": "ITEM_02BT14"
                }
            ],
            "name": "S9+ Ghana used",
            "description": "Clean UK used S9+",
            "price": "160000.00",
            "image": "http://localhost:8000/media/item_gallery/dummy_img.jpg",
            "is_sold": false,
            "created_at": "2020-07-21T10:48:58.099754Z",
            "updated_at": "2020-07-21T10:48:58.099805Z"
        }
    ]
}
```
## Get Store Items
GET: `/api/v1/store/`

Headers: `Authorization: JWT access_token`

Response (A list of items available for sale on the platform): `status_code: 200`

```json
[
    {
        "item_id": "ITEM_F4E1OJ",
        "sold_to": null,
        "owner": {
            "owner_id": "40b28a27-3424-4999-97df-fd8446416572",
            "first_name": "david",
            "last_name": "doe",
            "residence_state": "lagos"
        },
        "interested_buyers": [
            {
                "id": 2,
                "name": "joseph doe",
                "email": "josephdoe@hotmail.com",
                "location": "lagos",
                "item": "ITEM_F4E1OJ"
            }
        ],
        "name": "S9+ Foriegn used",
        "description": "Clean UK used S9+",
        "price": "140000.00",
        "image": "http://localhost:8000/media/item_gallery/abc_spring_RYwFcQw.png",
        "is_sold": false,
        "created_at": "2020-07-20T15:33:27.675114Z",
        "updated_at": "2020-07-20T15:33:27.675198Z"
    },
    {
        "item_id": "ITEM_02BT14",
        "sold_to": null,
        "owner": {
            "owner_id": "e40c39be-ef92-468f-9c99-cc7149e7d166",
            "first_name": "john",
            "last_name": "doe",
            "residence_state": "abuja"
        },
        "interested_buyers": [
            {
                "id": 6,
                "name": "joseph doe",
                "email": "josephdoe@hotmail.com",
                "location": "lagos",
                "item": "ITEM_02BT14"
            }
        ],
        "name": "S9+ Ghana used",
        "description": "Clean UK used S9+",
        "price": "160000.00",
        "image": "http://localhost:8000/media/item_gallery/dummy_img.jpg",
        "is_sold": false,
        "created_at": "2020-07-21T10:48:58.099754Z",
        "updated_at": "2020-07-21T10:48:58.099805Z"
    }
]
```

## Create Store Items
POST: `/api/v1/store/`

Headers: `Authorization: JWT access_token`

Response (The details of the created store item): `status_code: 201`

```json
{
    "item_id": "ITEM_MHTJNF",
    "sold_to": null,
    "owner": {
        "owner_id": "e40c39be-ef92-468f-9c99-cc7149e7d166",
        "first_name": "john",
        "last_name": "doe",
        "residence_state": "abuja"
    },
    "interested_buyers": [],
    "name": "5000mAh power bank",
    "description": "7 days lasting power bank",
    "price": "16000.00",
    "image": "http://localhost:8000/media/item_gallery/dummy_img.jpg",
    "is_sold": false,
    "created_at": "2020-07-22T22:13:33.848311Z",
    "updated_at": "2020-07-22T22:13:33.848348Z"
}
```

## Get, Update & Delete a specific Store Item
All the fields of a store item are updateable. 

### For GET
GET: `/api/v1/store/ITEM_MHTJNF/`
Headers: `Authorization: JWT access_token`

### For Update
PATCH: `/api/v1/store/ITEM_MHTJNF/`
Headers: `Authorization: JWT access_token`

DATA: the json fields you want to update

When an item has been sold a PATCH request is sent with the following data:
> `sold_to` is the id of the interested buyer
```json
    {
        "sold_to": "1",
        "is_sold": true,
    }
```
### For Delete
DELETE: `/api/v1/store/ITEM_MHTJNF/`
Headers: `Authorization: JWT access_token`


## Create a buyer interest

POST: `/api/v1/store/ITEM_02BT14/interested/`

Response: `status_code: 201`

```json
{
    "id": 7,
    "name": "johny doe",
    "email": "johny@hotmail.com",
    "location": "lagos",
    "item": "ITEM_MHTJNF"
}

```