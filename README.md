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
  - We used Azure Devops, generated our token to access to Azure
  -
  
4. Deploy it on Azure App
- Auto-scaling

5. Display Metrics on endpoint
- Prometheus
