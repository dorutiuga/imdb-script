import requests
from bs4 import BeautifulSoup
import time

def get_imdb_data(url):
    total_runtime_minutes = 0
    total_movies = 0
    total_series = 0
    
    while url:
        # Send a GET request to the IMDb ratings page
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all div elements with class "lister-item-content"
            movie_items = soup.find_all('div', class_='lister-item-content')
            
            # Count the number of movies on this page
            total_movies += len(movie_items)
            
            # Loop through each movie item
            for index, item in enumerate(movie_items, start=1):
                # Find the span element with class "runtime" containing the runtime of the movie
                runtime_span = item.find('span', class_='runtime')
                
                # Extract the runtime text
                if runtime_span:
                    runtime_text = runtime_span.get_text(strip=True)
                    
                    # Handle different formats of runtime text more robustly
                    runtime_values = runtime_text.split()
                    movie_runtime_minutes = 0
                    if len(runtime_values) == 2:
                        if runtime_values[1] == 'min':
                            movie_runtime_minutes = int(runtime_values[0])
                        elif runtime_values[1] in ['h', 'hr']:
                            movie_runtime_minutes = int(runtime_values[0]) * 60
                    elif len(runtime_values) == 4:
                        movie_runtime_minutes = int(runtime_values[0]) * 60 + int(runtime_values[2])
                    
                    # Check if the movie is a series (runtime more than 6 hours)
                    if movie_runtime_minutes > 6 * 60:
                        print(f"Total runtime for series {index}: {movie_runtime_minutes} minutes")
                        total_series += 1
                    else:
                        total_runtime_minutes += movie_runtime_minutes
                        print(f"Total runtime for movie {index}: {movie_runtime_minutes} minutes")
            
            # Find the "Next" button
            next_button = soup.find('a', class_='lister-page-next')
            
            # Check if there is a "Next" button
            if next_button:
                # Get the URL of the next page
                url = "https://www.imdb.com" + next_button['href']
            else:
                # If there is no "Next" button, exit the loop
                url = None
            
            # Wait for a short time before navigating to the next page
            time.sleep(1)
        else:
            # If the request was unsuccessful, print an error message
            print("Error: Failed to retrieve IMDb ratings. Status code:", response.status_code)
            return None, None
    
    return total_runtime_minutes, total_movies, total_series

# Function to convert minutes to days, hours, minutes, and seconds format
def convert_minutes_to_dd_hh_mm_ss(minutes):
    days = minutes // (60 * 24)
    hours = (minutes % (60 * 24)) // 60
    minutes %= 60
    seconds = minutes % 60
    return days, hours, minutes, seconds

# IMDb ratings page URL
url = "https://www.imdb.com/user/{{YOUR_IMDB_ID}}/checkins"

# Get the total sum of runtimes and number of movies listed on all pages of IMDb ratings
total_runtime, total_movies, total_series = get_imdb_data(url)

if total_runtime is not None and total_movies is not None:
    print("Total sum of runtimes from all movies (excluding series):", total_runtime, "minutes")
    print("Total number of movies listed:", total_movies)
    print("Total number of series listed:", total_series)
    
    # Convert total runtime to days, hours, minutes, and seconds
    days, hours, minutes, seconds = convert_minutes_to_dd_hh_mm_ss(total_runtime)
    print("Total runtime from all movies (excluding series) in days, hours, minutes, and seconds format:")
    print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
else:
    print("Error: Unable to retrieve IMDb data.")

