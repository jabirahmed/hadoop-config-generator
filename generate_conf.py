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

def generate_xml(cluster,configutration,component,hostconfig,hostname="all"):
       # this would generate the config files core-site.xml , mapred-site.xml and hdfs-site.xml
       print configutration
       print configutration[cluster][component]
       if hostname in hostconfig["hosts"]:
       		print hostconfig["hosts"][hostname]; 

		

config=dict()
config['clusters']=load_yaml("clusters.yaml");
config['defaults']=load_yaml("defaults.yaml");
config['hosts']=load_yaml("hosts.yaml")

print config;
clusters=config['clusters'];

for root in clusters.keys():
	clusternames=clusters[root].keys()

print clusternames

#trying to open cluster specific configs

for cname in clusternames:
		config[cname]=load_yaml(cname+".yaml");
#print config

generate_xml("emerald",config["emerald"],"datanodes",config["hosts"],'ergs4101.grid.lhr1.inmobi.com');
