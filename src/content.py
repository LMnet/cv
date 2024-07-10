from dataclasses import dataclass


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
