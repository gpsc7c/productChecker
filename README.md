# Author(s): "Gregory Shelton"
# Project  : Online Storefront Deal Checker
# Version  : 0.0.0001
# Updated  : 12/27/2025
# Purpose  : 
             Simple 20-40 hour program for boot.dev, built to be a program
             that can be set to automatically run on computer startup, read
             from a text file of urls or products, Identify which is
             which, identify whether the item in question is in stock, and
             identify whether the price has changed, then provide an alert
             if the price has gone down and the product is in stock, 
             and write a log on the status of all items and whether or not
             they have changed. intended to work with amazon, ebay, etc.
             preferrably has search functionality and a simple window with
             a text field that can add urls or products to the text file and
             organize said items. should have a natural limit to prevent on-
             startup lag, and close, outputting a partial log after x amount
             of seconds, alerting the user to the problem. should also alert
             the user if a page is inaccessible or down.
# How to Run:
             No current executable, intended to be runnable via python and
             via executable.
# How to Clone:
             clone via Git from https://github.com/gpsc7c/productChecker
