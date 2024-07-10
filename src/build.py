import datetime
import os
from dataclasses import dataclass

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader


src_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(src_path)
target_path = f'{root_path}/target'

@dataclass
class Link:
    name: str
    link: str


talks = [
    Link("Intro to Scala.js",                               "https://www.youtube.com/watch?v=QTGtCTtIrHc"),
    Link("Scala.js: When TypeScript is Not Enough",         "https://youtu.be/Ln8woWsIBoI?t=2h10m7s"),
    Link("Metaprogramming in Scala",                        "https://www.youtube.com/watch?v=AbIasjx6yPA"),
    Link("Integration Testing of Microservices with Scala", "https://www.youtube.com/watch?v=zE2sLcIeoZk"),
    Link("Pure FP: Why and How",                            "https://www.youtube.com/watch?v=pCtTBUeO41w"),
    Link("Production-Ready Functional Programming",         "https://youtu.be/wROJoMUHLck"),
]


def render(with_cover_letter: bool = True) -> str:
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('Template.html')
    return template.render(
        talks=talks,
        year=datetime.datetime.now().year,
        with_cover_letter=with_cover_letter,
    )


def build_html():
    os.makedirs(target_path, exist_ok=True)

    with open(f"{target_path}/cv.html", "w") as file:
        file.write(render(with_cover_letter=False))

    with open(f"{target_path}/cv_with_cover_letter.html", "w") as file:
        file.write(render(with_cover_letter=True))


if __name__ == '__main__':
    # print(__file__)
    # print(os.path.abspath(__file__))
    # print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    build_html()
