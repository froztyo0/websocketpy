import asyncio
import websockets

# def get_data(file_path):
#     with open(file_path,"r") as f:
#         pixel_matrix=json.load(f)["indflag"]
#         temp=[]
#         for i in list(pixel_matrix.keys()):
#             x,y=i.split(",")
#             temp.append({"x":x,"y":y,"color":pixel_matrix[i]["color"]})
#         pixel_matrix=temp
#         pixel_matrix.append("Invalid")
#         response=json.dumps({"type":"Jobs","jobs":{"Wololo":pixel_matrix}})
#         return response


async def echo(websocket, path):
    # This function will be called whenever a new connection is made
    try:
        while True:
            # Receive a message from the client
            message = await websocket.recv()
            print(f"Received message: {message}")

            # Echo the message back to the client
            # type: "RequestJobs", tokens: tokens
                # "787,208": { "color": "#ffa800", "prio": 250 },
            # message= get_data()
            message={"type": "Jobs","jobs": { "Wololo": [{ "x": -474, "y": -481, "color": "6" }, "Invalid"] }}
            await websocket.send(message)
    except websockets.ConnectionClosedOK:
        print("Connection closed by client.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Start the WebSocket server
start_server = websockets.serve(echo, "", port=int(os.environ["PORT"]))

# Enter the event loop to run the server indefinitely
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
