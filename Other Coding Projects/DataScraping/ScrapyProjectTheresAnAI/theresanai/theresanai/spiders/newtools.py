import requests

response = requests.get(
  url='https://proxy.scrapeops.io/v1/',
  params={
      'api_key': 'bb5832e7-f25f-4796-bd8f-429d2b0f0e02',
      'url': 'http://theresanaiforthat.com', 
  },
)

print('Response Body: ', response.content)
      

      