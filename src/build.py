from enum import Enum
from functools import partial

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from content import texts, talks


class Version(Enum):
    CONSICE = "CONSICE"
    DETAILED = "detailed"


def text(concise: str, detailed: str, version: Version):
    if version == Version.DETAILED:
        return detailed
    else:
        return concise


def render(version: Version = Version.DETAILED) -> str:
    env = Environment(loader=FileSystemLoader('.'))
    env.globals['text'] = partial(text, version=version)
    env.globals['version'] = version
    template = env.get_template('Template.html')
    return template.render(texts=texts, talks=talks)
