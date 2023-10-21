import json
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('items')


def get_all_items():
    response = table.scan()
    print("RESPONSE", response)
    data = response['Items']
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    return {
        'statusCode': 200,
        'body': json.dumps(data),
    }


def get_item(item_id):
    response = table.get_item(Key={'id': item_id})
    if 'Item' not in response:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': f'Item with id {item_id} not found'})
        }
    return {
        'statusCode': 200,
        'body': json.dumps(response['Item']),
    }


def create_item(body):
    if "name" not in body:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Name is required'})
        }
    elif "description" not in body:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Description is required'})
        }
    table.put_item(Item={
        'id': str(uuid.uuid4()),
        'name': body['name'],
        'description': body['description']
    })
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': "Item created successfully",
        })
    }


def lambda_handler(event, context):
    method = event["httpMethod"]
    resource = event["resource"]
    match f'{method} {resource}':
        case "GET /items":
            return get_all_items()
        case "GET /items/{id}":
            item_id = event["pathParameters"]["id"]
            return get_item(item_id)
        case "POST /items":
            body = json.loads(event["body"])
            return create_item(body)
