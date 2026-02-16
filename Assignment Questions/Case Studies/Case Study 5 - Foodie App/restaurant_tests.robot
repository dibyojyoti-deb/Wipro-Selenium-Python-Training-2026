*** Settings ***
Library    RequestsLibrary
Library    Collections

Suite Setup    Create Session    foodie    http://127.0.0.1:5000/api/v1
Suite Teardown    Delete All Sessions

*** Variables ***
${restaurant_id}    0
${user_id}          0
${order_id}         0
${dish_id}          0

*** Test Cases ***

Register Restaurant
    ${body}=    Create Dictionary    name=Food Hub    category=Veg    location=Delhi    contact=9999999999
    ${res}=    POST On Session    foodie    /restaurants    json=${body}
    Status Should Be    201    ${res}
    ${json}=    Evaluate    __import__('json').loads('''${res.text}''')
    Set Suite Variable    ${restaurant_id}    ${json['id']}

Duplicate Restaurant
    ${body}=    Create Dictionary    name=Food Hub    category=Veg    location=Delhi    contact=9999999999
    ${res}=    POST On Session    foodie    /restaurants    json=${body}    expected_status=409
    Status Should Be    409    ${res}

View Restaurant
    ${res}=    GET On Session    foodie    /restaurants/${restaurant_id}
    Status Should Be    200    ${res}

Update Restaurant
    ${body}=    Create Dictionary    location=Mumbai
    ${res}=    PUT On Session    foodie    /restaurants/${restaurant_id}    json=${body}
    Status Should Be    200    ${res}

Disable Restaurant
    ${res}=    PUT On Session    foodie    /restaurants/${restaurant_id}/disable
    Status Should Be    200    ${res}

Add Dish
    ${body}=    Create Dictionary    name=Pizza    type=Veg    price=250
    ${res}=    POST On Session    foodie    /restaurants/${restaurant_id}/dishes    json=${body}
    Status Should Be    201    ${res}
    ${json}=    Evaluate    __import__('json').loads('''${res.text}''')
    Set Suite Variable    ${dish_id}    ${json['id']}

Update Dish
    ${body}=    Create Dictionary    price=300
    ${res}=    PUT On Session    foodie    /dishes/${dish_id}    json=${body}
    Status Should Be    200    ${res}

Toggle Dish Status
    ${body}=    Create Dictionary    enabled=False
    ${res}=    PUT On Session    foodie    /dishes/${dish_id}/status    json=${body}
    Status Should Be    200    ${res}

Delete Dish
    ${res}=    DELETE On Session    foodie    /dishes/${dish_id}
    Status Should Be    200    ${res}

Register User
    ${body}=    Create Dictionary    name=Harsh    email=harsh@test.com
    ${res}=    POST On Session    foodie    /users/register    json=${body}
    Status Should Be    201    ${res}
    ${json}=    Evaluate    __import__('json').loads('''${res.text}''')
    Set Suite Variable    ${user_id}    ${json['id']}

Duplicate User
    ${body}=    Create Dictionary    name=Harsh    email=harsh@test.com
    ${res}=    POST On Session    foodie    /users/register    json=${body}    expected_status=409
    Status Should Be    409    ${res}

Place Order
    ${body}=    Create Dictionary    user_id=${user_id}    restaurant_id=${restaurant_id}    dishes=[]
    ${res}=    POST On Session    foodie    /orders    json=${body}
    Status Should Be    201    ${res}
    ${json}=    Evaluate    __import__('json').loads('''${res.text}''')
    Set Suite Variable    ${order_id}    ${json['id']}

View Orders By User
    ${res}=    GET On Session    foodie    /users/${user_id}/orders
    Status Should Be    200    ${res}

View Orders By Restaurant
    ${res}=    GET On Session    foodie    /restaurants/${restaurant_id}/orders
    Status Should Be    200    ${res}

Give Rating
    ${body}=    Create Dictionary    order_id=${order_id}    rating=5    comment=Excellent
    ${res}=    POST On Session    foodie    /ratings    json=${body}
    Status Should Be    201    ${res}

Admin Approve Restaurant
    ${res}=    PUT On Session    foodie    /admin/restaurants/${restaurant_id}/approve
    Status Should Be    200    ${res}

Admin Disable Restaurant
    ${res}=    PUT On Session    foodie    /admin/restaurants/${restaurant_id}/disable
    Status Should Be    200    ${res}

Admin View Orders
    ${res}=    GET On Session    foodie    /admin/orders
    Status Should Be    200    ${res}
