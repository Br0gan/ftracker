#!/usr/bin/python

import requests

with requests.Session() as c:
    url = 'http://www.cbssports.com/login'
    USERID = 'xxxxx'
    PASSWORD = 'xxxxx'
    c.get('http://www.cbssports.com/fantasy')
    login_data = dict(login_form='login_form', xurl='http://www.cbssports.com/fantasy',
                        master_product="150",  vendor="cbssports",
                        userid=USERID, password=PASSWORD, _submit="Sign In")

    c.post(url, data = login_data)
    page = c.get('http://teambuddy.football.cbssports.com/print/csv/teams/roster-grid', stream=True)
    if page.status_code == 200:
        print('sucess')
        with open('grid.csv', 'wb') as f:
            for chunk in page.iter_content(1024):
                f.write(chunk)


