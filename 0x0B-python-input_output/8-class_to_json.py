  #!/usr/bin/python3
''' class_to_json function '''


def class_to_json(obj):
    ''' Returns dict description to json'''
    return obj.__dict__
