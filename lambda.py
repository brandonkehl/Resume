import json

def lambda_handler(event, context):

    visitId = event['queryStringParameter']['visitID']
    visitCount = event['queryStringParameter']['count']

    print('visitors='+ visitCount)

    # body of response
    visitResponse ={}
   # visitResponse['visitId'] = visitId
    visitResponse['count'] = visitCount 

    # http response
    responseObject ={}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(visitResponse)

    return responseObject