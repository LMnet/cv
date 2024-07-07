from dataclasses import dataclass
from types import SimpleNamespace as ns


@dataclass
class Link:
    name: str
    link: str


talks = [
    Link("Intro to Scala.js" "Intro to Scala.js", "https://www.youtube.com/watch?v=QTGtCTtIrHc"),
    Link("Scala.js: When TypeScript is not enough", "https://youtu.be/Ln8woWsIBoI?t=2h10m7s"),
    Link("Metaprogramming in Scala", "https://www.youtube.com/watch?v=AbIasjx6yPA"),
    Link("Integration testing of microservices with Scala", "https://www.youtube.com/watch?v=zE2sLcIeoZk"),
    Link("Pure FP: why and how", "https://www.youtube.com/watch?v=pCtTBUeO41w"),
    Link("Production-ready functional programming", "https://youtu.be/wROJoMUHLck"),
]

podcasts = [
    Link("scalalaz", "https://scalalaz.ru"),
    Link("flatmappers", "https://flatmappers.com"),
]

texts = ns(
    about = ns(
        consice = """
            Open-source contributor. Co-maintained testcontainers-scala and fs2-kafka libraries. Also contributed to
            kafka, cats, monix and many others.
            
            Co-host of scala and fp oriented podcasts scalalaz and flatmappers.
            
            Speaker: Intro to Scala.js; Scala.js: When TypeScript is not enough; Metaprogramming in
            Scala; Integration testing of microservices with Scala; Pure FP: why and how; Production-ready functional
            programming.
            """,

        detailed_main = """
            I am a highly experienced and versatile software engineer with a strong background in backend development, data engineering, and full-stack development. My skills include working with various programming languages such as Scala, Java, JavaScript, and Python, and I have a deep understanding of both functional and object-oriented programming paradigms. I have successfully led teams, managed projects, and mentored developers, ensuring the delivery of high-quality software solutions.
        
            My primary focus is on developing high-load systems, big data processing systems, and building robust, maintainable solutions. With expertise in designing and implementing scalable microservices architectures, batch and streaming data processing pipelines, and distributed systems, I create effective solutions that meet business goals. My extensive experience with both pragmatic and bleeding-edge technologies allows me to adapt to different project needs effectively.
            """,

        scala_open_source = """
            Throughout my career, I have contributed to open-source projects, including co-maintenance of popular libraries such as testcontainers-scala and fs2-kafka, and occasional contributions to significant projects such as Kafka, Airflow, and Cats.
            """,

        talks_and_podcasts = """
            As an advocate for knowledge sharing and an active community member, I co-host Scala and functional programming podcasts and have delivered several talks at industry conferences.
            """,
    ),


    parrot = ns(
        consice = """
        <p>
        Combination of backend development (Java) and data engineering (Scala, Python). Backends were mostly scrappers for sites like YouTube, Tumblr, Wiki, etc. Also, I have been improving a complex Bittorrent system.
        </p>
        <p>  
        On the data engineering side: Spark, Airflow, Redshift, MySQL, DuckDB. Everything was in AWS: S3, RDS, EMR, Dynamo, OpenSearch, Kinesis, etc.
        </p>
        """,

        detailed = """
        <p>
        Combination of backend development and data engineering. On the backend side, I primarily worked with Java, developing and supporting scrapers for various sites such as YouTube, Tumblr, and Wikipedia. Additionaly, I have been improving a complex Bittorrent system that gets information about user's activity.
        </p>
        <p>
        Data engineering was mostly Scala development with a bit of Python. I handled large-scale data processing and analytics using technologies like Apache Spark, Apache Airflow, Amazon Redshift, MySQL, and DuckDB. I introduced and migrated all team's pipelines to Airflow. And was de-facto the administrator of company's Redshift cluster.
        </p>
        <p>
        The projects were hosted on AWS, utilizing a wide array of its services including S3, RDS (MySQL and PostgreSQL), EMR, DynamoDB, OpenSearch, and Kinesis.
        </p>
        <p>
        Among the interesting tasks I can mention a custom query language I've built on top of ElasticSearch. Also I initiated and migrated team's codebase into a monorepo, which greatly improved development experience.  
        </p>
        """,
    ),

    dgis = """
        <p>
        2gis is an online maps product (like Google Maps). I worked in 2 teams:
        </p>
        <p>
        1.Ads + Big Data team. Mostly worked on a HTTP backend for serving personalized ads. Also I created a kafka-to-hdfs connector with the exactly-once delivery semantic using akka-streams. Occasionally worked with Spark. Techologies: Akka, Kafka, Spark, Hadoop.
        </p>
        <p>
        2. Since Nov 2018 — the team focused on displaying products on the map. Participated in an architecture design of a whole new project from the start. Did a massive impact on a system in general, as well as designed and implemented a few crucial components.
        </p>
        <p>
        The system was designed as a group of microservices, which are mostly streaming services based on Kafka. Some of them were built with the kafka-streams. But most of them were written in a purely functional manner using Typelevel libraries: cats, cats-effect (with the tagless-final), fs2, fs2-kafka, doobie, etc.
        </p>
        <p>
        Also, I used RabbitMQ, PostgreSQL, RocksDB, and ElasticSearch occasionally.
        </p>
        <p>
        Eventually, I’ve become a lead developer: partially team management (resource planning, product planning, project management), hiring, mentoring (including internal Scala courses).
        </p>
        """,

    datamonsters = ns(
        consice = """
            Participated in a few projects. Mostly worked on a mobile messenger. This was a full-stack Scala development: Scala on the backend, Scala.js (through Cordova) on the frontend. Techs: Scala, Scala.js, Cordova, Akka, Play, RethinkDB.
            """,
        detailed = """
            <p>
            I participated in several projects, with the majority of my work focused on a mobile messenger project. This was a full-stack Scala development: Scala with Akka on the backend, and Scala.js (through Cordova) on the frontend. RethinkDB was used as the main database. The project was developed from scratch, and I was involved in both architecture design and functionality development.
            </p>
            <p>
            Other projects mainly included backend development using Scala, Akka, and Play framework with AWS infrastructure. Specifically, DynamoDB was used.
            </p>
            """,
    ),

    xored = ns(
        consice = """
            Worked on the Cisco XMP Topology: it’s a network topology visualization project. Backend: Java, Spring, Hibernate. Frontend: JavaScript, Dojo, TomSawyer, mxGraph.
            """,
        detailed = """
            <p>
            Mostly have been working on the Cisco XMP Topology project (part of the Cisco Prime Infrastructure platform).
            </p>
            <p>
            The project is designed for visualizing network topologies. Backend technologies included Java, Spring, and Hibernate. The frontend was built using Dojo. Initially, the TomSawyer project was used for graph visualization but later it was switched to fully client-side rendering with mxGraph and a REST-like interface on the backend.
            </p>
            """,
    ),

    pinpay = ns(
        consice = """
            <p>
            Worked on 2 projects (~50/50):
            </p>
            <p>
            1. JS-based GUI (WebKit engine) of the ATM (which was mostly a C++ Qt project).
            </p>
            <p>
            2. Java EE processing backend. Techs: Java, Spring, Hibernate, OracleDB.
            </p>
            <p>
            At some point I became a team leader: project management, architecture, mentoring. Introduced a continuous integration pipeline (using Jenkins), SVN to git migration, massively improved documentation processes.
            </p>
            """,

        detailed = """
            <p>
            The company's product was physical ATMs for all sorts of payments. 
            </p>
            <p>
            I've been working mostly on 2 projects, with ~50/50 ratio:
            </p>
            <p>
            1. JavaScript-based interface of the ATM. The ATM itself was a C++ Qt project, but the GUI was written using web technologies on top of WebKit engine. I've built a completely new version using more modern tech stack: Backbone, RequireJS, LESS, Grunt, a lot of HTML5 и CSS3. Built an automated testing platform with Mocha and Chai. 
            </p>
            <p>
            2. Java EE processing backend. Supported a legacy version built with Java 7, Maven, Spring, Hibernate and OracleDB. Introduced unit testing with JUnit + JMockit. Later on I've designed and started to build a new version of the backend using Java 8, newer Spring 4 (core, data jpa, mvc, rest, security), and Gradle.  
            </p>
            <p>
            At some point I became a team leader: project management, architecture, mentoring. Introduced a continuous integration pipeline (using Jenkins), SVN to git migration (including introduction of git-flow approach). I conducted code reviews, trained colleagues, mainly in the testing department, and initiated the documentation process for products. 
            </p>
            """,

    ),

    diasoft = ns(
        consice = """
            Java fintech: Java EE, SOAP, OracleDB, MsSQL, DB2, Sybase.
            """,

        detailed = """
            Big fintech company. Development and support of a massive Java EE 7 product Flextera. A lot of SQL for different DBs, including OracleDB, MsSQL, DB2 and Sybase. The architecture was built on top of SOAP protocol.
            """,
    ),

    saytostroy = ns(
        consice = """
            Small web-studio: LAMP stack, HTML, JavaScript.
            """,

        detailed = """
            Small web-studio. I've been building small and medium websites using LAMP (Linux, Apache WebServer, MySQL, PHP) stack, HTML, CSS, JavaScript, jQuery and Node.js.
            """,
    ),
)
