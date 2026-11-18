import re

my_stack = '''
<SWITCH1> display stack
Stack mode: Service-port
Stack topology type: Link
Stack system MAC: 0018-82b1-6eb4
MAC switch delay time: 2 min
Stack reserved vlan: 4093
Slot of the active management port: --
Slot    Role        Mac address       Priority   Device type
-------------------------------------------------------------
    0   Master      0018-82b1-6eb4    200        S5700-28P-LI-AC
    1   Standby     0018-82b1-6eb6    150        S5700-28P-LI-AC
    2   Linecard    0018-82b1-6eb2    100        S5700-48P-LI-AC
    3   Linecard    0018-82b1-6eb2    100        S5200-48P-SI-AC
'''

# my_stack = '''
# <SWITCH2> display stack
# Stack mode: Service-port
# Stack topology type: Link
# Stack system MAC: 0018-82b1-6eb4
# MAC switch delay time: 2 min
# Stack reserved vlan: 4093
# Slot of the active management port: --
# Slot    Role        Mac address       Priority   Device type
# -------------------------------------------------------------
#     0   Master      0018-82b1-6eb4    200        S5200-48P-SI-AC
#     1   Standby     0018-82b1-6eb6    150        S5700-28P-LI-AC
#     2   Linecard    0018-82b1-6eb2    100        S5200-48P-SI-AC
# '''

# Find hostname
pattern_hostname = re.compile(r"<\w{6}\d{1,2}>")
hostname = pattern_hostname.findall(my_stack)

# Find Slot
pattern_slot = re.compile(r"")
slots = pattern_slot.findall(my_stack)

# Find Switch Type
pattern_type = re.compile(r"")
type = pattern_type.findall(my_stack)

print(hostname)