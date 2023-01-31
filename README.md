# iprange_genndcheck
iprange  generator nd checker

This code is a python script that scans a range of IP addresses and checks if they are accessible. The user inputs a start IP and end IP, and the script will check all IPs in the range by making HTTP GET requests using the requests library. The response status codes are checked, and if a response returns with a status code of 200, the IP is considered accessible and is written to a file called "result.txt". The script uses threading to perform the checks in parallel, making the process faster. The output of the script is the working IPs written to "result.txt" and a message indicating the completion of the scanning process.

![Screenshot_1](https://user-images.githubusercontent.com/108156491/215879814-ddc7dd82-54ac-4715-8463-880af4974048.jpg)
