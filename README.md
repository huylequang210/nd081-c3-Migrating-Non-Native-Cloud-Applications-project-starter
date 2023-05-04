# TechConf Registration Website

Live Site: https://huylequang210.azurewebsites.net

## Monthly Cost Analysis
Complete a month cost analysis of each Azure resource to give an estimate total cost using the table below:

| Azure Resource | Service Tier | Monthly Cost |
| ------------ | ------------ | ------------ |
| *Azure Postgres Database* | Flexible Server - Burstable, B1ms, 1 vCores, 2 GiB RAM, 32 GiB storage |  16.09 $ |
| *Azure Service Bus*   | Basic     | 0.5 $ |
| *Azure Web App*  | Free (F1) | - $   |
| *Azure Function App* | Consumption (Serverless) - Free | - $ |
| TOTAL | | 16.59 $|

## Architecture Explanation
- Service Bus makes notifications task runs faster because it provides a background tasks to execute resource-intensive, time-consuming tasks. Now the web app is more responsive, and free up to take others incoming requests. Instead of waiting the webapp processes notifications synchronously as a part of request cycle, we now can off load it processing to a seperate background task.
- With Service Bus and azure function, now messages are not lost because of network failures or application crashes. This improves the reliability of the webapp.
- With Azure Web App plan F1, It's free, so it requires zero cost for hosting. And even though it's free, it still provides scalability, and automatically scale webapp based on demand.
- Azure Postgres Database Flexible Server provides scalability. It offers high availability, ensuring webapp stay ups and running. It also gets updated by Microsoft via patches, allows developers focus on features.
- Azure Function App Consumption (Serverless) is cost-effective. We only need to pay for the actual execution time of the function.