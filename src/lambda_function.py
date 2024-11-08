import json

cabinet_orders = {
    1: {"id": 1, "customer": "Jamesz", "cabinets": ["A"]},
    2: {"id": 2, "customer": "Bentley", "cabinets": ["A", "B"]}
}

def lambda_handler(event, context):
    order_id = event.get('order_id')

    if not order_id:
        payload = cabinet_orders
    else:
        order_id = int(order_id)
        payload = None

        for order in cabinet_orders.values():
            if order['id'] == order_id:
                payload = order
                break

        if payload == None:
            return {
                'statusCode': 400,
                'errorMessage': 'Unable to find order'
            }
    
    return {
        'statusCode': 200,
        'body': json.dumps(payload)
    }
