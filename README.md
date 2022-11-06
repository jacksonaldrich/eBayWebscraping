# eBayWebscraping
**This code scrapes data from eBay and stores the results in a json and csv file.**

This is the GitHub repository for project_03 for the class Computing for the Web (CSCI040). The instructions and rubric for this project can be found [here](https://github.com/mikeizbicki/cmc-csci040/tree/2022fall/project_03).

The file `ebay-d.py` is a python program that takes an input search term for eBay, and then generates either a `.json` or `.csv` file depending on what has been inputted into the command line. This project will output the following information about the eBay item:
<ol>
  <li>name: name of the item
  <li>price: stores as an integer; if the output is 5999, this means the actual price is 59.99)
  <li>status: describes the condition of the item
  <li>shipping: price of the shipping
  <li>free_returns: boolean value for whether there are free returns or not
  <li>items_sold: number of items sold
</ol>

To use this python program (`ebay-dl`), type the following into the command line (also known as the terminal):
```
$ python3 ebay-dl.py '*name of the item (can contain spaces)*'
```

The program will then download the first 10 pages (by default) of the search term! Also, if your search contains multiple words, be sure to use quotation marks around them!

By default, this program will download the data into a `.json` fole, but this can be changed. If you prefer a `.csv` fprmat, just type the following code into the command line: 
```
$ python3 ebay-dl.py 'baseball hat' --csv
```
