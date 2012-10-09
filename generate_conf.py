#!/usr/bin/python
import yaml
import sys

#cluster_name=sys.argv[1];
#hostname=sys.argv[2];


def load_yaml(fname):
	conf=dict();
	try: 
	  conf=yaml.load(open(fname))
	except IOError as e:
		print "Yaml File "+fname+" could not be loaded"
	return conf 

# loading all the confs
config=dict()
config['clusters']=load_yaml("clusters.yaml");
config['defaults']=load_yaml("defaults.yaml");
config['hosts']=load_yaml("hosts.yaml")


#trying to open cluster specific configs
clusters=config['clusters'];
for cname in clusters.keys():
	config["clusters"][cname]=load_yaml(cname+".yaml");

properties=dict();
properties.update(config['defaults']);

for a in config["clusters"]["emerald"]["datanodes"]:
	properties.update(a);

hostname="gs2120.red.ua2.inmobi.com"
if config['hosts'].has_key(hostname):
	for a in config['hosts'][hostname]:
        	properties.update(a);
else:
   print "No Configs found for the specific host "+ hostname

print properties
