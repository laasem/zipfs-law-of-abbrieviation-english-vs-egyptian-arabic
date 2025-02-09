# Testing Zipf’s Law of Abbreviation on English and Egyptian Arabic

Python script to test Zipf's Law of Abbreviation on English and Egyptian Arabic Wikipedia corpora.

## To run
Assuming python3 is installed via command `python3`, navigate to current directory and run:

```
source .env/bin/activate
python3 script.py
```

to run script in a virtual environment. Please note that the script loads large datasets into memory and so takes some time to complete.

When done, run `source .env/bin/deactivate` to deactivate virtual environment.

## Credits
Wikipedia dataset used available [here](https://huggingface.co/datasets/wikimedia/wikipedia).

Developed as part of the NLP course of the Universitat Pompeu Fabra's Master in Theoretical and Applied Linguistics taught by Professor Thomas Brochhagen.
