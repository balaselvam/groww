import connection
import fetch 
import asyncio

app = connection.app 

# Start the background task to update the live data
@app.on_event("startup")
async def startup_event():
    url = "https://groww.in/v1/api/option_chain_service/v1/option_chain/maruti-suzuki-india-ltd?expiry=2023-11-30"  # Replace this URL with the data source URL
    url_next = "https://groww.in/v1/api/option_chain_service/v1/option_chain/maruti-suzuki-india-ltd?expiry=2023-11-30"
    url_far = "https://groww.in/v1/api/option_chain_service/v1/option_chain/maruti-suzuki-india-ltd?expiry=2023-11-30"
    filename = "dw_data.json"  # Choose the desired filename for the saved data
    filename_next = "dw_data_next.json"
    filename_far = "dw_data_far.json"
    asyncio.create_task(fetch.fetch_and_save_data(url, filename))
    asyncio.create_task(fetch.fetch_and_save_data_next(url_next, filename_next))
    asyncio.create_task(fetch.fetch_and_save_data_far(url_far, filename_far))

