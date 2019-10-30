import json

import psycopg2 #biblioteca de banco de dados

from utils.db_credentials import DBCredentials

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

def claim_gift(event,context):
    log.info(json.dumps(event))
    item_id =  event['pathParameters']['id']
    # body = event['body']

    log.info(f"item_id: {item_id}")

    credentials = DBCredentials()

    conn = psycopg2.connect(**credentials.credentials)
    cur = conn.cursor()

    cur.execute("update items set reserved = true where id = %s",(item_id,))

    cur.close()
    conn.commit()
    conn.close()

    response = {
        "statusClose": 200
    }

    return response