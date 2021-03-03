import re

def snake_to_camel_case(camel):
    if camel[0] == '_':
        camel = camel[1:]
    camel = ''.join(x.capitalize() or '_' for x in camel.split('_'))
    return camel[0].lower() + camel[1:]

def camel_to_snake_case(snake):
    snake = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', snake)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', snake).lower()