# Scrapy Booking.com


## JOB

Input Start time / Scheduling When to start the spider automatically for a given city in the world with a given date range for a given date gap

City name Name of the city scanned for example: Miami Beach or Paris

Date range Start date Start date of the scan:
Date range End date End date of the scan

Date Gap Number of days gap How many days gap for each date scanned

For example: Scan from today to the end of the month with a date gap of one day.
Or Scan the entire year from today to the end of the year for a 2 day stay or a two day gap
Output

Each Hotel/apartment/vacation rentals Names
Each Hotel/apartment/vacation rentals expedia ID
Each Hotel/apartment/vacation rentals GPS coordinates
Each Hotel/apartment/vacation rentals prices Classified from min to max all of the price per each hotel for each day
Each Hotel/apartment/vacation rentals Star rating (if available)
Each Hotel/apartment/vacation rentals Review score
Each Hotel/apartment/vacation rentals Number of reviews
Each Hotel/apartment/vacation rentals number of rooms

## Usage

Install scrapy:

```
pip install scrapy
```

Run Job:

```
cd booking
scrapy crawl booking \
  -a city="chicago" \
  -a start_date="2020/09/25" \
  -a end_date="2020/10/25" \
  -a gap=5 \
  -o 2020_09_25_chicago.csv
```

Params:
- **city**: city name
- **start_date**: start day scrapy
- **end_date**: end day scrapy 
- **gap**: Gap day between scrapy (if 1, scrapy day by day between start_date and end_date)
  
Each scrapy day (depend on the start, end and gap), checkin-date will be different for collect prices and disponible rooms for this day.

## Output

This command export all hotels information to csv file. 

```
{'booking_id': '359287',
 'checkin_date': '2020/10/26',
 'end_date': '2020/10/30',
 'hotel_type': 'Hotel',
 'lat': 34.08367223,
 'lng': -118.36280733,
 'name': 'Palihotel Melrose',
 'number_of_reviews': 216,
 'number_of_rooms': 24,
 'price': 159.0,
 'price_un': 'US$',
 'review_score': 8.3,
 'scrapy_date': '2020/09/22 11:42:51',
 'star_rating': 3,
 'start_date': '2020/10/01',
 'uri': 'https://www.booking.com/hotel/us/palihotel-melrose.en-gb.html?label=gen173nr-1FCAEoggI46AdICVgEaCCIAQGYAQm4ARfIAQzYAQHoAQH4AQKIAgGoAgO4Ap6aqPsFwAIB0gIkZjM3MmFhOWItNjA3NC00NmM1LTk5YzctYzY5NzQ5ZTVlOGYy2AIF4AIB&sid=61033abc508df16ac8f4c2bf8dc24dc3&all_sr_blocks=35928701_265721760_2_0_0&checkin=2020-10-26&checkout=2020-10-27&dest_id=2279&dest_type=region&group_adults=1&group_children=0&hapos=319&highlighted_blocks=35928701_265721760_2_0_0&hpos=19&no_rooms=1&req_adults=1&req_children=0&room1=A&sr_order=popularity&sr_pri_blocks=35928701_265721760_2_0_0__12150&srepoch=1600785760&srpvid=6afe676f2990001c&ucfs=1&from=searchresults;highlight_room='}
```