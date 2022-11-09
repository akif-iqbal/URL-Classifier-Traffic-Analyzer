from logistic import LogisReg

ob=LogisReg()
data=ob.process()
web=["google.com/search=jcharistech"]
pred=ob.testing(web)
print(pred)

