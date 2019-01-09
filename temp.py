# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

import nidaqmx.system
system = nidaqmx.system.System.local()

for device in system.devices:
    device_name = device.name

print(device_name)

print(device_name+'/ai0')
'''
device = system.devices['Dev1']
phys_chan = device.ai_physical_chans['ai0']
print(phys_chan.name)
'''
