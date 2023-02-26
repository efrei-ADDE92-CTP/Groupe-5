# Groupe-5 : Deploy an ML app 

Technologies : Github, Azure, Prometheus, 


1. Deploy an API 
- Python : get predictions of iris classifications using K Nearest Neighbors
- Create an API

2. Build the docker image
- On Linux
- Using Python 3.8
- Push -> luciebottin/iris-docker

3. Deploy it on the Azure Container Registry (ACR)
- Create a github workflow
- Use secrets
- Azure :
  - We could have used Azure Devops, generate our token to access to Azure, it's already done by our organisation

![Dashboard](img/acr.png)

  
4. Deploy it on Azure App
- Auto-scaling
- Endpoint : TO ADD

![Dashboard](img/containerapp2.png)

5. Display Metrics on endpoint
- Prometheus

6. Load Test
- Vegeta for CLI

![Dashboard](img/vegeta.png)

- K6 for API
-> docker run --rm -i grafana/k6 run - <script.js

![Dashboard](img/k6.png)


- Octoperf for SaaS