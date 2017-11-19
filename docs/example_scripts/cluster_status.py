import os
from ibm_analytics_engine import CloudFoundryAPI, IAE

os.environ["LOG_LEVEL"] = "DEBUG"

cf_api_key_filename = os.environ['API_KEY_FILENAME']
cluster_instance_guid = os.environ['CLUSTER_INSTANCE_GUID']

cf = CloudFoundryAPI(api_key_filename=cf_api_key_filename)
iae = IAE(cf_client=cf)
status = iae.status(cluster_instance_guid)

print(status)
