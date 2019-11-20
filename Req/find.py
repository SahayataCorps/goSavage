#from LexalFeature import LexicalFeatures
import sys
import requests
from Final import Final
class Finale:
    finalle = []

    url = ''


    def getFeatures(self,u):
        self.url = u

        lf = LexicalFeatures(self.url)
        lf.fillDetails()
        lfl = lf.returnFeature()

        sumup = lfl
        self.finalle.append(sumup)

    def senData(self):
        durl = ''
        dapi = ''
        data = {

            "Inputs": {

                "input1":
                    {
                        "ColumnNames": [],
                        "Values": [self.finalle, ]
                    }, }
            ,
            "GlobalParameters": {
            }
        }

        body = str.encode(json.dumps(data))
        headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + dapi)}
        req = urllib.request.Request(durl, body, headers)

        try:
            response = urllib.request.urlopen(req)

            result = json.loads(response.read().decode('utf-8'))

        except urllib.request.HTTPError as error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())

            print(json.loads(error.read()))




a = Finale()
urll = sys.argv[1]
#a.getFeatures(urll)
b = Final()
print(b.modelE(urll))