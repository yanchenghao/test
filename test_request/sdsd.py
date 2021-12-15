import requests



header={
"country": "CN",
"language": "en",
"appVersionName": "1.0.1",
"appVersionCode": "7",
"packageName": "com.mole.talktalk",
"packageChannel": "google",
"curPackageChannel": "google",
"appPlatform": "1",
"Authorization": "7NPZMsDsnIIMBI7shC0AYeeBzPjPvB8PbKdEE+j+H0iubPJxtGs5dDP4Ze178yW5",
# "Authorization": "h8pIYs+niv4dLK3By6vIFXgpXsEH6uIr1Y9lbhRAveWubPJxtGs5dDP4Ze178yW5",
"deviceId": "8c154773-5b9a-4b25-bfd9-bf488b7643b9",
# "deviceId": "1e985fc9-08d7-494f-89f8-1824f581946b",
"brand": "TECNO",
"model": "TECNO CG8",
"sdkInt": "30",
# "netQuality": "netType: WIFI",
"Content-Type": "application/json",
"Host": "apitest.molelive.com",
"Accept-Encoding": "gzip",
"User-Agent": "okhttp/3.14.9",
"Connection": "keep-alive"}
url="http://api.molelive.com/api/content/index/all"
# url="http://apitest.molelive.com/api/content/index/all"
param={"type":"popular"}
r1=requests.get(url,params=param,headers=header)
print(r1.text)