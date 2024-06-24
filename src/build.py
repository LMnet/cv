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


parrot = """
Combination of backend development (Java) and data engineering (Scala, Python). Backends were mostly scrappers for sites like YouTube, Tumblr, Wiki, etc. Mainly worked as a data engineer: Spark, Airflow, Redshift, MySQL, DuckDB. Everything was in AWS: S3, RDS, EMR, Dynamo, OpenSearch, Kinesis, etc.
"""

dgis = """
<p>
The main product of the 2gis is online maps. I worked in 2 teams:
</p>
<p>
1.Ads + Big Data team. Mostly worked on a HTTP backend for serving personalized ads. Also I created a kafka-to-hdfs connector with the exactly-once delivery semantic using akka-streams. Occasionally worked with Spark. Techologies: Akka, Kafka, Spark, Hadoop.
</p>
<p>
2. Since Nov 2018 — the team focused on displaying products (goods) on the map. Participated in an architecture design of a whole new project from the start. Did a massive impact on a system in general, as well as designed and implemented a few crucial components.
</p>
<p>
The system was designed as a group of microservices, which are mostly streaming services based on Kafka. Some of them were built with the kafka-streams. But most of the scala services were written in a purely functional manner using Typelevel libraries: cats, cats-effect (with the tagless-final), fs2, fs2-kafka, doobie, etc.
</p>
<p>
Also, I used RabbitMQ, PostgreSQL, RocksDB, and ElasticSearch occasionally.
</p>
<p>
Eventually, I’ve become a lead developer: partially team management (resource planning, product planning, project management), hiring, mentoring (including internal Scala courses).
</p>
"""

datamonsters = """
Participated in a few projects. Mostly worked on a mobile messenger. It was a full-stack Scala development: Scala on the backend, Scala.js (through Cordova) on the frontend. Techs: Scala, Scala.js, Cordova, Akka, Play, RethinkDB.
"""

xored = """
Worked on the Cisco XMP Topology: it’s a network topology visualization project. Backend: Java, Spring, Hibernate. Frontend: JavaScript, Dojo, TomSawyer, mxGraph.
"""

pinpay = """
<p>
Worked on 2 projects (~50/50):
</p>
<p>
1. JavaScript-based (webkit) GUI of the ATM (which was mostly a C++ Qt project).
</p>
<p>
2. Java EE processing backend. Techs: Java, Spring, Hibernate, OracleDB.
</p>
<p>
At some point I became a team leader: project management, architecture, mentoring. Introduced a continuous integration pipeline (using Jenkins), SVN to git migration, massively improved documentation processes.
</p>
"""

diasoft = """
Java fintech: Java EE, SOAP, OracleDB, MsSQL, DB2, Sybase.
"""

saytostroy = """
Small web-studio: LAMP stack, HTML, JavaScript.
"""

hr_friendly_description = """
I am a highly experienced and versatile software engineer with a strong background in backend development, data engineering, and full-stack development. My skills include working with various programming languages such as Scala, Java, JavaScript, and Python. I have a deep understanding of both functional and object-oriented programming paradigms. I have successfully led teams, managed projects, and mentored junior developers, ensuring the delivery of high-quality software solutions.

I focus on developing high-load systems, big data processing systems, and building robust, maintainable solutions. I have experience in designing and implementing scalable microservices architectures and have a strong background in data processing and analytics. I enjoy working in collaborative environments and am effective in bridging the gap between technical and non-technical stakeholders to ensure the successful alignment of development efforts with organizational goals.

I excel in environments that leverage cutting-edge technologies and value continuous improvement and innovation. My experience in designing and implementing scalable (micro)services architectures, coupled with a strong background in data processing and analytics, enables me to drive impactful solutions that meet business objectives. I enjoy working in collaborative environments and strive to contribute effectively to team success.
"""

scala_open_source = """
Throughout my career, I have contributed to open-source projects, including co-maintainense of popular libraries such as testcontainers-scala and fs2-kafka, and occassional contributions to projects such as Kafka, Cats, Monix, Airflow, and others. 
"""

talks_and_podcasts = """
As an active community member, I co-host Scala and functional programming podcasts and have delivered several talks at industry conferences.
"""
