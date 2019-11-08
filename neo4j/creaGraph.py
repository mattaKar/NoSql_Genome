from connection import DriverManager
from collections import namedtuple


rela = namedtuple('rela','prot1 prot2 poids')

def getPoid():
    return 1

def test(domains):
    for a in domains:
        print(domains.tell(),)
        return a;

def TrouverLien(DescProt,domains):
    if DescProt!="":
        a = DescProt.split()
        prot1 = a.pop(0)
        for DescProt2 in domains:

            b = DescProt2.split()
            prot2 = b.pop(0)
            #print(b)


            if len(list(set(a) & set(b)))!=0:
                #print(f'prot1 = {prot1}////// prot2={prot2}')
                yield prot1,prot2,getPoid()
        """else:
            #print(" pas cool")
            yield(prot1,prot2,0)"""


with DriverManager("bolt://localhost:7687","neo4j","louis41260") as driver:


    with open('sample_domains.txt') as domains:
        for DescProt in domains:
            a = DescProt.split()
            driver.add_prot(a[0])



          #driv = DriverNeo4j("bolt://localhost:7687","neo4j","louis41260"
    with open('sample_domains.txt') as domains:
        DescProt = "a"
        i=1
        while DescProt != "":

            DescProt = domains.readline()
            li = domains.tell()
            i+=1

            for prot1,prot2,poids in TrouverLien(DescProt,domains):

                #print(domains.tell())
                driver.add_link(prot1,prot2,poids)

            print(f"i={i}")

            domains.seek(li)
