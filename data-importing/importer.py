# Import Necessary Packages
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import gzip
import shutil


# Get to the data

url = "https://webrobots.io/kickstarter-datasets/"

# Open the URL
response = requests.get(url)

# Load the data
if response.status_code == 200:
    # Parse the HTML
    soup = BeautifulSoup(response.content, "html.parser")

    #Find all the links to JSON files
    json_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None and (href.endswith('.json') or href.endswith('.json.gz')):
            json_links.append(href)
    # Check how many JSON files we found
    print(f"Found {len(json_links)} JSON files to download")

    ## Download each json file
    for json_url in json_links:
        # Get the JSON file
        json_response = requests.get(json_url)
        print(json_response.status_code)
        if json_response.status_code == 200:
            # Save the JSON file
            print(f"Downloading {json_url}")
            filename = os.path.join(r'C:\Users\d0tam\kickstarter-JMP\data', json_url.split("/")[-1])

            #Write the content to a .gz file if it's gzipped
            with open(filename, "wb") as f:
                f.write(json_response.content)

            print(f"Downloaded {filename}")

            # If the file is a .gz file, unzip it
            if filename.endswith(".gz"):
                with open(filename[:-3], 'wb') as out_file:
                    with gzip.open(filename, 'rb') as in_file:
                        shutil.copyfileobj(in_file, out_file)
                print(f"Decompressed {filename[::-3]}")

                #Optionally, remove the .gz file
                os.remove(filename)
            
        else:
            print(f"Failed to download {json_url}")

else:
    print(f"Failed to open {url}")


