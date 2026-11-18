import re

my_mac_address = '''
R1#show mac addr
          Mac Address Table
-------------------------------------------
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    fc15.b413.114a    DYNAMIC     Gi0/1
  10    fc15.b417.0280    DYNAMIC     Gi0/1
  10    fc15.b417.70e8    DYNAMIC     Gi0/1
  10    fc15.b419.84fc    DYNAMIC     Gi0/1
  10    fc15.b419.9884    DYNAMIC     Gi0/1
   1    0008.e3ff.fd90    DYNAMIC     Gi0/1
   1    001d.70b5.4e00    DYNAMIC     Gi0/1
   1    0026.9861.881a    DYNAMIC     Gi0/1
   1    1caa.07c3.629a    DYNAMIC     Gi0/1
   1    2c0b.e954.f317    DYNAMIC     Gi0/1
   1    5006.0447.361a    DYNAMIC     Gi0/2
   1    5006.0447.3640    DYNAMIC     Gi0/2
   1    5061.bf82.6217    DYNAMIC     Gi0/1
   1    d824.bdb1.7bc0    DYNAMIC     Gi0/2
 125    000a.8302.58c4    DYNAMIC     Gi0/1
 125    000a.8302.58c5    DYNAMIC     Gi0/1
 125    000a.8302.58c8    DYNAMIC     Gi0/1
 125    000a.8302.58cd    DYNAMIC     Gi0/1
 128    0010.f348.ce67    DYNAMIC     Gi0/1
 128    001c.2000.118b    DYNAMIC     Gi0/1
 128    001c.2000.143e    DYNAMIC     Gi0/1
 128    001c.2000.14fd    DYNAMIC     Gi0/1
 128    001c.2000.29cf    DYNAMIC     Gi0/1
 143    9c14.6366.2383    DYNAMIC     Gi0/1
 143    e050.8b31.1671    DYNAMIC     Gi0/1
 143    e050.8b31.1672    DYNAMIC     Gi0/1
1200    b878.7920.7a91    DYNAMIC     Gi0/1
1200    b878.7920.7be4    DYNAMIC     Gi0/1
Total Mac Addresses for this criterion: 1945
'''

pattern = re.compile(r'\d*\s{4}\w{4}\.\w{4}\.\w{4}')
matches = pattern.findall(my_mac_address)

if matches:
    for match in matches:
        entry = match.split()
        print(entry[0] + ";" + entry[1])

else:
    print("Error.")