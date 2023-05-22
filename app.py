import culturestreak
import logging
import random
import time
import sys

import nltk
nltk.download('gutenberg')
culturestreak.processing()
from nltk.corpus import gutenberg

unique_words = set(gutenberg.words())

console_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(message)s')
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)
logging.getLogger().setLevel(logging.INFO)

loop_duration = 3600
start_time = time.time()

while (time.time() - start_time) < loop_duration:
    random_paragraph = ' '.join(random.sample(list(unique_words), 50))
    logging.info(random_paragraph)
    time.sleep(1)

logging.info('Program telah selesai.')


