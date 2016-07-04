import argparse
import yaml
from compose.integration.gateway import GatewayBuilders
from compose.integration.service import Service
from compose.integration.channel import Channel

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("start", help="Start services")
    # parser.add_argument("stop", help="Stop services")
    args = parser.parse_args()
    
    # print args.echo
    
    with open("Maestrofile.yml", 'r') as stream:
        try:
            doc = yaml.load(stream)
            channels = {}
            services = {}
            gateways = {}
            if 'channels' in doc:
                channels_def = doc['channels']
                for name in channels_def:
                    # iterating all gateways
                    channel = Channel(name)
                    channels[name] = channel
                print ""
            if 'gateways' in doc:
                gateways_def = doc['gateways']
                for name in gateways_def:
                    # iterating all gateways
                    builder = GatewayBuilders.builder(name)
                    gateway = builder.build(channels, gateways_def[name])
                    gateways[name] = gateway
            if 'services' in doc:
                services_def = doc["services"]
                for name in services_def:
                    # iterating all gateways
                    service = Service(channels, services_def[name])
                    services[name] = service
            print 'Definition:'
            print 'Channels:'
            for channel in channels:
                print '-',channel+':', channels[channel]
            print 'Services:'
            for service in services:
                print '-',service+':', services[service]
            print 'Gateways:'
            for gateway in gateways:
                print '-',gateway+':', gateways[gateway]
        except yaml.YAMLError as exc:
            print(exc)

class Gateway(object):
    def __init__(self, name):
        self.name = name