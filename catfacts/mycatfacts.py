#!/usr/bin/env python3
"""Author: Michael
 this module returns cat facts for the cat-fact API
"""
import random
import requests

def main():
    """main method that plays with the cat info """
    raw_data = requests.get("https://cat-fact.herokuapp.com/facts")
    cat_facts = raw_data.json()

    # for fact in cat_facts["all"]:
    #    print(fact["text"])
    print(dir(raw_data))
    cat_fact = random.choice(cat_facts['all'])
    print(cat_fact['text'])
    print(raw_data.raw.read(10))
    print(raw_data.status_code)
    print(raw_data.history)


if __name__ == "__main__":
    main()
