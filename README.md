# SA Economy Tracker

A small data pipeline that pulls South African economic indicators from the World Bank API, cleans them, stores them in a database, and shows them through an API and a dashboard. It also compares South Africa with peer countries such as Nigeria, Kenya and Brazil.

**Status:** in progress. The extract step is being built first.

## What it does

1. **Extract:** fetches indicators (GDP growth, inflation, unemployment) from the World Bank API and caches the raw JSON in `data/raw/`.
2. **Transform:** cleans the data with pandas, handles missing years, and adds year-on-year change, a rolling average and a flag for unusual jumps (z-score).
3. **Load:** writes the cleaned data to SQLite using SQLAlchemy. Re-running the load does not create duplicate rows.
4. **Serve:** a FastAPI service returns the data as JSON.
5. **Show:** a Streamlit dashboard lets you pick a country and an indicator and see the chart.

```
World Bank API -> extract -> transform -> load -> SQLite
                                                    |
                                      FastAPI <-----+-----> Streamlit
```

## Project structure

```
sa-economy-tracker/
├── etl/          # extract.py, transform.py, load.py
├── api/          # main.py (FastAPI)
├── dashboard/    # app.py (Streamlit)
├── data/raw/     # cached API responses
├── tests/        # pytest tests
└── README.md
```

## Data source

[World Bank Indicators API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation). No API key is needed.

| Indicator | Code |
|---|---|
| GDP growth (annual %) | `NY.GDP.MKTP.KD.ZG` |
| Inflation, consumer prices (annual %) | `FP.CPI.TOTL.ZG` |
| Unemployment (% of labour force) | `SL.UEM.TOTL.ZS` |

## Roadmap

- [ ] Extract one indicator for one country
- [ ] Extract several countries and indicators, with pagination and error handling
- [ ] Transform: missing values, year-on-year change, rolling average, anomaly flag
- [ ] Load into SQLite without duplicates
- [ ] FastAPI endpoints (`/indicators/{country}/{indicator}`, `/compare`)
- [ ] Streamlit dashboard
- [ ] Tests for the transform functions
- [ ] Dockerfile
- [ ] Scheduled weekly data refresh (GitHub Actions)
- [ ] Short write-up of findings

## Author

Karabo Moreti ([GitHub](https://github.com/thatomoreti), [LinkedIn](https://linkedin.com/in/karabo-moreti))
