# /usr/bin/python

from pprint import pprint
from random import choice

from netapp.santricity.api.v2.storage_systems_api import StorageSystemsApi
from netapp.santricity.api.v2.volumes_api import VolumesApi
from netapp.santricity.api_client import ApiClient
from netapp.santricity.configuration import Configuration
from netapp.santricity.rest import ApiException

config = Configuration()

config.host = "http://mpstack.wic.openenglab.netapp.com:8081"  # Add ip address of the proxy here
config.username = "rw"
config.password = "rw"

GB = 1024 ** 3

api_client = ApiClient()
config.api_client = api_client

system_api = StorageSystemsApi(api_client=api_client)

# Get storage system status
try:
    storage_system = system_api.get_storage_system(system_id="1")
except ApiException as e:
    # Handle exception here
    raise
else:
    if storage_system.status in ['optimal', 'needsAttn']:
        print("Using Storage-System - %s, Status: %s" % (storage_system.name, storage_system.status))

        # Get all volumes info for each storage system
        volume_api = VolumesApi(api_client=api_client)
        volumes = volume_api.get_all_volumes(system_id=storage_system.id)

        # Get all volume group info for each storage system
        vgs = volume_api.get_all_storage_pools(system_id=storage_system.id)
        vg = choice([vg for vg in vgs if vg.free_space > 1 * GB])
        print("Selected volumeGroup %s with free capacity of %s bytes and raidLevel of %s." %
              (vg.name, vg.free_space, vg.raid_level))

        vol = volume_api.new_volume(storage_system.id,
                                    body={"name": "myVolume", "size": 1, "sizeUnit": "gb", "poolId": vg.id})
        pprint(vol)

        # For demonstration purposes
        # volume_api.remove_volume(storage_system.id, vol.id)
