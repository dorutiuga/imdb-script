# IMDb Ratings Scraper

This Python script scrapes IMDb user ratings page to calculate the total runtime of movies listed on the page. It also excludes series with a runtime of more than 6 hours and calculates the total runtime for those separately.

## Prerequisites

- Python 3.x
- BeautifulSoup4 library
- Requests library

## Installation

1. Clone the repository or download the Python script (`runtime.py`) to your local machine.

2. Install the required Python libraries:

   ```bash
   pip install beautifulsoup4 requests
    ```

3. ## Usage
   
3.1. Open the file in a text editor and at line 5 `YOUR_IMDB_ID = "IMDB_ID"` change IMDB_ID with your current id that you can find in imdb if you navigate to ratings page and extract from url. 
3.2. Run the script by executing the following command in your terminal:

   ```bash
   python runtime.py
   ```
<img width="666" alt="Screenshot 2024-03-24 at 09 43 02" src="https://github.com/dorutiuga/imdb-script/assets/107680344/60632677-0260-40d6-9ac2-15b9603826ae">
