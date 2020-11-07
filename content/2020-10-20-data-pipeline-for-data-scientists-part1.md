Title: Data Pipeline for Data Scientists - Part 1 - ETL
Date: 2020-10-20
Category: Blog
Tags: DataScience; Development;
Slug: data-pipeline-for-data-scientists-part1
Status: draft

The goal of any ETL process is to get data from some source and place it somewhere you can perform analysis on it, in some usable way.  Modern pipeline architectures are doing more ELT: Extract, Load, Transform, which is what I will be demonstrating.

The GET application will perform the raw PULL of data and Load it into our data-lake.  Next the PROCESS application will take that data and convert it into something usable.  My example process will be downloading all 13F filings from the SEC's Edgar portal and converting the raw files into a processed CSV.