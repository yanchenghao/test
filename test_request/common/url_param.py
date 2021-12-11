from urllib.parse import urlparse,parse_qs,urlencode
def params_encode(url):
    query=urlparse(url).query
    params=parse_qs(query)
    if params=="":
        return url
    else:
        params_result={k:v[0] for k,v in params.items()}
        url1 = url.split("?")[0]
        return url1,params_result
    # a=urlencode(params_result)
    # for key in params:
    #     a[]=params[key][0]
    # print(query)
    # print("a")