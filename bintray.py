import json
import subprocess

try:
    v = subprocess.check_output(['git', 'describe', '--dirty'], stderr=subprocess.DEVNULL).decode().strip().replace('-','b', 1).replace('-','.')
except subprocess.CalledProcessError as e:
    v = open('version').read().strip()

o = {
        'package': {
            'name': 'pros-cli',
            'repo': 'pros',
            'subject': 'purdue-sigbots'
        },
        'version': {
            'name': v,
            'desc': subprocess.check_output(['git', 'log', '-1', '--format=%B']).decode().strip()
        },
        'files': [
            { 'includePattern': './(pros_cli-.*\\.zip)', 'uploadPattern': '$1' },
            { 'includePattern': './dist/(.*\\.whl)', 'uploadPattern': '$1' }
        ],
        'publish': 'true'
    }

with open('bintray.json', 'w') as f:
    json.dump(o, f)