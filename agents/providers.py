import time

def provider_a(context):
    print("provider A started")
    time.sleep(2)
    print("provider A finished")
    return {"status":"success", "provider":provider_a.__name__, "price": 450, "reason":None}

def provider_b(conext):
    print("provider B started")
    time.sleep(1)
    print("provider B finished")
    return {"status":"success", "provider":provider_b.__name__, "price": 600, "reason":None}

def provider_c(conext):
    print("provider C started")
    time.sleep(6)
    print("provider C finished")
    return {"status":"success", "provider":provider_c.__name__, "price": 550, "reason":None}

