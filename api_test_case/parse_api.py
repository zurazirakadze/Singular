import json
import requests


def validate_user_info(known_info, Key):
    url = "https://coreapi-gli.singulardev.uk/WebsiteService"
    payload = 'userIdentifier=qa_3&password=Testing&otpDeliveryChannel=0&req=login'
    headers = {
        'Cookie': 'userPasswordUpdated=2020-10-15%2012%3A43%3A23; '
                  'userCountry=%7B%22id%22%3A7%2C%22is_blocked%22%3Afalse%2C%22title%22%3A%22Georgia%22%2C%22dial_in'
                  '%22%3A%22995%22%2C%22iso%22%3A%22GEO%22%2C%22iso2%22%3A%22GE%22%7D; '
                  'user=%7B%22id%22%3A4837143%2C%22isLoggedIn%22%3Afalse%7D; '
                  'userLastSession=2020-10-15%2016%3A45%3A24; '
                  'JSESSIONID'
                  '=eyJ0cyI6MzQ1NjU1OTkwNzIxLCJkdCI6ImV5SjFhV1FpT2pRNE16Y3hORE1zSW5OemFXUWlPaUk1WW1ObVl6ZG1aQzB3TVRFMExUUXlNbVV0T0RKaE1DMHhaR1V6TWpSaVptUXpZeklpZlE9PSIsInNnIjoiOTQxOTc4MGJkNDBhOTI1MzUyZjI3OWQ2MzA5NTU0ODdiOTEyYzQxMDdmNTIwM2YwNmMwMDJkZmVjYTU2OWExYiJ9; BIAB_CUSTOMER=NDgzNzE0My01OTZjNjU0M2MzYjkyY2NiOGM0YzhlZWI4OGYyNjcyZmEwY2JlZDc5YzIwZGMyN2NiMjQxZjllNmI5NDM2OTBh',
        'Origin': 'https://www-gli.singulardev.uk',
        'Referer': 'https://www-gli.singulardev.uk',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.text.encode('utf8')
    print(data)
    parse_data = json.loads(data)
    assert known_info in parse_data[Key]


