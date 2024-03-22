from fastapi import FastAPI,HTTPException,Request,WebSocket
import asyncio
import json 
import requests
import connection
from fastapi.responses import StreamingResponse
from typing import Iterator

app = connection.app
#function to download live current expiry data from web
async def fetch_and_save_data(url, filename):
    while True:
        app.state.data_list = {}
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404 Not Found)
            with open(filename, "wb") as f:
                f.write(response.content)
                print(f"Data downloaded and saved as '{filename}'")
            # Read data from the JSON file and convert to a list
            try:
                with open(filename, "r") as file:
                    data = file.read()
                    if data.strip():
                        app.state.data_list = json.loads(data)
                    else:
                        #app.state.data_list = {}  # Empty data
                        continue
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON data: {str(e)}")
                app.state.data_list = {}  # Empty data if decoding fails
            
        except requests.RequestException as e:
            print(f"Error during data fetch: {str(e)}")
        await asyncio.sleep(2)

#function to download live next expiry data from web
async def fetch_and_save_data_next(url, filename):
    while True:
        app.state.data_list_next = {}
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404 Not Found)
            with open(filename, "wb") as f:
                f.write(response.content)
                print(f"Data downloaded and saved as '{filename}'")
            # Read data from the JSON file and convert to a list
            try:
                with open(filename, "r") as file:
                    data = file.read()
                    if data.strip():
                        app.state.data_list_next = json.loads(data)
                    else:
                        #app.state.data_list = {}  # Empty data
                        continue
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON data: {str(e)}")
                app.state.data_list_next = {}  # Empty data if decoding fails
            
        except requests.RequestException as e:
            print(f"Error during data fetch: {str(e)}")
        await asyncio.sleep(2)

#function to download live far month expiry data from web
async def fetch_and_save_data_far(url, filename):
    while True:
        app.state.data_list_far = {}
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404 Not Found)
            with open(filename, "wb") as f:
                f.write(response.content)
                print(f"Data downloaded and saved as '{filename}'")
            # Read data from the JSON file and convert to a list
            try:
                with open(filename, "r") as file:
                    data = file.read()
                    if data.strip():
                        app.state.data_list_far = json.loads(data)
                    else:
                        #app.state.data_list = {}  # Empty data
                        continue
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON data: {str(e)}")
                app.state.data_list_far = {}  # Empty data if decoding fails
            
        except requests.RequestException as e:
            print(f"Error during data fetch: {str(e)}")
        await asyncio.sleep(2)

# Global variables to store the chart data
app.state.oi_pcr_avg = {}
app.state.x_data = []
app.state.y_data = []

async def generate_chart_data() -> Iterator[str]:

    # Load data from the JSON file
    with open("oi_pcr_avg_data.json", "r") as file:
        data = json.load(file)

    # Store the data in the app state
    app.state.oi_pcr_avg = data
    # Iterate through the data and yield each item with a delay of 2 seconds
    for item in app.state.oi_pcr_avg:
        json_data = json.dumps(item)
        #print(json_data)
        yield f"data:{json_data}\n\n"

@app.get("/chart-data")
async def chart_data(request: Request) -> StreamingResponse:
    app.state.oi_pcr_avg = {}
    response = StreamingResponse(generate_chart_data(), media_type="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response