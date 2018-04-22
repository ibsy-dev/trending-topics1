#!/usr/bin/python 

pip install python twitter

import twitter

api = twitter.Api(consumer_key="HdNFQ0YH52wyrwtUYiwalIp3b",
consumer_secret="dC6Uc13Xhrtsel92uBlD3r6QyEkWq8oCFR6psW8rCsURR4YQaY",
access_token_key="46344285-UOV7LAxBlelMHA59eYH1wteT4FssMjoBQJJIq1UPU",
access_token_secret="FXSMZSOZameYmsfbP2Gac2COGPPF8ZDJWoWyQniLxVQxz")

print(api.VerifyCredentials())

