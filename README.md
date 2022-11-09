
### Running Example

Run on Windows Development Machine
````
mlflow ui --backend-store-uri mysql://root:123456@127.0.0.1:3306/mlflow --host 0.0.0.0
````
Run on Linux server
````
mlflow server -p 10003 --backend-store-uri mysql://cumtcsb617:741852369@43.143.136.241:3306/mlflow --host 0.0.0.0 --default-artifact-root /home/pywork/mlwork/artifacts
````
Run on Linux server (Redirect Stderr)
````
nohup mlflow server -p 10003 --backend-store-uri mysql://cumtcsb617:741852369@43.143.136.241:3306/mlflow --host 0.0.0.0 --default-artifact-root file:///home/pywork/mlwork/artifacts > mlflow.log
````