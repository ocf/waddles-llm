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
    # Get all links from the homepage
    links = [base_url]
    # all_links = get_all_links(base_url)

    # if all_links:
    #     print("All links on the homepage:")
    #     for link in all_links:
    #         links.append(link)

    #     # Crawl each subpage recursively
    #     for subpage_url in all_links:
    #         subpage_links = get_all_links(subpage_url)
    #         if subpage_links:
    #             for link in subpage_links:
    #                 links.append(link)
    # print(links)
    return WebBaseLoader(web_paths=links).load()
