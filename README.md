# Task-Scheduler
Simple Django API to schedule a task

## Requirements
Requires nothing more than Django and requests, they can be installed by running the command below. You may want to create a virtual environment first. Additional dependencies get downloaded automatically
```
pip install Django==3.0.7 requests==2.24.0
```

## API
### Endpoints
It consists of only two end points 
#### 1. /ping

Ping the server to check if it is running, returns status 200 if it is running.

Methods Allowed: ['GET']

Response recieved
```
{
   "status" : "OK"
}
```

#### 2. /api
Methods Allowed: ['GET']

Parameters: ['datetime', 'url']

The datetime format must be in the format dd-mm-yyyyTHH:mm:ss. Here 'T' joins date and time. Time must be in 24 hour format and each entity must be zero padded, eg. 28-06-30T06:00.
If the datetime provided is behind current datetime, server responds with error. The url should also be correct.

Sample Request:

```
http://localhost:8000/api?datetime=28-06-2020T04:24:50&url=http://localhost:8000/ping
```

Response status: 200 OK
```
{
    "status": "success"
}
```

Error Responses:

Response status: 400 Bad Request
```
{
    "datetime": "invalid date",
    "url": "invalid url"
}
```
Response status: 500 Internal Server Error

No Body



