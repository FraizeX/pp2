import json
with open ('sample-data.json') as file:
    data = json.load(file)
    
list = []

for item in data['imdata']:
    atr = item['l1PhysIf']['attributes']
    list.append({
        'dn': atr.get('dn'),
        'descr': atr.get('descr'),
        'speed': atr.get('speed'),
        'mtu': atr.get('mtu')
    })

txt = """
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
"""

print(txt)

for item in list:
    print(item['dn'], str(" " * int(55 - len(item['dn']))), item['descr'], str(" " * int(20 - len(item['speed']))), item['speed'], str(" " * int(5 - len(item['mtu']))), item['mtu'])