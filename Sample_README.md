# Introduction

A SEC-10K filing provides comprehensive summary of a company’s financial performance. Several research publications have already established the high value of information contained in it.

This project aims to extract year on year sentiment change in the 10K report, from specific sections of the report, and analyze the stock price variation around the report publishing date.

## Functional Overview

Extracting insights from a SEC 10K report is widely researched and several publications have demonstrated that valuable information can be gleaned from these reports.   For e.g.
1. Analyze lawsuits, litigations of a company and predict its future performance.
2. Analyze historical reports and gain insights on the performance of the company.

The current POC experiment scope focused on extracting sentiments from specific sections of the 10K reports using NLP and testing a hypothesis whetehr the stock price variations around the report publish date were correlated with the sentiment score.
a. Management Discussion Section:	Has the most discretion and flexibility in terms of content. Content changes in this section can lead to significantly large and abnormal returns.
b. Risk Factors Section:	Changes in details in this section can lead to stock price correction at an average of 22% per year.
c. CXO’s reference:	Changes in language referring to the CEO/CFO’s can have a significant impact in the Stock price movements.
d. Litigation & Lawsuits:	Changes focused on Litigation & Lawsuits of a stock can have an impact on returns at an average of 8.5% per year.


## Solution Architecture

The workflow from ingestion of data to extracting insights is described in the picture below:

![](architechture/SEC10k_insights_architechture.PNG)

To run this project the scripts stored in the folder ‘scripts’ should be run in the following order:

1. stock_price_extraction.py
2. meta_data_extraction.py
3. html_text_extraction.py
4. section_extraction.py
5. legal_extraction.py
6. financial_info_extraction.py
7. word_dictionary_extraction.py
8. stockdata_extraction.py
9. sentiment_extraction.py
10. sentiment_stockdata_correlation.py
 
The SEC10k_insights_pipeline.py script runs the above files sequentially using the mlflow package.
To track the progress of the pipeline using mlflow ui, run the command 'mlflow ui' in Ananconda Prompt.
Next, open the tracking URL "http://localhost:5000" in your browser.

The above project can be run on a local system as well as on Azure. 
The ‘config_util.py’ file uploaded in the ‘scripts’ folder contains functions for local environment as well as azure. 
These functions are used in the main scripts. 
Thus the main scripts can be run either on a local system or in Azure.

## Choosing an environment 
To choose the environment, the 'sec10k_app_config.json' file must be edited. 
The first key-value pair of the configuration file decides whether the file should run in the local system or azure, this the value of the ‘method’ key can be edited to either ‘local’ or ‘azure’.

## To run the scripts on azure

1. Create a Storage Account with File Shares and Blob Storage
2. Update the details of the account in the sec10k_app_config.json file placed in the ‘config_files’ folder. 
3. Create directories in the File Share and update the paths in the ‘sec10k_app_config.json’ file
4. Edit ’method’ the config file to ‘azure’

When you choose to run the scripts using Azure, creation of your resources can be done through the 'creation_azure_resources.py' script. The names of your storage account, file shares, directories can be changed in the 'sec10k_app_config.json' fiile itself.
## To run script on your local system

1. Create paths on your local system for the output of each script.
2. Update these paths in the ‘sec10k_app_config.json’ file
3. Edit ‘method’ in the config file to ‘local’

There is only one input step in the meta_data_extraction.py script. All other scripts only generate outputs from the inputs of the previous step. 

Financial_info_extraction.py and word_dictionary_extraction.py are stand alone scripts and can be run in any order. 

## Insights Dashboard
The insights captured by these scripts are displayed as PowerBI dashboards. These dashboards are stored in the folder 'dashboards'. There are two dashboards, one is the outcome of running the scripts locally, while the other is the outcome of running the scripts on Azure.