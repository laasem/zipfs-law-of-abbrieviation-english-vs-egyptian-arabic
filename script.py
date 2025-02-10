# DOWNLOADS AND IMPORTS

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
import matplotlib.pyplot as plt
import seaborn as sns

# Configure plot style
%matplotlib inline
sns.set_style('whitegrid')
plt.rcParams.update({'font.size': 24})

#############

# FUNCTION DEFINITIONS

# Define a function to download dataset by language ISO code,
# returning a specified number of rows for performance reasons
# from the training split, which for these 2 languages is the only one,
# and converting the dataset to a Pandas dataframe
def load_dataframe(language_iso_code):
  dataset = load_dataset(
          'wikimedia/wikipedia',
          f'20231101.{language_iso_code}',
          split='train[:100]'
          )
  dataframe = dataset.to_pandas()
  return dataframe['text']

# Define a function that, given a text, a Spacy nlp model, and a dict,
# populates the dict with the unique token types present in the text
# and their frequency counts.
# To do so, the function first tokenizes and normalizes tokens
# using the provided model,
# ignoring case and stop words.
# Both tokenization and counting are done
# on the fly in the same loop to avoid memory issues
# given the size of the dataset
def count_type_to_freq(text, nlp, type_to_freq):
    doc = nlp_en(text)

    for token in doc:
      if token.is_punct: continue

      word = token.text.lower()
      if type_to_freq.get(word):
        type_to_freq[word] += 1
      else:
        type_to_freq[word] = 1

# Define a function to plot word lengths against log(frequency)
def plot(type_to_freq):
  x = [len(word_type) for word_type in type_to_freq.keys()]
  y = type_to_freq.values()

  plt.figure(figsize=(12, 8))
  plt.scatter(x, y, color='b', alpha=0.7)
  plt.yscale('log')
  plt.xlabel('word length')
  plt.ylabel('log(frequency)')
  plt.show()

#############

# SCRIPT LOGIC

# Get and plot data for English
df_en = load_dataframe('en')
nlp_en = spacy.load('en_core_web_sm')
type_to_freq_en = {}
df_en.apply(count_type_to_freq, args=(nlp_en, type_to_freq_en))
plot(type_to_freq_en)


# df_arz = load_dataframe('arz')
