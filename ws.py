import re
from mitmproxy import ctx
def websocket_message(flow):
    # get the latest message
    message = flow.messages[-1]
    if message.from_client:
         ctx.log.info("Client: {}".format(message.content))
    else:
        ctx.log.info("Server: {}".format(message.content))
    pass

