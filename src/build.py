import datetime
import os
from dataclasses import dataclass

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from playwright.sync_api import sync_playwright

path_src = os.path.dirname(os.path.abspath(__file__))
path_root = os.path.dirname(path_src)
path_target = f"{path_root}/cv"
path_cv_html = f"{path_target}/cv.html"
path_cv_cover_letter_remote_html = f"{path_target}/cv_cover_letter_remote.html"

# TODO: add download as pdf button to the footer

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
    env = Environment(loader=FileSystemLoader(path_src))
    template = env.get_template("Template.html")
    return template.render(
        talks=talks,
        year=datetime.datetime.now().year,
        with_cover_letter=with_cover_letter,
    )


def build_html():
    with open(path_cv_html, "w") as file:
        file.write(render(with_cover_letter=False))

    with open(path_cv_cover_letter_remote_html, "w") as file:
        file.write(render(with_cover_letter=True))


def build_pdf(html_file_path):
    path, _ = os.path.splitext(html_file_path)
    pdf_file_path = f"{path}.pdf"

    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path="/usr/bin/google-chrome-stable")

        page = browser.new_page()
        page.goto(f'file://{html_file_path}')
        page.pdf(path=pdf_file_path, format='A4', margin={
            'top': '1cm',
            'bottom': '1cm',
            'left': '1cm',
            'right': '1cm'
        })

        browser.close()


if __name__ == '__main__':
    build_html()
    build_pdf(path_cv_html)
    build_pdf(path_cv_cover_letter_remote_html)
