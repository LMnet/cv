from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from content import texts


def render():
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('Template.html')
    return template.render(texts=texts)
