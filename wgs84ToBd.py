# -*- coding: utf-8 -*-
import urllib
import hashlib
import requests
import json

class Geoconv(object):
    my_ak = '6QIcXpIzMMUbXIgxgziDzzDa7NGh5daV'
    my_sk = 'fFyAglwnmgxnYI6c---------------------------'

    def __init__(self):
        pass

    # GPS����ת��Ϊ�ٶ�����
    #���ͣ�http://lbsyun.baidu.com/index.php?title=webapi/guide/changeposition
    #API��http://api.map.baidu.com/geoconv/v1/?coords=114.21892734521,29.575429778924&from=1&to=5&ak=�����Կ //GET
    def wgs84tobd09(self,lon,lat):
        queryStr = '/geoconv/v1/?coords={},{}&from=1&to=5&ak={}'.format(lon,lat,self.my_ak)
        # print queryStr
        # ��queryStr����ת�룬safe�ڵı����ַ���ת��
        encodedStr = urllib.parse.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")

        # �����ֱ��׷����yoursk
        rawStr = encodedStr + self.my_sk

        # md5�������snֵ
        my_sn = '6QIcXpIzMMUbXIgxgziDzzDa7NGh5daV'  ###hashlib.md5(urllib.parse.quote_plus(rawStr)).hexdigest()
        # print my_sn
        url = 'http://api.map.baidu.com' + queryStr + "&sn=" + my_sn
        # print url

        res = requests.get(url)
        # print '*' * 10
        # get�յ�������
        json_str = res.content
        # print json_str
        dictData = json.loads(json_str)
        # print dictData["result"][0]["x"]
        # print dictData["result"][0]["y"]
        return dictData["result"][0]["x"],dictData["result"][0]["y"]


if __name__ == '__main__':
    LON = '116.668443'	
##'112.40832'
    LAT = '39.643480'
	#'34.636055'
    myconv = Geoconv()
    print (myconv.wgs84tobd09(LON,LAT))