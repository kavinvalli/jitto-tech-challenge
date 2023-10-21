# Jitto Tech Challenge

## Main URL

This is the main url: https://23goerl6qg.execute-api.us-east-2.amazonaws.com/jitto-tech-challenge

### Get All Items

`GET https://23goerl6qg.execute-api.us-east-2.amazonaws.com/jitto-tech-challenge/items`

### Get Single Item (based on id)

`GET https://23goerl6qg.execute-api.us-east-2.amazonaws.com/jitto-tech-challenge/items/{id}`

### Create Item

`POST https://23goerl6qg.execute-api.us-east-2.amazonaws.com/jitto-tech-challenge/items`

Request Body:

```json
{
  "name": "Item 1",
  "description": "Lorem ipsum dolor sit amet constectuer init"
}
```

Request Headers:

```
x-api-key: J7os3Fs2Yf13N4o3tC7As5rwhvcxOTxGrBqmkYi6
```

## Usage

- AWS Lambda Function
- API Gateway

## Features

- Endpoints
  - Retrieve all items
  - Retrieve details of single item
  - Add a new item
- API Key based authentication via API Gateway
- Logging using CloudWatch
- Rate Limiting using API Gateway and Usage Plan (100 rate per second, 200 burst)
