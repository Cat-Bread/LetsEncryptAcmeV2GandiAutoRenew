import ConfigParser as configparser
import sys
import os
import requests
import json
import ipaddress
    
config_file = "config-updatenskey"

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

def get_current_keys(key_path):
    try:
        for root, dirs, files in os.walk(key_path):
            return files

    except Exception:
        print('Failed to get ns key')
        sys.exit(2)

def read_config(config_path):
    #Read configuration file
    cfg = configparser.ConfigParser()
    cfg.read(config_path)

    return cfg

def get_record(url, headers):
    #Get existing record
    r = requests.get(url, headers=headers)
    return r


def update_record(url, headers, payload):
    r = requests.put(url, headers=headers, json=payload)
    if r.status_code != 201:
        print('Record update failed with status code: %d' % r.status_code)
        sys.exit(2)
    return r


def main():
    path = config_file
    if not path.startswith('/'):
   	    path = os.path.join(SCRIPT_DIR, path)
    config = read_config(path)
    if not config:
        sys.exit("Please fill in the 'config.txt' file.")

    for section in config.sections():
        apikey = config.get(section, 'apikey')
        challengepath = config.get(section, 'challengepath')
        headers = { 'Content-Type': 'application/json', 'X-Api-Key': '%s' % config.get(section, 'apikey')}
        url = '%sdomains/%s/records/_acme-challenge/TXT' % (config.get(section, 'api'), config.get(section, 'domain'))
    print('challengepath = %s' % challengepath) 

    newkey = sys.argv[1]
    currentkeylist = get_current_keys(challengepath)

    print 'newkey = %s' % newkey

    # Create json record to update Gandi with new key
    gandiupdate = {'rrset_ttl': config.get(section, 'ttl'), 'rrset_values': [newkey]}

    # Get current gandi ns key
    print('url = %s' % url)
    record = get_record(url, headers)
 
    if record.status_code == 200:
        gandikeyvalue = json.loads(record.text)['rrset_values'][0]         
        print('Current/Old Gandi key value is: %s' % gandikeyvalue)
    else:
       sys.exit('No existing record: Check that dns _acme-challenge TXT record exists')
 
    # Check ns record key value 
    if newkey == gandikeyvalue:
        sys.exit("NS record already updated. No action taken.") 
    else: 	 
        update_record(url, headers, gandiupdate)
        print('New Gandi key value is: %s'% newkey)
  
sys.exit


if __name__ == "__main__":
    main()
