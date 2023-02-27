# Groupe-5 : Deploy an ML app 

Technologies : Github, Azure, Prometheus, 


<h2>1. Deploy an API</h2> 
- Python : get predictions of iris classifications using K Nearest Neighbors
- Create an API

<h2>2. Build the docker image</h2>
- On Linux
- Using Python 3.8
- Push -> luciebottin/iris-docker

<h2>3. Deploy it on the Azure Container Registry (ACR)</h2>
- Create a github workflow
- Use secrets
- Azure :
  - We could have used Azure Devops, generate our token to access to Azure, it's already done by our organisation

![Dashboard](img/acr.png)

  
<h2>4. Deploy it on Azure App</h2>
- Auto-scaling
- Endpoint : https://container-app-gr1--zxh954n.icybush-d5d8ff73.westeurope.azurecontainerapps.io

![Dashboard](img/containerapp2.png)

<h2>5. Display Metrics on endpoint</h2>
- Prometheus

<h2>6. Load Test</h2>
- Vegeta for CLI

![Dashboard](img/vegeta.png)

- K6 for API
-> docker run --rm -i grafana/k6 run - <script.js

![Dashboard](img/k6.png)


- Octoperf for SaaS

![Dashboard](img/octoperf.png)
