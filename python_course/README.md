The script run_scp_task.sh automates the daily execution of a certificate rotation container and conditionally restarts the artemis-broker container based on log output.

### Prerequisites:
 1. Podman and Podman Compose installed. 
 2. scp-task-certificate-management and artemis-broker containers defined in your podman-compose.yml. 
 3. Cron installed and enabled.

### What Is a Cron Job? 
A cron job is a scheduled task in Unix-like systems that runs automatically at specified intervals. It's managed by the cron daemon, which checks a configuration file called the crontab to determine what to run and when.

### Basic crontab commands: 
1. Use crontab -l to see the cron expressions that has been added till date. 
2. Use crontab -r to remove a cron expression. (Avoid using this command as it removes all the expressions added till date).
3. Use crontab -e to add a cron expression.

### What does the script run_scp_task.sh does? 
1. This script starts the scp-task-certificate-management container using Podman Compose. 
2. Waits briefly for logs to populate. 
3. Checks the logs for the phrase "Rotation success event captured". 
4. If found, restarts the artemis-broker container. 
5. If not found, then just prints "Certificate up to date".

### When does the run_scp_task.sh script execute? 
According to the cron expression which has been added this script runs everyday at midnight. The cron expression to execute it everday midnight would be something like 0 0 * * * 

### Steps to execute run_scp_task.sh script:
1. This script can be found in the folder cicd-dm-config/scripts/run_scp_task.sh 
2. Head to the above location and run the script using the command ./run_scp_task.sh 
3. Once you run the script it will create a log file called cert_rotation_check.log.
4. This log file will be created in the folder cicd-dm-config/countrybox/ 
5. Open the log file to see all the details like Execution Timestamp, and Containers logs.