# Mars-News-Now

### by:
* Arnold Schultz

# Overview:
A web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.  The data is collected from a scrape function in scrape_mars.py that gets called in the flask server.

## Websites for gathering data:

* Web Site for the latest news:
    * Link: https://redplanetscience.com/
    * Description: Gets the name of the featured article as well as the summary text and puts it at the top of the page

* Featured Image
	* Link: https://spaceimages-mars.com/
    * Description: Get the link to the featured image from the website
	
* Mars Data
	* Link:  https://galaxyfacts-mars.com/
    * Description: Calls a pandas function to gather tables from the html of the website, picks the desired table, converts to a dataframe, stylizes and returns back html.

* Mars Hemispheres
	* Link:  https://marshemispheres.com/
    * Description: Gets an image from each of the pages related the hemispheres of Mars.

### Requirements:

The flask server and the scrape program are written in python and run in an environment that has ``pandas``, ``splinter``,    
``bs4``,``webdriver_manager.chrome``, ``time``, ``flask``, ``flask_pymongo`` and using ``python 3.8``.

The HTML was wrtiien using bootstrap 5
