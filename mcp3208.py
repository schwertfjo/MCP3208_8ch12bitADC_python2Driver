#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from spidev import SpiDev

class MCP3208:
    def __init__(self, bus = 0, device = 0, channel = 0):
        self.bus, self.device, self.channel = bus, device, channel
        self.spi = SpiDev()

    def __enter__(self):
        self.open()
        self.spi.max_speed_hz = 200000
        return self

    def open(self):
        self.spi.open(self.bus, self.device)
    
    def read(self):
        if self.channel > 7 or self.channel < 0:
            return -1
        adc = self.spi.xfer2([ (24 + self.channel) << 2, 0, 0])
        data = (adc[1] << 4) | (adc[2] >> 4)
        return data

    def __exit__(self, type, value, traceback):
            self.close()
            
    def close(self):
        self.spi.close()

#test
if __name__ == "__main__":
    while True    
        with MCP3208(bus = 0, device = 0, channel = 0) as ch0:
            print ch0.read()
        time.sleep(1)

