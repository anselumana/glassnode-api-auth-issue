# Glassnode API Auth Issue
Project for the testing and description of Glassnode API Auth Issue.

## Issue description
I am using a free account to access data from both Glassnode web UI and Glassnode public API.
The issue is that while the web UI blocks the visualization of any T3 metric, the public API has some T3 metrics available.
I initially discovered this issue using my personal account (anselumana@gmail.com), but I also tested it against a new account and multiple api keys, and still got the same results.
Following is the list of the exploited T3 endpoints:
* /v1/metrics/indicators/nupl_less_155
* /v1/metrics/indicators/nupl_more_155
* /v1/metrics/supply/sth_lth_realized_value_ratio
* /v1/metrics/supply/sth_profit_loss_ratio

## How to replicate the issue
Follow these steps:
* Clone this repo
* Install the dependencies via `py install -r requirements.txt`
* Create a `.env` file with the following key-value pair: `api_key=<YOUR_API_KEY>`
* Run the script with `py main.py`
This will try to fetch data from all T3 endpoints and save it to `./data/data.json`.
