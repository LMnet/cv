import datetime

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

from content import talks


def render(with_cover_letter: bool = True) -> str:
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('Template.html')
    return template.render(
        talks=talks,
        year=datetime.datetime.now().year,
        with_cover_letter=with_cover_letter,
    )
