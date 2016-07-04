# -*- coding: utf8 -*-
from compose.integration.channel import Channel
class Service(object):
    def __init__(self, channels, parameters):
        self.name = parameters['name']
        self.version = parameters['version']
        self.configuration = parameters['configuration']
        channel = Channel(parameters['input-channel'])
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
        return '[name:' + str(self.name) +', version:' + str(self.version) + ', configuration:' + str(self.configuration) + ', channel:' + str(self.channel) + ']'