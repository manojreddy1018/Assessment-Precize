# Assessment 1 -Precize 
### To Buid the docker container from docker file.
```
sudo docker build -t python3.
```
### For creating a directory on your host machine to store the report.
```
mkdir -p ~/reports
```
### Run the Docker container and mount the output directory to your host machine.
```
docker run --rm -v ~/reports/output report
```
### To run this container periodically, we use a cron job on your Linux machine. Open your crontab configuration:
```
crontab -e
```
### Add the following line to run the container daily at midnight
```
0 0 * * * docker run --rm -v ~/reports/output report
```
