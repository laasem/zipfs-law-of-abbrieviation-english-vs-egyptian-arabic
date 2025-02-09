# Download pip and use it to install required packages
import pip
required_packages = ['datasets', 'spacy', 'spacy-transformers']
for package in required_packages:
  print(f'Installing package: {package}...')
  pip.main(['install', package])


# Download needed English model via python -m spacy command
import subprocess
subprocess.run(['python', '-m', 'spacy', 'download', 'en_core_web_sm'])

# Import required packages and functions
from datasets import load_dataset
import spacy

# Define a function to load dataset by language ISO code,
# returning the training split, which is the only one
def load_dataset_by_language(iso_code):
  return load_dataset(
          'wikimedia/wikipedia',
          f'20231101.{iso_code}',
          split='train'
          )

# Each dataset contains a 'text' column containing the content of the
# Wikipedia articles, which is what we're interested in.
# Here we define a function to tokenize the contents of that column
# using spacy
def tokenize(batch):
    nlp = spacy.load('en_core_web_sm')
    return nlp(batch['text'])

dataset_en = load_dataset_by_language('en')
dataset_en.set_transform(tokenize)


dataset_arz = load_dataset_by_language('arz')



