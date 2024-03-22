import connection 

app = connection.app

#Check json data in url parameter
@app.get("/data")
async def get_data():
    return app.state.data_list

#Read CE option Open Interest data
@app.get("/data/ceoi")
async def get_data():
    ce_OI = []
    for option_chain  in app.state.data_list["optionChains"]:
        open_interest = option_chain["callOption"]["openInterest"]
        ce_OI.append({"strikePrice": option_chain["strikePrice"], "openInterest": open_interest})
    return ce_OI

#Read CE option Open Interest data
@app.get("/data/peoi")
async def get_data():
    pe_OI = []
    for option_chain  in app.state.data_list["optionChains"]:
        open_interest = option_chain["putOption"]["openInterest"]
        pe_OI.append({"strikePrice": option_chain["strikePrice"], "openInterest": open_interest})
    return pe_OI

#Read All primary keys in json file
@app.get("/data/keys")
async def get_item():
    key_item = []
    for i in app.state.data_list.keys():
        key_item.append(i)
    return key_item
    #return {"message": "Item not found"}

@app.get("/data/val")
async def get_item():
    val_item = []
    for i in app.state.data_list.values():
        val_item.append(i)
    return val_item
    #return {"message": "Item not found"}