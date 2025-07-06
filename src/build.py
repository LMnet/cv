import datetime
import os
from dataclasses import dataclass

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from playwright.sync_api import sync_playwright

base_url = "https://lmnet.github.io/cv"
src_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(src_path)
target_path = f"{root_path}/docs" # `/docs` because GitHub Pages requires this particular folder name


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


@dataclass
class CV:
    name: str
    render_config: dict | None = None

    @property
    def base_file_path(self) -> str:
        return target_path

    @property
    def html_file_path(self) -> str:
        return f"{self.base_file_path}/{self.name}.html"

    @property
    def pdf_file_path(self) -> str:
        return f"{self.base_file_path}/{self.name}.pdf"

    @property
    def html_link(self) -> str:
        return f"{base_url}/{self.name}.html"

    @property
    def pdf_link(self) -> str:
        return f"{base_url}/{self.name}.pdf"

    def render(self) -> str:
        env = Environment(loader=FileSystemLoader(src_path))
        template = env.get_template("Template.html")

        cv_render_config = self.render_config if self.render_config else {}

        render_params = {
            'talks': talks,
            'pdf_link': self.pdf_link,
        } | cv_render_config

        return template.render(render_params)

    def build_html(self):
        with open(self.html_file_path, "w") as file:
            file.write(self.render())

    def build_pdf(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path="/usr/bin/google-chrome-stable")

            year = datetime.datetime.now().year
            # Only inline styles work here
            footer_template = f"""
                <div style='
                    width: 100%;
                    text-align: right;
                    font-size: 12px;
                    font-style: italic;
                    color: #000;
                    padding-right: 36px;
                    font-family: "Times New Roman", serif;
                '>
                    Yury Badalyants, {year}
                </div>
            """

            page = browser.new_page()
            page.goto(f'file://{self.html_file_path}')
            page.pdf(
                path=self.pdf_file_path,
                format='A4',
                margin={
                    'top': '1cm',
                    'bottom': '1cm',
                    'left': '1cm',
                    'right': '1cm'
                },
                display_header_footer=True,
                header_template="<span></span>",
                footer_template=footer_template,
            )

            browser.close()

    def build_all(self):
        self.build_html()
        self.build_pdf()


main_cv = CV("cv")
cv_cover_letter_remote = CV("cv_cover_letter_remote", {'with_cover_letter': True})


if __name__ == '__main__':
    main_cv.build_all()
    cv_cover_letter_remote.build_all()
    print("CV build was successful")
