import os
import json

vcap_application = json.loads(os.environ['VCAP_APPLICATION'])

vcap_variables = ["application_id", "name", "instance_index", "space_name"]

tags = []

for vcap_var_name in vcap_variables:
    vcap_var = vcap_application.get(vcap_var_name)
    if vcap_var:
        key = vcap_var_name
        if vcap_var_name == 'name':
            key = 'application_name'
        tags.append("{0}:{1}".format(key, vcap_var))

uris = vcap_application.get('uris')
if uris:
    for uri in uris:
        tags.append("uri:{0}".format(uri))

print json.dumps(tags)