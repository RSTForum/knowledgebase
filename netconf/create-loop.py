from ncclient import manager
import xmltodict
import xml.dom.minidom

m = manager.connect(host="10.0.0.1", port=830, username="cisco", password="cisco", hostkey_verify=False)

RSTForum_template = """
<config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                        <name>{int_name}</name>
                        <description>{int_desc}</description>
                        <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
                        <enabled>true</enabled>
                        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                                <address>
                                        <ip>{ip_address}</ip>
                                        <netmask>{subnet_mask}</netmask>
                                </address>
                        </ipv4>
                </interface>
        </interfaces>
</config>
"""

# Build the XML Configuration to Send
RSTForum_netconf_payload = RSTForum_template.format(int_name="Loopback1",
                                          int_desc="RSTForum NETCONF created Loopback",
                                          ip_address="2.2.2.2",
                                          subnet_mask="255.255.255.0"
                                          )

print("----------------------")
print("RSTForum- Configuration Parameters:")
print("----------------------")
print(RSTForum_netconf_payload)

# Send NETCONF <edit-config>
RSTForum_netconf_reply = m.edit_config(RSTForum_netconf_payload, target="running")

# Print the NETCONF Reply
print(RSTForum_netconf_reply)
print("----------------------")
print("RSTForum- Thanks you:")
print("----------------------")
