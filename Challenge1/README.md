Challenge #1

A 3-tier environment is a common setup. Use a tool of your choosing/familiarity create these resources. 
Please remember we will not be judged on the outcome but more focusing on the approach, style and reproducibility.

Solution:
We have developed this solution keeping AWS CloudFormation tool in mind. Here, you will find 2 templates and 1 python script as core files which will be explained below.

mylocalvpctemplate.yaml: This is a AWS CloudFormation template for VPC. for VPC. It Creates a multi-tier network appropriate for a web application, including subnets for 
						 application, application load balancer (can disable), database (can disabled using parameter), and shared services (can disable). Creates IGW and 
						 NAT Gateway for providing internet access to underlying resources in respective public and private subnet.
						
cloud_multi_tiertemplate.yaml: This is a AWS CloudFormation template for a static web app. This template installs a highly-available, scalable web application deployment.
							   It demonstrates using the AWS CloudFormation bootstrap script "webapp_server_setup.py" to deploy a stateless web application. Here we 
							   are creating an Application Load Balancer(ALB) with three subnet and Auto Scaling Group(ASG) for WebApp tier of minimum size 3 and maximum Size
							   can be provided during deployment. Also, A dynamo DB service is created for DB tier.
							   
webapp_server_setup.py:  This is a bootstrap script for setting up a sample webApplication on ec2 instance. It is passed through userdata in LaunchConfig of ASG for WebApp tier 
						 at the time of ec2 launch. The path for this file is defined in ServerCodeUrl: in the cloud_multi_tiertemplate.yaml.