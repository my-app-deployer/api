# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from v1.models import Server, Job, Command, Routine
__author__ = "tricci"
__date__ = "$30 avr. 2015 13:57:31$"

def boot(ClassName):
  c = ClassName
  return c
class JobStack(object):
	"""docstring for JobStack"""
	def __init__(self, commands, server):
		self.server=server
		self.commands=commands.split('\n')
	def update(self,server=None):
		for srv in self.servers:
			if len(srv.jobs.pending):
				
queue=[
{
	"Server_id":"id",
	"jobs":{
		"pending":{
			"cd {{app}}",
			"composer update"
		},
		"current":{
			"composer install"
		},
		"done":{
			"rm -rf {{app}}/cache/"
		}
	}
	
},
{
	"Server_id":"id2",
	"jobs":{
		"pending":{
			"cd {{app}}",
			"composer update"
		},
		"current":{
			"composer install"
		},
		"done":{
			"rm -rf {{app}}/cache/"
		}
	}
	
}


]
