Crpyto Info Depictor
=======

What you'll see
-----------
This project will create a webpage depicting the purchase and sell price of Cryto Currency's, specifically
Bitcoin and Ethereum from coinbase and blockchain. It will also provide recommendations in regards to what exchange one should buy and/or sell each coin.

The title of each exchange hovers above the selling/purchase prices of each respective coin. This title also serves as a link to the websites homepage. The text found below the prices is the recommendation in regards where the user should buy and sell each coin to obtain optimal profit. Below this recommendation is a button to the coin information at the exchange name found above.

You will also find information on Dogecoin at the bottom of the page, also informing on the purchase/selling price of each exchange.

The Check Me Out link is a fun little link to who made the page.

How to Run
-----------

In order to properly run this project you must first install Poetry, a tool used for dependency management and packaging in Python. A link to the installation documents can be found here:
>https://python-poetry.org/docs/

Following installation run the command "poetry install", this will obtain all the dependency's required for running this project.

In order to run the application, you must first execute the following command:
> poetry run python crypto_proj/crypto_flask.py

 This will cause the program to run on local host 5000. The webpage is located in the following url:
 >http://127.0.0.1:5000/webpage

 Questionnaire
 -----------
 1. One optimization is allowing the system to fail gracefully. This means allowing coins found at one exchange
 location to be obtainable, despite not being found in the other exchange place.

 2. I would say that some portions of over designing this application was allowing for scalability. I believe the way my logic is structured and implemented allows for easily scaling the application to get the prices of many different coins at these two chosen exchange locations. It is also easy to integrate more exchanges, simply by defining the required URL to get API requests. Create a function to return a dictionary of the required values, and then implement the find_best method with output of this function.

 3. If I had to scale my solution to 100 users/second traffic, I would create a cache of recently searched for coins. Once this data was stored I could simply update it X times every 5 seconds, and use the information stored in the database to increase response time. In other words, this would result in less calls to the exchange companies API, resulting in quicker results. 

 4. One enhancement I would make would be to allow realtime information from each exchange to be depicted on the webpage.  
