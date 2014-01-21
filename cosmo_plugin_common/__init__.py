import json
import os

class Config(object):
	def get(self):
		which = self.__class__.which
		env_name = which.upper() + '_CONFIG_PATH'
		config_path = os.getenv(env_name, os.path.expanduser('~/' + which + '_config.json'))
		with open(config_path) as f:
			cfg = json.loads(f.read())
		return cfg
