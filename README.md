# TechConf Registration Website

Live Site: https://huylequang210.azurewebsites.net

## Monthly Cost Analysis
Complete a month cost analysis of each Azure resource to give an estimate total cost using the table below:

| Azure Resource | Service Tier | Monthly Cost |
| ------------ | ------------ | ------------ |
| *Azure Postgres Database* | Flexible Server - Burstable, B1ms, 1 vCores, 2 GiB RAM, 32 GiB storage |  16.09 $ |
| *Azure Service Bus*   | Basic     | 0.5 $ |
| *Azure Web App*  | Free (F1) | - $   |
| *Azure Function App* | Consumpsion (Serverless) - Free | - $ |
| TOTAL | | 16.59 $|

## Architecture Explanation
- Service Bus makes notifications task runs faster because it provides a background tasks to execute resource-intensive, time-consuming tasks. Now the web app is more responsive, and free up to take others incoming requests.
- With Service Bus and azure function, now messages are not lost because of network failures or application crashes. This improves the reliability of the webapp.
