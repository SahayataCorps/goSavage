import requests

class Final:

	
    def modelE(self, u):
        url = 'https://www.virustotal.com/vtapi/v2/url/report'
        params = {'apikey': '03bb6241c79ef6d1ad942e40681ff63a76d693c1cd7fa7ceba67fff078bb0bd5',
                  'resource': u}
        response = requests.get(url, params=params)
        return response.json()['positives']
