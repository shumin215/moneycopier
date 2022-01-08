import os
import jwt
import uuid
import hashlib
import argparse
from urllib.parse import urlencode

import requests

def read_key (_file_path):
    print("Read file: ", _file_path)
    with open(_file_path, "r", encoding="utf-8") as f:
        ret = f.readline().rstrip()
        return ret

def main():
    parser = argparse.ArgumentParser(description="This is to test accessing exchange, UPBIT")
    parser.add_argument("-ak", "--ak", required=True, help="This is access key file path")
    parser.add_argument("-sk", "--sk", required=True, help="This is secret key file path")
    args = parser.parse_args()

    ak_file = args.ak
    sk_file = args.sk

    access_key = read_key(ak_file)
    secret_key = read_key(sk_file)

    server_url = "https://api.upbit.com/v1/accounts"

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.get(server_url, headers=headers)

    print(res.json())

if __name__ == "__main__":
    main()
