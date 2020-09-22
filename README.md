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
scrapy crawl booking -a city="chicago" -a start_date="2020/09/25" -a end_date="2020/10/25" -a gap=5 -o 2020_09_25_chicago.csv
```

Params:
- city: city name
- start_date: start day scrapy
- end_date: end day scrapy 
- gap: Gap day between scrapy (if 1, scrapy day by day between start_date and end_date)
  
Each scrapy day (depend on the start, end and gap), checkin-date will be different for collect prices and disponible rooms for this day.

## Output

This command export all hotels information to csv file. 

```
{'expedia_id': '1646995',
 'hotel_type': 'Hotel',
 'lat': 41.88803583,
 'lng': -87.62503662,
 'name': 'LondonHouse Chicago, Curio Collection by Hilton',
 'number_of_reviews': 889,
 'number_of_rooms': 64,
 'price': 260.09375,
 'price_un': 'US$',
 'review_score': 9.0,
 'star_rating': 4,
 'uri': 'https://www.booking.com//hotel/us/londonhouse-chicago-curio-collection-by-hilton.en-gb.html?label=gen173nr-1FCAEoggI46AdICVgEaCCIAQGYAQm4ARfIAQzYAQHoAQH4AQKIAgGoAgO4Aqb4o_sFwAIB0gIkODZjZGYzM2ItMzdkNC00NzUxLTgxNWItNDA3Mzg1NTI3YWJj2AIF4AIB&sid=0cd08e9b5c917c4c417a633b7c95b8e8&all_sr_blocks=164699509_107178679_2_0_0&checkin=2020-09-22&checkout=2020-09-23&dest_id=20033173&dest_type=city&group_adults=1&group_children=0&hapos=5&highlighted_blocks=164699509_107178679_2_0_0&hpos=5&no_rooms=1&req_adults=1&req_children=0&room1=A&sr_order=popularity&sr_pri_blocks=164699509_107178679_2_0_0__15900&srepoch=1600715817&srpvid=74b38794cd21000e&ucfs=1&from=searchresults;highlight_room='}
```