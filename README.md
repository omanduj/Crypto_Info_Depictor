Crypto Info Depictor
=======

What you'll see
-----------
This project will create a webpage depicting the purchase and sell price of Crypto Currencies, specifically
Bitcoin and Ethereum from coinbase and blockchain. It will also provide recommendations in regards to which exchange one should buy and/or sell from.

The title of each exchange hovers above the selling/purchase prices of each respective coin. This title also serves as a link to the website's homepage. The text found below the prices is the recommendation in regards where the user should buy and sell each coin to obtain optimal profit. Below this recommendation is a button to the coin information at the exchange name found above.

You will also find information on Dogecoin at the bottom of the page, also informing on its purchase/selling price at each exchange.

The "Check Me Out" link is a fun little link to who made the page.

How to Run
-----------

In order to properly run this project you must first install Poetry, a tool used for dependency management and packaging in Python. A link to the installation documents can be found here:
>https://python-poetry.org/docs/

Following installation run the command "poetry install", this will install all the project's dependencies.

In order to run the application, you must execute the following command:
>poetry run python crypto_proj/crypto_flask.py

 This will cause the program to run locally on port 5000. The webpage is located in the following url:
>http://127.0.0.1:5000/webpage

You can visit the following link to get the json representation of the best and worst locations to purchase a given coin:
>http://127.0.0.1:5000/coin_info

 Questionnaire
 -----------
 1. One optimization is allowing the system to fail gracefully. This means allowing coins found at one exchange
 location to be obtainable, despite not being found in the other exchange place. Another optimization would lie in how I store data in the logic layer. I believe I could have dealt with any issue of memory usage by creating a database as opposed to making a dictionary of coins again and again, thus increasing speed as well.
 A final optimization to the program would having the HTML buttons on the front end take you to the website that has the best deal as opposed to linking to the website whose coin information is displayed above them.


 2. I would say that some portions of over designing this application was allowing for scalability. As I was working on this project I found myself working in waves. The first wave was a very basic thought process of obtaining the desired coin information and showing this. Once I had this done, I thought of ways that would improve the ease of adding other coins. My program allows for easy incorporation of other coins from these exchange companies as well as integrating other companies. The only new information required is that you input the correct symbol to represent a coin and a key to refer to that symbol (the name of the coin). This also ties into how I structured return values, as a dictionary to make accessing values easier as oppose to some other datatype.
 Another over-designed aspect of this application is the front end. I may have taken the easy route of creating a webpage that delivers the desired information, but I believe a more eye catching view would make for a better user experience.


 3. If I had to scale my solution to 100 users/second traffic, I would create a cache of recently searched for coins. Once this data was stored I could simply update it X times every 5 seconds, and use the information stored in the database to increase response time. In other words, this would result in less calls to the exchange companies API, resulting in quicker results.

 4. One enhancement I would make would be to allow realtime information from each exchange to be depicted on the webpage.  
