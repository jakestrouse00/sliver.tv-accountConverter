import requests


def conventAccount(email, password):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
        'X-App-Version': '4',
        'X-Platform': 'web',
        'Content-Type': 'application/json; charset=UTF-8'
    }

    payload = {
        "email_or_username": email,
        "password": password
    }

    r = requests.post('https://api.sliver.tv/v1/user/auth', json=payload, headers=head)

    body = r.json()['body']
    token = body['access_token']
    user = body['id']
    with open('auths.txt', 'a+') as f:
        f.write(f'{token}:{user}\n')


def getAccounts():
    with open('accounts.txt', 'r') as f:
        accounts = f.read().splitlines()
    return accounts


accounts = getAccounts()
for accountm in accounts:
    account = accountm.split(":")
    email = account[0]
    password = account[1]
    conventAccount(email, password)
