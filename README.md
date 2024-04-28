## Web Scraping and Data Analysis of Real Estate Listings in Oregon
![image](https://github.com/eKeiran/WebScraping/assets/34791715/5b88d667-78bb-46e3-bf21-a28d8dff376f)

### Overview
This project involved scraping real estate listings from Realtor.com for properties located in Oregon. 
Using Selenium and Beautiful Soup, I extracted new listings, including information such as address, zip code, bathrooms, bedrooms, price, and more.
The scraped data was then saved into CSV files for further analysis.

### File Structure
├── folium_oregon.html
├── preprocessed_scraped_oregon.csv
├── Realtor_Analysis_Oregon.ipynb
├── realtor-analysis-oregon.pdf
├── scraped_data_oregon.csv
├── WebScraping_Realtor_Oregon.ipynb
└── webscraping-realtor-oregon.pdf


### Tools Used
- Python
- Selenium
- Beautiful Soup
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Process
1. **Web Scraping**: Used Selenium to automate browsing and navigation on Realtor.com, simulating human interaction to access the listings.
2. **Data Extraction**: Utilized Beautiful Soup to parse the HTML content of the listings and extract relevant information, including address, zip code, bathrooms, bedrooms, price, etc.
3. **Data Storage**: Saved the extracted data into CSV files (`scraped_data_oregon.csv` and `preprocessed_scraped_oregon.csv`) for easy access and further analysis.
4. **Data Analysis**: Performed various data analysis tasks using Pandas and NumPy, including descriptive statistics, data cleaning, and aggregation. The analysis notebooks are `WebScraping_Realtor_Oregon.ipynb` and `Realtor_Analysis_Oregon.ipynb`.
5. **Visualization**: Visualized the data using Matplotlib and Seaborn to gain insights into the real estate market trends, pricing distribution, and other patterns.

### How to Use
1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the web scraping script (`WebScraping_Realtor_Oregon.ipynb`) to fetch real estate listings from Realtor.com and save the scraped data into `scraped_data_oregon.csv`.
4. Run the data analysis notebook (`Realtor_Analysis_Oregon.ipynb`) to perform analysis and generate visualizations using the scraped data.
5. Explore the generated CSV files and notebooks for further insights.

