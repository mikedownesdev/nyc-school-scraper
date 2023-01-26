## Prerequisite Installation

- [PyQuery](https://pyquery.readthedocs.io/en/latest/)
- [Python 3](https://www.python.org/downloads/) (Python 2.X may work)

## Brief

I needed to compile a list of NYC Schools and School Principals with their contact information. Luckily, The New York City Department of Education has a decent system for querying its member schools:
https://schoolsearch.schools.nyc/

Upon querying for a few schools, I was able to determine that all of the NYC Schools have their own url at https://www.schools.nyc.gov/schools/{School-Number}, where the school number is the combination of a letter (representing the borough) and a number. These school profile pages contain a standard HTML layout for useful pieces of information about the school.

## About This Project

This simple Python-powered web scraper will loop, starting 0 and continuing until an upper bound number is reached, for each borough code, using it in the URL template from above and attempting to pull the specific pieces of data that we are scraping for. 

### Example
The Bronx (X): 
https://www.schools.nyc.gov/schools/X001
https://www.schools.nyc.gov/schools/X002 -- Not a school
https://www.schools.nyc.gov/schools/X003
https://www.schools.nyc.gov/schools/X004
...
https://www.schools.nyc.gov/schools/X400


