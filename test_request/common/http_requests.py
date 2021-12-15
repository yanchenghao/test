import requests
class HttpRequest:

    def request(self,url,headers=None,params=None,data=None,json=None,http_method=None,timeout=5,verify=True,cookie=None):

        if http_method.upper()=='GET':
                red = requests.get(url,headers=headers,params=params,timeout=timeout,verify=verify,cookies=cookie)
        elif http_method.upper()=='POST':
                red = requests.post(url,headers=headers,data=data,json=json,timeout=timeout,verify=verify,cookies=cookie)
        code=red.status_code
        try:
            body=red.json()
        except Exception as e:
            body=red.text
        res=dict()
        res["code"]=code
        res["body"]=body
        return res