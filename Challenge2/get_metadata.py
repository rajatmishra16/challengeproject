import requests
import json

metadata_url = 'http://169.254.169.254/latest/'


def metadata_tree(metadata_url, base):
    output = {}
    for item in base:
        new_metadata_url = metadata_url + item
        r = requests.get(new_metadata_url)
        text = r.text
        if item[-1] == "/":
            list_of_values = r.text.splitlines()
            output[item[:-1]] = metadata_tree(new_metadata_url, list_of_values)
        elif is_json(text):
            output[item] = json.loads(text)
        else:
            output[item] = text
    return output

def get_metadata():
    base = ["meta-data/"]
    result = metadata_tree(metadata_url, base)
    return result


def get_metadata_json_format():
    metadata = get_metadata()
    metadata_json = json.dumps(metadata, indent=4, sort_keys=True)
    return metadata_json


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True

def gen_dict_extract(key, metadata):
    if hasattr(metadata, 'items'):
        for k, v in metadata.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result


def find_key(key):
    metadata = get_metadata()
    return list(gen_dict_extract(key, metadata))

usage = input("If you want to see complete metadata, Please press \'M/m\'. If you want to see particular metadata key, Please Press \'K/k\':")
if usage == M or usage == m:
    print(get_metadata_json_format())
elif usage == K or usage == k:
    key = input("Please Enter meta-data key:\n")
    print(find_key(key))
else:
    print("Incorrect Usage")
    