# #!/usr/bin/env python

# import os, sys, pprint
# import yaml

# with open('config.yaml','r') as f:
#     config = yaml.safe_load(f)

# # pprint.pprint(config)
# # pprint.pprint(os.listdir(config['destiny']))
# # # pprint.pprint(config['period'])
# # pprint.pprint(config['servers'][1]['name'])
# # pprint.pprint(config['servers'][1]['user'])
# # pprint.pprint(config['servers'][1]['server_ip'])

# for server in config['servers']:
#     pprint.pprint(server['name'])
#     pprint.pprint(server['user'])
#     pprint.pprint(server['server_ip'])


a=['/tmp/reports/secondarylab/successful_logins/2024322_3-29---8_.txt', '/tmp/reports/secondarylab/successful_logins/2024322_3-30---24_.txt', '/tmp/reports/secondarylab/successful_logins/2024322_2-0---6_.txt', '/tmp/reports/secondarylab/successful_logins/2024322_1-59---35_.txt', '/tmp/reports/secondarylab/successful_logins/2024322_3-30---33_.txt', '/tmp/reports/secondarylab/successful_logins/2024322_3-32---2_.txt', '/tmp/reports/secondarylab/successful_logins/2024322_3-29---41_.txt']
print(a.sort())