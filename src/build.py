from dataclasses import dataclass

@dataclass
class NamedLink:
    name: str
    link: str


talks = [
    NamedLink("Intro to Scala.js" "Intro to Scala.js", "https://www.youtube.com/watch?v=QTGtCTtIrHc"),
    NamedLink("Scala.js: When TypeScript is not enough", "https://youtu.be/Ln8woWsIBoI?t=2h10m7s"),
    NamedLink("Metaprogramming in Scala", TODO),
    NamedLink("Integration testing of microservices with Scala", "https://www.youtube.com/watch?v=zE2sLcIeoZk"),
    NamedLink("Pure FP: why and how", "https://www.youtube.com/watch?v=pCtTBUeO41w"),
    NamedLink("Production-ready functional programming", "https://youtu.be/wROJoMUHLck"),
]

podcasts = [
    NamedLink("scalalaz", "https://scalalaz.ru"),
    NamedLink("flatmappers", "https://flatmappers.com"),
]


about = """
Open-source contributor. Co-maintained testcontainers-scala and fs2-kafka libraries. Also contributed to
kafka, cats, monix and many others.

Co-host of scala and fp oriented podcasts scalalaz and flatmappers.

Speaker: Intro to Scala.js; Scala.js: When TypeScript is not enough; Metaprogramming in
Scala; Integration testing of microservices with Scala; Pure FP: why and how; Production-ready functional
programming.
"""
