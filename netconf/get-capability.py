from ncclient import manager

m = manager.connect(host="10.0.0.1", port=830, username="cisco", password="cisco", hostkey_verify=False)

for RSTForum in m.server_capabilities:
	print(RSTForum)	


