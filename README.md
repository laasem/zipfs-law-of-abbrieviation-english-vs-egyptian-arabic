# Testing Zipf’s Law of Abbreviation on English and Egyptian Arabic

Python script to test Zipf's Law of Abbreviation on English and Egyptian Arabic Wikipedia corpora.

## Dependencies
Before running, the following dependencies need to be satisfied:

- python3 needs to be installed on the environment you will run the script in (local, cloud, etc.) via command `python3`.
- The Wikipedia dataset [here](https://huggingface.co/datasets/wikimedia/wikipedia) needs to be accessible and downloadable via HuggingFace, specifically the `20231101.en` and `20231101.arz` files.

## Run
Assuming python3 is installed via command `python3`, navigate to current directory and run:

```
source .env/bin/activate
python3 script.py
```

to run script in a virtual environment. Please note that the script loads large datasets into memory and takes some time to complete - running on a cloud environment like Google Colab with GPU runtime would be helpful.

When done, run `source .env/bin/deactivate` to deactivate virtual environment.

## Credits
Developed as part of the NLP course of the Universitat Pompeu Fabra's Master in Theoretical and Applied Linguistics taught by Professor Thomas Brochhagen.
