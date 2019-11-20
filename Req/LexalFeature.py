# -*- coding: utf-8 -*-
from urllib.parse import urlparse
import re
from tld import get_fld, get_tld
import socket


class LexicalFeatures:
    accused = ''
    length = {
        "hostnameLength":0,
        "topLevelDomainLength":0,
        "primaryDomainLength":0,
        "pathLength":0
    }
    details = {
        "protocol":"http",
        "hostname":"",
        "topLevelDomain":"",
        "primaryDomain":"",
        "path":"",
        "query":"",
        "noOfQuery":0,
        "ipaddress":""
    }
    containsIp = 0
    token = {
        "domainToken":[],
        "pathToken":[]
    }

    no_of_dots = 0
    length_of_url = 0
    token_count = 0
    avg_token_length = 0

    avg_path_token = 0
    path_token_count = 0

    domain_token_count = 0
    largest_domain = 0
    avg_domain_token = 0

    malicious = 0

    def __init__(self, urlp):
        assert isinstance(urlp, str)
        self.accused = urlp
        self.no_of_dots = self.accused.count('.')
        self.length_of_url = len(self.accused)
        


    def fillDetails(self):
        sep = urlparse(self.accused)
        #protocol
        if sep.scheme != '':
            self.details["protocol"] = sep.scheme

        #hostname
        if bool(re.search(r'\d.\d.', self.without(sep.netloc))):
            self.containsIp = 1
            self.details["ipaddress"] = sep.netloc
        else:
            self.details['hostname'] = sep.netloc
            self.length['hostnameLength'] = len(sep.netloc)
            self.details['topLevelDomain'] = get_tld(self.without(sep.netloc), fix_protocol=True)
            self.length['topLevelDomainLength'] = len(self.details['topLevelDomain'])
            self.details['primaryDomain'] = get_fld(self.without(sep.netloc), fix_protocol=True)
            self.length['primaryDomainLength'] = len(self.details['primaryDomain'])
            try:
                self.details["ipaddress"] = socket.gethostbyname(sep.netloc)
            except:
                pass
        #path & querry
        self.details['path'] = sep.path
        self.details['query'] = sep.query
        self.details['noOfQuery'] = len(sep.query.split('&'))
        if sep.query=='':
            self.details['noOfQuery']-=1
        self.length['pathLength'] = len(self.details['path']) + len(self.details['query'])
        self.tokens()


    def without(self, obj):
        ret = ''
        for x in obj:
            if ord(x)>-128 or ord(x)<128:
                ret+=x
        return ret

    def tokens(self):
        if self.containsIp == 0:
            host_token = self.details['hostname'].split('.')
            self.token["domainToken"] = host_token
            self.domain_token_count = len(host_token)
            self.largest_domain = len(max(host_token, key=len))
            if len(host_token):
                self.avg_domain_token = sum([len(x) for x in host_token])/len(host_token)
            else:
                self.avg_domain_token = 0
            self.token_count += len(host_token)
            self.avg_token_length += self.avg_domain_token

        path_token = re.findall(r'/\w+', self.details['path'])

        if self.details['noOfQuery']:
            query_token = self.details['query'].split('&')
            for x in query_token:
                q = x.split('=')
                for i in q:
                    path_token.append(i)
        self.token['pathToken'] = path_token
        self.path_token_count = len(path_token)
        if len(path_token):
            self.avg_path_token = sum([len(x) for x in path_token])/len(path_token)
        else:
            self.avg_path_token = 0
        self.token_count += len(path_token)
        self.avg_token_length += self.avg_path_token


    def returnFeature(self):
        features = [
                    
                    self.details['noOfQuery'],
                    
                    self.length['hostnameLength'],
                    self.length['topLevelDomainLength'],
                    self.length['primaryDomainLength'],
                    self.length['pathLength'],
                    self.containsIp,
                    self.no_of_dots,
                    self.length_of_url,
                    self.token_count,
                    self.avg_token_length,
                    self.path_token_count,
                    self.avg_path_token,
                    self.domain_token_count,
                    self.largest_domain,
                    self.avg_domain_token
                    ]
        return features

