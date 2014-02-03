import keystoneclient.v2_0.client as ksclient
import novaclient.v1_1.client as nvclient
import glanceclient.v2.client as glanceclient
import os

def get_keystone_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d

def get_nova_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d

keystone_creds = get_keystone_creds()
nova_creds = get_nova_creds()

keystone = ksclient.Client(**keystone_creds)
glance_endpoint = keystone.service_catalog.url_for(service_type='image',
                                                   endpoint_type='publicURL')
glance = glanceclient.Client(glance_endpoint, token=keystone.auth_token)
images = glance.images.list()

nova = nvclient.Client(**nova_creds)
nova.servers.list()

for image in glance.images.list():
    if "ubuntu" in i["name"]:
        print "Found image named ubuntu. Creating instance... ", i
        flavor = novaclient.flavors.find(name="m1.micro")
        instance = novaclient.servers.create(name="Test Script Server", image=i, flavor=flavor)
        break

