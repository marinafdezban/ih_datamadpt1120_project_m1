# Data Project 1

## :chart_with_downwards_trend: How is the world of data distributed across the European Union?

**Interested in the world of data? Do you dream of becoming a data expert?**

Here you can find a study on how data professions are distributed across the European Union with socio-demographic information, which can be very helpful if you really want to introduce yourself into this new field of knowledge. 

![Image](https://www.masterbigdataonline.com/images/big_data_matrix.jpg)

> Blockquote


## :woman_technologist: How can I get this information?

Very easy! First, you need to know which information are you looking for... Do you want to know how data jobs are distributed across all European countries, or just about one specific country?

``` 

**EU countries** :arrow_right: python main.py -p /data/raw_data_project_m1.db

```

``` 

**A specific country** :arrow_right: python main.py -p /data/raw_data_project_m1.db -c {write the country to want to get info from}

```

## :bar_chart: What information this study will provide you?

Country | Job Title | Rural | Quantity | Percentage

--- | --- | ---

Spain | Data Architect | Urban | 2 | 0.14%

France | Data Officer| Rural | 5 | 2.06%

Great Britain | Data Coordinator | Urban | 9 | 4%

... | ... | ... | ... | ...


**:round_pushpin: Data Sources**

* **Tables (.db)** with data from a survey. You will find the information in The data folder.
* **API** with information regarding data jobs. This API is from [Open Skills Project](http://dataatwork.org/data/).
* **Web Scraping** countries information from [Eurostat website](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes).


## :open_file_folder: Folder Structure

``` 
└── ih_datamadpt1120_project_m1
    ├── __trash__
    ├── .gitignore
    ├── requirements.txt
    ├── README.md
    ├── main.py
    ├── notebooks
    │   └── final.ipynb
    ├── p_acquisition
    │   ├── __init__.py
    │   └── m_acquisition.py
    ├── p_wrangling
    │   ├── __init__.py
    │   └── m_wrangling.py
    ├── p_analysis
    │   ├── __init__.py
    │   └── m_analysis.py
    ├── p_reporting
    │   ├── __init__.py
    │   └── m_reporting.py
    ├── results
    │	├── {country}results.csv
    │	└── all countries results.csv
    └── data
        └── raw_data_project_m1.db

```

## :mailbox: Contact info

For questions, suggestions and other inquiries... here is my email address [marina.fernandez@gmail.com](m.fernandezban@gmail.com)





