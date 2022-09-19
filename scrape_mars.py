from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    # Visit https://redplanetscience.com/
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    # Get the News Title
    news_title = soup.find('div', class_='content_title').text

    # Get the title intro
    news_intro = soup.find('div', class_='article_teaser_body').text

    # Visit https://spaceimages-mars.com/
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Find the featured image
    featured_image = soup.find('img', class_='headerimage')

    # Save the url to the image
    featured_image_url = url + featured_image['src']

    # Move on to the next website
    url = 'https://galaxyfacts-mars.com/'

    # Read in the tables from the site
    tables = pd.read_html(url)
    
    # Save the desired table
    mars_facts = tables[0]

    # Set the column names correctly
    mars_facts.columns = mars_facts.iloc[0]

    # Drops the row used as the columns
    mars_facts.drop(mars_facts.index[0], inplace=True)

    # Remove column name that isn't needed
    mars_facts.rename(columns={ 'Mars - Earth Comparison' : '' }, inplace=True)

    # Save the table to html without index so it looks nicer
    mars_facts_html = mars_facts.to_html(index=False)

    # Next website
    url = 'https://marshemispheres.com/'

    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # variables list for getting links and titles
    product_list = []
    url_list = []
    product_title = []
    product_url_list = []
    hemisphere_image_urls = []

    # get each hemisphere page available
    product_items = soup.find_all('div', class_='description')

    # loop to get each hemisphere page available
    for product in product_items:
        title = product.find('h3').text
        product_title.append(title)
        product_url = product.find('a')['href']
        url_list.append(product_url)

    product_url_list = [ url + p_url for p_url in url_list]

    # Ensure the material is still there
    try:
        for title in product_title:
            browser.links.find_by_partial_text(title).click()
            html = browser.html
            soup = bs(html, "html.parser")
            title = soup.find('h2', class_='title').text
            image = soup.find('div', id='wide-image').find_all('img')[1]['src']
        
            hemisphere_image_urls.append({ 'title' : title, 'img_url' : url + image})
            browser.links.find_by_partial_text('Back').click()
        
    except:
        print("Scraping Complete")
    
    # Store data in a dictionary
    mars_data_dict = {
        "featured_img": featured_image_url,
        "news_title": news_title,
        "news_intro": news_intro,
        "mars_facts" : mars_facts_html,
        "hemisphere_imgs" : hemisphere_image_urls
    }

    # Close the browser after scraping
    browser.quit()

    # return the results
    return mars_data_dict