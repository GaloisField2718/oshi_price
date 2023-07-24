# oshi_price
Fetch the last Oshi price from unisat.


## Installation 

```
git clone https://github.com/GaloisField2718/oshi_price.git && cd oshi_price
```

You need to have chrome installed on your computer. For [ubuntu server](https://askubuntu.com/questions/245041/how-do-i-install-chrome-on-a-server), [google_chrome [Wiki ubuntu-fr]](https://doc.ubuntu-fr.org/google_chrome) and for other OS you can download from [Official link](https://support.google.com/chrome/a/answer/9025903?hl=fr).

After this : 
```
pipenv shell
```

And 
```
pipenv install
```

If you need to install each packages it's : 
```
pipenv install selenium chromedriver-binary
```

## Run

```
python3 fetch_prices.py
```

## Integrations

This code can be integrated easily to many different code and usage.

One idea could be to integrate this in a telegram bot, ex : [GaloisField2718/SatoshiPriceBot](https://github.com/GaloisField2718/SatoshiPriceBot).


