def GetUrl(url):
    urls = url.split('/')
    url = urls[0] + '/' + urls[1] + '/' + urls[2] + '/'
    return url
# testurl = GetUrl('http://mqc.test.haigeek.com/login')
# print(testurl)