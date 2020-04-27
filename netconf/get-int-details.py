from ncclient import manager
import xml.dom.minidom

m = manager.connect(host="10.0.0.1", port=830, username="cisco", password="cisco")
RSTForum_filter = '''
 <filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
   <interface>
    <GigabitEthernet>
     <name>2</name>
    </GigabitEthernet>
   </interface>
  </native>
 </filter>
'''
print("----------------------")
print("RSTForum- Configuration Parameters:")
print("----------------------")
result = m.get_config('running', RSTForum_filter)
print(xml.dom.minidom.parseString(str(result)).toprettyxml())
print("----------------------")
print("RSTForum- Thanks you:")
print("----------------------")
