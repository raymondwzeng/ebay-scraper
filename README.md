# EBay Scraper
This was a personal project of mine back in early 2021, near the height of the GPU crisis, as a way to see if I could find good deals on GPUs at the time.
This WILL NOT work as-is by design - I have chosen to alter the code slightly as to prevent this to be used by others (though as prices come down, I doubt many will try to use this either way).

## What it did/features
The program was able to scrape listings from Ebay's website from user input. It would find items that fit the criteria (with some bonuses like free shipping), and get their average prices.
After getting the average prices, it would export 2 csv files: one with the "raw" data, and another with links to potentially good deals to bid on.

There were also some nice additional features, such as the program getting *most* permutations of GPUs (e.g. Asus GTX1060 3GB, 4GB, etc.).

## Libraries Used
- Requests (actually sending the proper requests to EBay servers)
- BeautifulSoup (parsing the data)
- csvprocess (exporting all of the data to a .csv file)

**Note: By using (or attempting to use) this program, you acknowlege that you accept all responsibilies and potential consequences that may occur. Scraping the website in such a manner is generally frowned upon, and you may end up receiving an unpleasant message from Ebay. Crawl at your own risk.**