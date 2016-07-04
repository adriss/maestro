# -*- coding: utf8 -*-
from compose.integration.gateway.http import HttpBuilder

BUILDERS = {'http': HttpBuilder()}

class GatewayBuilders(object):
    @staticmethod
    def builder(bld,):
        return BUILDERS[bld]