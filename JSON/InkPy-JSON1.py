import json

inkjsonpath = open('./ShopTest.json', "r")
inkjson = json.loads((inkjsonpath).read())

# ALL OF THE CODE IS COMMENTED DUE TO ME BEING UNABLE TO PARSE NESTED JSON FILES


# inkroot = dict(inkjson["root"])
# inkroot = dict.fromkeys(inkjson["root"])


# def get_simple_keys(data):
#     result = []
#     for x in data:
#             inkroot[inkjson['root']] = {}
#             keys = x.keys()
#             result = keys
#             values = x.values()
#             # for k in x.keys():
#             #     if k =='root': continue
#             #     inkroot[x['root']][k]=x[k]
#     return result

# print(get_simple_keys(inkjson))

# value = inkjson['root']
# print(value)

# print(inkjson["root"]["start"])