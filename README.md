# fast_food_fast_api_repo
[![Build Status](https://travis-ci.org/vincentmuriuki/fast_food_fast_api_repo.svg?branch=develop)](https://travis-ci.org/vincentmuriuki/fast_food_fast_api_repo)   <a href="https://codeclimate.com/github/vincentmuriuki/fast_food_fast_api_repo/maintainability"><img src="https://api.codeclimate.com/v1/badges/7738f429b7d55cf0dc91/maintainability" /></a>   [![Coverage Status](https://coveralls.io/repos/github/vincentmuriuki/fast_food_fast_api_repo/badge.svg?branch=ch-add-coveralls-160649712)](https://coveralls.io/github/vincentmuriuki/fast_food_fast_api_repo?branch=ch-add-coveralls-160649712)

This the repo holds the api endpoints for [Fast Food Project](https://github.com/fast_food_fast_api_repo.git). 

In order to test the API endpoints, follow the simple steps outlined below.

* Clone the repository `git clone https://github.com/fast_food_fast_api_repo.git`
Alternatively, you can view the hosted heroku site here[https://fast_food_fast_api_repo.herokuapp.com/api/v1](https://fast_food_fast_api_repo.herokuapp.com/api/v1).

* Create a virtual environment for the application by running the comand```bash
$virtualenv venv
```

* Run ```bash
$pip install -r requirements.txt
``` to install the project dependancies and other third-party library dependancies



* run `python run.py` and test the apis on `POSTMAN` 
```bash
$python run.py
```

You can alternatively use the `heroku` link to test the api's on postman.

Open postman, and try this endpoints

|Endpoint|Function|
|--------|--------|
| `POST /api/v1/orders`|This api creates a new order.
| `GET /api/v1/orders`|This endpoint gets all orders. 
| `GET /api/v1/orders/<id>`|This endpoint gets a specific order, id valid `order_id` is issued.
| `PUT /api/v1/orders/<id>`|This api updates an order status.
| `DELETE /api/v1/orders`|This deletes all orders 
| `DELETE /api/v1/orders/<id>`|This api deletes an order.


## POST place order

In order to test the `POST` endpoint, you need to send a json file `{"name" : "Pizza", "price" : "800", "description": "6 pieces"}`

```json
{
        "name" : "Pizza",
            "price" : "800",
        "description": "6 pieces"
}
```

The other fields such as `status` and `order_id` are automatically generated when an order is placed. The `order_id` is autoincremented according to the orders length.


## GET all orders

When you run the `GET` request before placing an order, it returns an empty dictionary.
```json
{
    "Orders": []
}
```
If there is a history of orders, it should display the whole history.
```json
{
    "Orders": [
        {
            "id": 12,
            "name": "Pizza",
            "price": "800",
            "description": "6 pieces",
            "status": "Pending"
        },
        {
            "id": 13,
            "name": "Nyama Choma",
            "price": "1500",
            "description": "6 Kg",
            "status": "Pending"
        },
        {
            "id": 14,
            "name": "Pizza",
            "price": "1800",
            "description": "8 Pcs",
            "status": "Pending"
        },
        {
            "id": 15,
            "name": "Fish",
            "price": "900",
            "description": "Fry",
            "status": "Pending"
        }
    ]
}
```

## GET specific order by id

This request requires you to issue an `order_id` in order for it to successfully execute. 
Sample output:
```json
{
    "order": {
        "id": 14,
        "name": "Pizza",
        "price": "1800",
        "description": "8 Pcs",
        "status": "Pending"
    }
}
```
If `order_id` is invalid, it throws a `404` error: 
```json
{
    "message": "Order not found"
}
```
## PUT specific order by id
A successful `PUT` update requests updates the order_status to `approved`
```json
{
    "message": "status approved"
}
```

A sample output of an updated order is shown below:
```json
{
    "order": {
        "id": 14,
        "name": "Pizza",
        "price": "1800",
        "description": "8 Pcs",
        "status": "approved"
    }
}
```
If the specified order is not found, the application throws an `order not found` error
```json
{
    "message": "Order not found"
}
```
## DELETE specific order by id

For a successful delete, an `Requested order deleted sucessfuly` message is shown.
```json
{
    "Message": "Requested Order deleted successfully!"
}
```

Else, if an invalid id is issued, the application throws a `404` error 
```json
{
    "message": "Requested Order not found! Try a different ID!"
}
```


This project is open source. Feel free to fork this repo and contribute. Happy coding y'all!