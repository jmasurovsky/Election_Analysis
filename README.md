# Election_Analysis

## Overview of Election Audit

The purpose of this project is to assist the Colorado Board of Elections in ensuring that votes were counted accurately by completing an election audit of recent election results of a Unites States congressional precinct. Additional tasks were requested in order to complete the election audit, such as:

- The voter turnout for each county

- The percentage of votes from each county out of the total count

- The county with the highest turnout

The Colorado Board of Elections also requested for the process to be automated, therefore using Python was essential. 

## Resources

Data source: election_results.csv

Software: Python 3.7.6, Visual Studio Code 1.47.1

## Election-Audit Results

The analysis of the election show that for this congressional distrcit: 

- There were 369,711 total votes cast in the election.

* The counties were:

  * Jefferson
  
  * Denver
  
  * Arapahoe

* The county results were:

  * Jefferson received 10.5% of the vote and 38,855 number of votes.
 
  * Denver received 82.8% of the vote and 306,055 number of votes.

  * Arapahoe received 6.7% of the vote and 24,801 number of votes.
 
- Denver had the largest voter turnout by county.

* The candidates were:

  * Charles Casper Stockham
 
  * Diana DeGette
 
  * Raymon Anthony Doane

* The candidate results were:

  * Charles Casper Stockham received 23% of the vote and 85,213 number of votes.
 
  * Diana DeGette received 73.8% of the vote and 272,892 number of votes.
 
  * Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
 
* The winner of the election was:

  * Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
  


## Election-Audit Summary

The Python script PyPoll_Challenge.py can be used to automate an election audit to perform an analysis of voting results by candidate and county. The script could be modified to be used for Senate elections by extracting voting count by senatorial districts, and used for local election voting data to determine neighborhood voting counts. For example, to determine neighborhood count for a local election audit, the county list and dictionary would have to be modified to capture neighborhoods. Similar steps that were made to capture county data are similar to capture neighborhood data when making for loops and conditionals.

