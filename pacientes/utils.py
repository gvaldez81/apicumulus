import json
from django.core import serializers

def to_json(objct, multi=False):
    if not multi:
        obj_str = serializers.serialize('json', [objct, ])
        obj_json = json.loads(obj_str)[0]

        return pretty_json(obj_json)
    else:
        obj_str = serializers.serialize('json', objct)
        obj_json = json.loads(obj_str)

        return [pretty_json(ugly_json) for ugly_json in obj_json]

def pretty_json(ugly_json):
    oid = ugly_json.pop('pk', 0)
    fields = ugly_json.pop('fields', {})
    ugly_json.pop('model', '')

    ugly_json['id'] = oid
    ugly_json.update(fields)

    return ugly_json
