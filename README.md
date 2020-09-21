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
scrapy crawl booking -a city="chicago" -a date="09/22/2020" -o 09_22_2020_chicago.csv
```

Params:
- city: City name
- date: Checkin date (Price and Disponible Rooms depend on the checkin date)