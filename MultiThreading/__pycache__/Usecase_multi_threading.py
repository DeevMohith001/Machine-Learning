'''
Real-World Examples: Multithreading for I/O-bound Tasks
Scenario: web scraping
web scraping  often involves making numerous network requests to
fetch web pages. These tasks are I/O bound because they spend a lot of
time waiting for responses from servers. Mutithreading can significantly
improve the performance by allowing multiple web pages to be fetched concurrently.

'''