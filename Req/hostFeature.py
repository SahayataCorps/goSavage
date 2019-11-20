import whois
import datetime

def days_between(d1, d2):
    d1 = str(d1)
    d2 = str(d2)
    d1 = d1.split(" ")
    d2 = d2.split(" ")
    d1 = d1[0]
    d2 = d2[0]

    year1, month1, day1 = map(int,d1.split("-"))
    year2, month2, day2 = map(int,d2.split("-"))
    d1 = datetime.date(year1,month1,day1)
    d2 = datetime.date(year2, month2, day2)
    return abs(d1-d2).days

def tokens(lib):
    token = []
    for x in lib:
        y = x.split(".")
        for i in y:
            token.append(i)
    return token


class HostFeature:
    url = ''
    ifip = 1
    whoisServer = ''
    nameServer = ''
    country = ''
    name = ''
    creationDate = ''
    registrar = ''
    expiration = ''
    age=''

    def __init__(self, source, isIP):
        self.url = source
        self.ifip = isIP

    def getDetails(self):
        try:

            details = whois.whois(self.url)

            self.registrar = details['registrar']
            self.whoisServer = details['whois_server']
            self.nameServer = details['name_servers']
            self.nameServer = tokens(self.nameServer)
            self.country = details['country']
            self.name = details['name']

            self.creationDate = details['creation_date']
            self.creationDate = self.creationDate[0]

            self.expiration = details['expiration_date']
            self.expiration = self.expiration[0]

            self.age = days_between(self.creationDate, datetime.datetime.now())


        except:
            pass

    def returnDatas(self):
        hostFeatures = [
            self.registrar,
            self.whoisServer,
            self.country,
        self.name,
        
        ]
        return hostFeatures


a = HostFeature("http://themoodmusic.com",0)
a.getDetails()
print(a.returnDatas())
