from compose.integration import Builder
from compose.integration.channel import Channel

class HttpBuilder(Builder):

    def build(self, channels, parameters):
        http = HttpGateway(parameters)
        http.set_channel(channels, parameters)
        return http
##
#    channel: &hello_world
#      id: hello_world
#    configuration:
#      port: 8080
#      path: /hello_world
class HttpGateway:
    def __init__(self, parameters):
        configuration = parameters['configuration']
        self.port = configuration['port']
        self.path = configuration['path']

    def set_channel(self, channels, parameters):
        # channel: &hello_world
        #    id: hello_world
        channel = Channel(parameters['channel'])
        add_to_channels = True
        for a_channel in channels:
            if channel == channels[a_channel]:
                # channel already exists
                channel = channels[a_channel]
                add_to_channels = False
                break
        self.channel = channel
        if add_to_channels:
            channels[channel.id] = self.channel
    
    def __str__(self):
        return '[port:' + str(self.port) +', path:' + self.path + ', channel:' + str(self.channel) + ']'