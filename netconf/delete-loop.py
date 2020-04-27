from ncclient import manager
import xml.dom.minidom

# IOS XE Settings
RSTForum_host = "10.0.0.1"
RSTForum_port = 830
RSTForum_username = "cisco"
RSTForum_password = "cisco"

m = manager.connect( host=RSTForum_host, port=RSTForum_port, username=RSTForum_username, password=RSTForum_password, hostkey_verify=False, look_for_keys=False )

RSTForum_netconf_template = """
<config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface operation="delete">
                        <name>Loopback1</name>
                </interface>
        </interfaces>
</config>
"""

print("----------------------")
print("RSTForum- Configuration Parameters:")
print("----------------------")
print(RSTForum_netconf_template)

RSTForum_netconf_reply = m.edit_config(RSTForum_netconf_template, target = "running")

print(xml.dom.minidom.parseString(RSTForum_netconf_reply.xml).toprettyxml())

m.close_session()

# Print the NETCONF Reply
print(RSTForum_netconf_reply)
print("----------------------")
print("RSTForum- Thanks you:")
print("----------------------")
