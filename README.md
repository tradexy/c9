# c9
Cloud9 test
create environment AWS cloud9 using ec2 
Run configurations / run config / run new config. Use command in 
(python3) hello.py 5 9
(python3) s3.py my-test-bucket221026 us-west-2
following
https://docs.aws.amazon.com/cloud9/latest/user-guide/sample-python.html


note file path error as default set to environment, need to add c9 to path to run command
python3: can't open file '/home/ec2-user/environment/python3': [Errno 2] No such file or directory

else in the command line use 
python 3 hello.py 5 9
