# Machine Learning Workflow for Scones Unlimited on Amazon SageMaker

Welcome to the Machine Learning Workflow project for Scones Unlimited on Amazon SageMaker! This project aims to set up, train, deploy, and monitor a machine learning model for image classification using Amazon SageMaker.

## Overview

In this project, we will create a machine learning workflow to classify images of scones using Amazon SageMaker. The workflow includes setting up SageMaker Studio, preparing the data, training an image classification model, deploying the model as an API endpoint, and monitoring the deployed model for errors.

## Setup Instructions

1. **SageMaker Studio Workspace Setup**:
   - Follow the provided instructions to set up a SageMaker Studio workspace.
   - Configure a kernel suitable for running the project.

## Data Preparation

2. **Loading and Preparing Data**:
   - Complete the ETL (Extract, Transform, Load) section of the starter code to prepare the data for machine learning with SageMaker.

## Model Training

3. **Training a Machine Learning Model**:
   - Train an image classification model as per the provided instructions up to the stage of "Getting ready to deploy".
   - Successfully train the model and prepare for deployment.

## Model Deployment

4. **Deploying Model as API Endpoint**:
   - Deploy the trained ML model onto SageMaker.
   - Construct an API endpoint associated with the deployed model.
   - Print a unique model endpoint name in the notebook for future use.
   
5. **Making Predictions**:
   - Demonstrate successful predictions using a sample image through the deployed API endpoint.

## Machine Learning Workflow

6. **Authoring Lambda Functions**:
   - Author three Lambda functions as specified:
     - The first Lambda returns an object to the Step Function as image_data in an event.
     - The second Lambda handles image classification.
     - The third Lambda filters low-confidence inferences.
   - Save the code for each Lambda function in a Python script.

7. **Authoring Step Function**:
   - Compose the Lambdas together in a Step Function.
   - Export the Step Function definition as JSON.
   - Provide a screenshot of the working Step Function.

## Model Monitoring

8. **Monitoring Model for Errors**:
   - Extract Monitoring data from S3.
   - Load the data from Model Monitor into the notebook.
   - Visualize Model Monitor data and create custom visualizations of the outputs.

## Conclusion

By completing all the specified tasks, you will demonstrate proficiency in setting up SageMaker Studio, preparing data, training and deploying machine learning models, constructing a machine learning workflow with Lambda functions and Step Functions, and monitoring the deployed model for errors.

Feel free to refer to the provided instructions and documentation throughout the project for guidance and assistance. Good luck with your Machine Learning Workflow project for Scones Unlimited on Amazon SageMaker!