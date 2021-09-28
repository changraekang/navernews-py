import requests

def getNewsApi():

    url ="http://localhost:8080/news"

    response = requests.get(url)
    responseDict = response.json()


    news_code = responseDict['code']
    newsDto = responseDict
    if news_code == 1:
        return (newsDto['data'])
    else:
        print(newsDto['msg'])
