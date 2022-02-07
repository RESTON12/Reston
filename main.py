import requests
from keep_alive import keep_alive
payload ={
    "content": "Reston"
}

header = {
    "authorization": "ODUzMzY4Njk1MjE2Nzk5NzY0.Yf_jWA.N6bwmUD45s3sKCwgyb9w9UFxrec"
   
}


while True:
    web_info = requests.post('https://discord.com/api/v9/channels/940262299762040876/messages', data=payload, headers=header)

