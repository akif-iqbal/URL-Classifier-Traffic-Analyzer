from logistic import LogisReg
import re

ob=LogisReg()
web=["amazon.in"]

for i in range(len(web)):
    if "https://www." or "https://"  in web[i]:
        url = re.compile(r"https?://(www\.)?")
        web[i] = url.sub('', web[i]).strip().strip('/')
print(web)
pred=ob.testing(web)
print(pred)
