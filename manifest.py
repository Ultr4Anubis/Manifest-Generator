import uuid
import json
name=input('Please enter the name of your manifest: ')
desc=input('Please enter the description for your manifest: ')
manitype = ''

while True:
    manitype=input('Which type of manifest would you like to generate? a|resources or b|data? Please enter either a or b: ')
    if manitype == 'a' or manitype == 'b':
        break

manifest_type = ''
if manitype == 'a':
    manifest_type = 'resources'
elif manitype == 'b':
    manifest_type = 'data'


manifest_json = {'format_version': 2, 'header': {'name': name, 'description': desc, 'uuid': str(uuid.uuid4()), 'version': [1,0,0],'min_engine_version': [1,16,100]},'modules': [{'type': manifest_type, 'uuid': str(uuid.uuid4()), 'version': [1,0,0]}]}
json=json.dumps(manifest_json, indent=4)

print(json)
