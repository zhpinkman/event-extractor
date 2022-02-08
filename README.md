# event-extractor
This repository is a python package that is able to extract events in a given time. 


```python
>>> from event_extractor import Event_extractor

>>> Event_extractor.get_special_events(year=2021, month="february", term='Historic Event')

[
  'Feb 2 Jeff Bezos announces he is stepping down as CEO of Amazon after 30 years, becoming executive chairman',
  'Feb 3 US President Joe Biden signs executive orders to reunite immigrant families, setting up a new taskforce to address around 1000 remaining separated families', 
  'Feb 9 US Senate Impeachment trial of former President Donald Trump begins in Washington D.C.', 
  'Feb 13 Mario Draghi, former head of the European Central Bank, is sworn in as Italian Prime Minister ahead of a new coalition government', 
  'Feb 21 India\'s BJP party issues resolution country had "defeated COVID under the able, sensitive, committed and visionary leadership of Prime Minister Narendra Modi”, massive second wave hits two months later', 
  'Feb 22 Wife of drug cartel boss "El Chapo" Emma Coronel Aispuro arrested in the US on drug trafficking charges and conspiring to free her husband from prison',
  'Feb 25 Chinese President Xi Jinping claims the country has eradicated extreme poverty (earning less than US$620 a year), though many observers remain skeptical about the accuracy of Chinese data due to widespread corruption and lack of transparency'
]

```
