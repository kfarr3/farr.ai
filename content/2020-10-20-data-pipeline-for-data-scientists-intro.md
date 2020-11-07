Title: Data Pipeline for Data Scientists - Introduction
Date: 2020-10-20
Category: Blog
Tags: DataScience; Development;
Slug: data-pipeline-for-data-scientists-intro
Status: draft

To each person, a Data Scientist has a different set of skills.  I see them as the glue between *data* and *business value*, connected through statistics, machine learning, etc.  The amount of data plumbing and application work required for a Machine Learning model to drive business value is enormous.  A single Data Scientist can easily keep 10 or more skilled Software Engineers busy building out data ingestion at scale, getting the data into a facility for analysis, deploying models, measuring deployed models, retraining, etc.

Where the work of a Data Scientist stops and the Software Engineers begins is fuzzy, and dependent on the company.  For some companies, the Data Scientist lives only in Jupyter or R, building models that Machine Learning Engineers will port and deploy.  Others may develop their models directly in a production language and environment, and may take part of the deployment.  It is my assertion, that the field of Data Science, immature and fledging, is similar to Software Development in the 1990s.  The large companies are doing many things right and set the stage for what many think Data Science should be, however smaller companies can still derive value from properly built models, even if they cannot support the hypothesised 10-1 ratio of Software Engineers to Data Scientists.  This area, where a generalist can provide enormous value to a company by wearing many hats.  Similar to how even the most non-tech companies have a Software Engineering department, so to will they eventually have a Data Analyst/Business Analyst/Data Science department.

A Data Scientist that cannot pull their own data, cannot process JSON, etc, is at the whim of the Software Engineers backlog.  Which, when prioritized by business need by a functioning Product Owner, has a hard time showing a need for data that a Data Scientist has yet to analyze.  There are dozens of articles on data pulling techniques, no need to belabor that here.  What I do want to do is present a framework for empowering Data Scientists to push their code as close to production as possible.  This reduces the time for Software Engineers, but it also lets the Data Scientist gain the ability to assist when things stop working, and they will.  A Data Scientist creating models for production had better have skin in the game and appreciate what happens when a model stops working, produces damaging results, or any other number of Operations level issues.

This series will walk through a possible deployment pattern, aimed at Data Scientists integrating with a modern Software Development stack.  I will skip over some table-stakes discussions like Infrastructure as Code and Network Security, as each team will be different, add a lot of complexity that is not needed, and are typically one time setup.

* Part 1 - Extract, Load, Transform
* Part 2 - Notebook to Production Feature Engineering
* Part 3 - Model Training
* Part 4 - Model Deployment