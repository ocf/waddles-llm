import pickle
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from langchain.document_loaders import WebBaseLoader


def get_all_links(url):
    try:
        # Send an HTTP request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract all links from the page
            links = set()  # Using a set to avoid duplicates
            for a_tag in soup.find_all("a", href=True):
                link = a_tag["href"]

                # Make the URL absolute (resolve relative URLs)
                absolute_link = urljoin(url, link)

                # Remove fragments and query parameters
                absolute_link = (
                    urlparse(absolute_link)._replace(query="", fragment="").geturl()
                )

                # Add the absolute URL to the set
                links.add(absolute_link)

            return links
        else:
            # Print an error message if the request was not successful
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def crawl_website(base_url):
    # Construct the pickle file path
    pickle_file_path = os.path.join(os.getcwd(),"sources/websites/", "linkmap.pickle")
    # Check if the pickle file exists
    try:
        with open(pickle_file_path, "rb") as file:
            links = pickle.load(file)
            # take the first ten elements of the linkmap
            links = links[:10]
            return WebBaseLoader(web_paths=links).load()

    except FileNotFoundError:
        # If the pickle file doesn't exist, generate links and save to the pickle file
        links = [base_url]
        all_links = get_all_links(base_url)

        if all_links:
            for link in all_links:
                links.append(link)

            # Crawl each subpage recursively
            for subpage_url in all_links:
                subpage_links = get_all_links(subpage_url)
                if subpage_links:
                    links.extend(subpage_links)


        # If the element doesn't start with "httos://www.ocf.berkeley.edu" or "http://ocf.io", or "https://github.com/ocf/" remove it
        links = [
            link
            for link in links
            if link.startswith("https://www.ocf.berkeley.edu")
            or link.startswith("http://ocf.io")
            or link.startswith("https://github.com/ocf/")
        ]
        # Save the links to a pickle file
        with open(pickle_file_path, "wb") as file:
            pickle.dump(links, file)

        return WebBaseLoader(web_paths=links).load()
