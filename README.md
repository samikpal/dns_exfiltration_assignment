# DNS Exfiltration Assignment
## TASK 1: 
In this task, I try to train a model to detect DNS entries for attempts of cyber-attacks.
The entire experiment has been divided into the following steps: 
1.	Data Analysis and data Engineering and Data Cleaning
2.	Feature Filtering/Selection
3.	Model
4.	Evaluation
5.	Save Model

## TASK 2: 
Here I deploy the trained model on dataset of DNS entries which are being streamed through Kafka. 
Steps:
1. Create 2 version of the saved model: Static and Dynamic 
2. Get 1 datapoint.
3. Evaluate using both models
4. Check if evaluation is correct or not and maintain an accuracy score
5. Maintain a dataset of all datapoints accessed so far.
6. When the accuracy score for the Dynamic model falls below a set threshold, retrain the model on the dataset collected so far. 
