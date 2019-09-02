# XRP-SHOP Web API

This project is created with the intent of playing with Terraform, AWS and Circle-CI with a real project.  
The real project is the new cpre API for the XRP-SHOP project. The initial goal is to provide some administrative functions.  


## AWS

Created a new user and group.  
The API will be provided by AWS Lambda(s) accessed by AWS API Gateway.   

## Terraform

Manage an S3 bucket used to deploy the AWS Lambda (zip file).  
It will create the infrastructure for the API.  



## Circle CI

Example 1:  https://github.com/datapunkz/python-cicd-workshop/blob/master/.circleci/config.yml  
