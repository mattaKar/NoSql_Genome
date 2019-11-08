from neo4j import GraphDatabase



class driverNeo4j():
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
        self._session = self._driver.session()
        self._session.run("MATCH (n) DETACH DELETE n")

    def add_link(self,prot1,prot2,poids):
            #print(1, [...])
            
            self._session.run("match (a:Proteine),(b:Proteine)  where a.name=$prot1 and b.name=$prot2 create (a)-[c:Dom]->(b) RETURN c",prot1=prot1,prot2=prot2)

    def add_prot(self, name):
        self._session.run("CREATE (prot:Proteine {name:$name})", name=name)

    def close(self):
        self._driver.close()

class DriverManager():
    def __init__(self, uri, user, password):
        self._uri = uri
        self._user = user
        self._password = password
        self.driver = None



    def __enter__(self):
        self.driver = driverNeo4j(self._uri,self._user,self._password)
        return self.driver

    def __exit__(self,exc_type, exc_value, exc_traceback):
        self.driver.close()
