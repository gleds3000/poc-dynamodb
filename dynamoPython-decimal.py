import boto3
import random
from decimal import *


def load_transactions(dynamodb):

    table = dynamodb.Table('expenses')

    trans = {}

    trans['transNo'] = random.randint(100000, 99999999999)
    trans['amount'] = Decimal(str(random.random()*random.randint(10,1000)))
    trans['transDate'] = '2020-03-19'

    print(trans)

    table.put_item(Item=trans)


if __name__ == '__main__':


    dynamodb = boto3.resource('dynamodb',  endpoint_url = "http://localhost:8001")

    load_transactions(dynamodb)
