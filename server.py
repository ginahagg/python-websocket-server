from websocket_server import WebsocketServer
import json
import time
import array;

# Called for every client connecting (after handshake)
def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])
	#server.send_message_to_all("Hey all, a new client has joined us")
	dt = get_data()
	#maxItem = {u'y': 371, u'x': 634}
	for item in dt:
	#	if item == maxItem:
	#		for x in range(4000):
	#			server.send_message_to_all( json.dumps(maxItem) );
	#			time.sleep(0.003)
	#	else:
		server.send_message_to_all( json.dumps(item) )
		time.sleep( 0.07 )


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
	if len(message) > 200:
		message = message[:200]+'..'
	print("Client(%d) said: %s" % (client['id'], message))

def get_data():
	with open('points.json') as f:
  		return json.load(f)




PORT=9001
server = WebsocketServer(PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()

