# Heart Disease Project

## Problem Statement

Heart disease is the leading cause of death worldwide, accounting for one third of deaths in 2019. Heart disease cases nearly doubled over the period, from 271 million in 1990 to 523 million in 2019, and the number of heart disease deaths rose from 12.1 million to 18.6 million. The efficient and accurate and early medical diagnosis of heart disease plays a crucial role in taking preventive measures to prevent death.

The aim of this notebook is to find out which algorithm performs the best in predicting whether you are at a risk of developing a heart disease or not.

**Why Machnine Learning?**

ML is best suited for complex problems that are not answered by simple logic. In healthcare, disease epidemiology is often complex and our understanding changing. This makes diseases, such as stroke, prime candidates for ML.

## Instructions
* For quick review: select `Midterm_Project - heart_disease.ipynb` in respository and scroll.
* To run: Open `Midterm_Project - heart_disease.ipynb`.
  * The notebook can be downloaded and run on a local Jupyter instance.  

### Midterm_Project - heart_disease.ipynb

* Throughout this notebook you will find links to further understading or clarification of various concepts.

### Containerization: 
  * In `notebook.ipynb`, see section section *Deployment*, then subsection *BentoML* on build instructions.
  * To build a bento instance for live test, notebook must be run on a local Jupyter instance.
  * Bentoml commands are listed but not run from the notebook.

#### Cloud deployment on AWS


1.Login to AWS Console
2.Go to Elastic Container Registry. Select Create Registry.
3.In registry select "View push commands"
- On local Windows PC use GitBash and follow macOS/Linux commands.NOTE: Must have AWS CLI installed.
- AWS console, login via the prompts.
- (Get-ECRLoginCommand).Password | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com
- Skip this command, docker build done though bentoml -> docker build -t heart-disease .
- docker tag heart-disease:latest [censored].dkr.ecr.us-east-1.amazonaws.com/heart-disease:latest
- docker push [censored].dkr.ecr.us-east-1.amazonaws.com/heart-disease:latest
4.Move to Elastic Container Service, then Select Create new Task Definition.
- Follow prompts, be sure to sleect image uploaded to the registry.
- Then select Create
5.Select Clusters on the left pane, then Select create cluster.
- Follow the prompts to create cluster
- Select the cluster
- Select Tasks and then Run new Task
- Follow prompts and select the created task.
    - select Run Task
6.Select ECS and add container
- Enter the Container name (heart-disease-container) and Image URI
- Memory Limits(MiB), set to Soft limit and 256
- Port mappings, Container port 3000 and Protocol tcp
- Click to end at the end
7.Cluster
- Go Cluster again and clik to Tasks
- Run a new task
- Launch type, FARGATE
- Operating system family, Linux
- Cluster VPC*, select the defaul value
- Subnets, us-east-1a
- Security groups, Type = Custom TCP, Port range = 3000
- Go back to Cluster and wait for the Last status value until it gets from Provisioning to Running
- Select the task from the column
- From the Network you can copy the Public IP
- Now you can reach the Bentoml Api by using this Public IP and addin to the end port number (3000)
- For instance: 54.161.38.215:3000

**Files**
* Notebook: `Midterm_Project - heart_disease.ipynb`
* Data: `heart.csv`
* ML script: `service_midterm.py`
  * Note: Model is saved locally via bentoml 
* Dependency and enviroment management: `bentofile.yaml`


Production App Access

To access production site go here: http://54.161.38.215:3000/

Select Try it out in the POST section. Use template below. Change the variable

![image]

In Request body enter patient information based on template

Given samles must be in NumpyNdarray format.
Template: [[0.583333,0.320755,0.625440,0,0.622800,0,0.322000,2,1,0,0,0,1,0,0,1,0,1,0]]

Select Execute

Scroll down to Server response and see response in Response body.



## Production App Access

**Instructions**

1.) To access production site go here: http://34.207.77.6:3000/#/Service%20APIs/stroke_prediction__classify

2.) Select Try it out in the POST section.

![image](https://github.com/ukvar/Machine-Learning-Zoomcamp-Homeworks/blob/main/Midterm-Project/serviceapi1.PNG)

3.) In Request body enter patient information based on template or paste in example patient. Select Execute.

![image](https://github.com/ukvar/Machine-Learning-Zoomcamp-Homeworks/blob/main/Midterm-Project/serviceapi2.PNG)
![image](https://github.com/ukvar/Machine-Learning-Zoomcamp-Homeworks/blob/main/Midterm-Project/serviceapi3.PNG)

4.) Scroll down to Server response and see response in Response body.
