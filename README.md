# eBayWebscraping
**This code scrapes data from eBay and stores the results in a json and csv file.**

This is the GitHub repository for project_03 for the class Computing for the Web (CSCI040). The instructions and rubric for this project can be found [here](https://github.com/mikeizbicki/cmc-csci040/tree/2022fall/project_03).

The file `ebay-dl.py` is a python program that takes an input search term for eBay, and then generates either a `.json` or `.csv` file depending on what has been inputted into the command line. This project will output the following information about the eBay item:
<ol>
  <li>name: name of the item
  <li>price: stores as an integer; if the output is 5999, this means the actual price is 59.99
  <li>status: describes the condition of the item
  <li>shipping: price of the shipping
  <li>free_returns: boolean value for whether there are free returns or not
  <li>items_sold: number of items sold
</ol>

# How to use this program
To use this python program `ebay-dl`, type the following into the command line (also known as the terminal):
```
$ python3 ebay-dl.py 'name of the item (can contain spaces)'
```
Such as:
```
$ python3 ebay-dl.py 'soccer ball'
```

The program will then download the first 10 pages (by default) of the search term! Also, if your search contains multiple words, be sure to use quotation marks around them!

# How to download the data as a .csv file
By default, this program will download the data into a `.json` fole, but this can be changed. If you prefer a `.csv` fprmat, just type the following code into the command line - note the `--csv=True` added to the end of the previous command: 
```
$ python3 ebay-dl.py 'name of the item (can contain spaces)' --csv=True
```
Such as:
```
$ python3 ebay-dl.py 'soccer ball' --csv=True
```

# How to modify the number of pages scraped
Finally, if you want to modify the number of pages scraped, type in the following command into the command line (by adding `--num_pages`):
```
$ python3 ebay-dl.py 'soccer ball' --num_pages=(enter integer here)
```
Such as:
```
$ python3 ebay-dl.py 'soccer ball' --num_pages=3
```
