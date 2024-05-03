Project using distributed DB/Tech and Visualization BI Software

Technologies: Python, Neo4j, Tableau

Dataset: https://www.kaggle.com/datasets/okhiriadaveoseghale/100000-sales-records

For this to work you must have a Neo4j Account and you can then plug in your URI to the "conn", and the user and pass into "user" and "pword"

This was meant to be used in a notebook given the technology stack, however there is also an option to use a python script version if you want, which can be added to in order to make it more friendly. The python file is just given as a starting point. If you desire to use the notebook, you can download the notebook afterwards into a script format.

The .twb is the file containing the visualizations. These visualizations are a series depicting three different scenarios to answer one question. The idea was to use the data to find the most cost effective way to increase profits in countries in the bottom 50th percentile of orders outside of the Major Regions. Major Region in this case is defined by the top 3 regions by sales/profit shown in the first dashboard.

The second dashboard is those non-major regions' countries split into the Cost/Profit for each item with the amount of units sold for those items. 

The final dashboard is used to give final recommendations of which months to run an ad campaign around the Lowest Cost/Highest Profit items in order to maximize the typical spending peaks. The idea behind choosing the months are to run the campaign before a general spending peak for that country. Logic being: money will be spent anyway, make them buy more of the most profitable items.