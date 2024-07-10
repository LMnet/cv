from dataclasses import dataclass
from types import SimpleNamespace as ns

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

texts = ns(
    # TODO
    new_zealand_remote = """
        <p>
        I'm currently in New Zealand and would like to know if remote work from here is possible. I'm not seeking for relocation or visa support, only remote work. If it's not an option, I'd appreciate a direct indication of that fact in the response.
        </p>
    """,
)
