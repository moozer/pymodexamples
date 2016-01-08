
import yaml

ymlfile = "servers.yml"

f = open(ymlfile)

# use safe_load instead load
dataMap = yaml.safe_load(f)

f.close()

# and now we have a dictionary with all the data
print dataMap
