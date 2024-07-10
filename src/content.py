from dataclasses import dataclass
from types import SimpleNamespace as ns

@dataclass
class Link:
    name: str
    link: str


talks = [
    Link("Intro to Scala.js",                               "https://www.youtube.com/watch?v=QTGtCTtIrHc"),
    Link("Scala.js: When TypeScript is not enough",         "https://youtu.be/Ln8woWsIBoI?t=2h10m7s"),
    Link("Metaprogramming in Scala",                        "https://www.youtube.com/watch?v=AbIasjx6yPA"),
    Link("Integration testing of microservices with Scala", "https://www.youtube.com/watch?v=zE2sLcIeoZk"),
    Link("Pure FP: why and how",                            "https://www.youtube.com/watch?v=pCtTBUeO41w"),
    Link("Production-ready functional programming",         "https://youtu.be/wROJoMUHLck"),
]

texts = ns(
    # TODO
    new_zealand_remote = """
        <p>
        I'm currently in New Zealand and would like to know if remote work from here is possible. I'm not seeking for relocation or visa support, only remote work. If it's not an option, I'd appreciate a direct indication of that fact in the response.
        </p>
    """,
)
