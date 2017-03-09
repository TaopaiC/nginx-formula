#!/usr/bin/env python
from jinja2 import Environment, FileSystemLoader
import os

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH)),
    trim_blocks=False)
 
 
def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def main():
    context = {
            'config': {
                'server': {
                    'renderToken': 'on',
                    'aenderToken': 'on',
                    'bbb': 'cc'
                    }
                }
            }
    context['config']['server'].update({
        'bbb': 'bb'
        })
    print render_template('nginx.conf', context)

if __name__ == "__main__":
    main()

