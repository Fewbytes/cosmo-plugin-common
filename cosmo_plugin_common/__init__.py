import json
import os

class Config(object):
	def get(self):
		which = self.__class__.which
		env_name = which.upper() + '_CONFIG_PATH'
		default_location_tpl = '~/' + which + '_config.json'
		default_location = os.path.expanduser(default_location_tpl)
		config_path = os.getenv(env_name, default_location)
		try:
			with open(config_path) as f:
				cfg = json.loads(f.read())
		except IOError:
			raise RuntimeError(
				"Failed to read {0} configuration from file '{1}'."
				"The configuration is looked up in {2}. If defined, environment variable "
				"{3} overrides that location.".format(
					which, config_path, default_location_tpl, env_name))
		return cfg
