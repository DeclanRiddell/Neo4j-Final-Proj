#!/usr/bin/env python
# coding: utf-8

# Neo4j Connection and Import CSV with Query Function
# 
# Declan Riddell

# In[26]:


import neo4j
from neo4j import GraphDatabase

URI = "conn"
AUTH = ("user", "pword")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()


# Database Design:
# 
# Order - [:Contains_Item]- Item - [:From_Country] -> [:From_Region]

# In[20]:


summary = driver.execute_query(
    """LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/DeclanRiddell/Neo4j-Final-Proj/main/dataSet/100000SalesRecords.csv' as row 
        with row where row is not null
        MERGE (i:Item{name : row.`Item Type`})
        SET
        i.SalesChannel = row.`Sales Channel`,
        i.ShipDate = row.`Ship Date`,
        i.UnitsSold = row.`Units Sold`,
        i.UnitPrice = row.`Unit Price`,
        i.UnitCost = row.`Unit Cost`,
        i.TotalRevenue = row.`Total Revenue`,
        i.TotalCost = row.`Total Cost`,
        i.TotalProfit = row.`Total Profit`
        MERGE (o:Order {name: row.`Order ID`}) 
        SET
        o.OrderPriority = row.`Order Priority`,
        o.OrderDate = row.`Order Date`,
        o.OrderID = row.`Order ID`
        MERGE (c:Country {name: row.Country}) 
        MERGE (r:Region {name: row.Region}) 
        MERGE (c)-[:IN_REGION]->(r)
        merge (i)-[:FROM_REGION]->(r)
        merge (i)-[:FROM_COUNTRY]->(c)
        merge (o)-[:CONTAINS_ITEM]->(i)""",
    database_="neo4j",
).summary

print("Created {nodes_created} nodes in {time} ms.".format(
    nodes_created=summary.counters.nodes_created,
    time=summary.result_available_after
))


# Reusable Query Function

# In[28]:


query = """
    Match (n) return n
"""


driver.execute_query(query, database_="neo4j")


# Now you can run whatever queries you want by copying and pasting this cell and changing the query command!
