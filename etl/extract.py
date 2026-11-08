#Extract.py is meant to extract data from the world bank api.           
           
def build_url(countries, indicator , start_year, end_year, per_page, page):
    base_url = "https://api.worldbank.org/v2"
    country_text =  ";".join(countries)
    date_range = f"{start_year}:{end_year}"
    return base_url + "/country/" + country_text+ "/indicator/" + indicator+ "?format=json&per_page=" + per_page+ "&date=" + date_range + "&page=" + page

country_list = ["ZA","NG","BRA"]
url = build_url(country_list,"FP.CPI.TOTL.ZG","2000","2025","1000","1")

print(url)