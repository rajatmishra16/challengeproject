Challenge #2

We need to write code that will query the meta data of an instance within AWS and provide a json formatted output.The choice of language and implementation is up to you. 
Bonus Points The code allows for a particular data key to be retrieved individually 
Hints · Aws Documentation (https://docs.aws.amazon.com/) · 
		Azure Documentation (https://docs.microsoft.com/en-us/azure/?product=featured) ·
		Google Documentation (https://cloud.google.com/docs)
		
Solution:
 
 As the challenge mentions that we need to query instance data within AWS. We can view all categories of instance metadata from within a running instance, use the following URI.
 http://169.254.169.254/latest/meta-data/
 
 AWS Reference:  https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html
 
 We have used same concept to build this solution.
 
 Usage: If you want to see complete metadata, Please press \'M/m\'. If you want to see particular metadata key, Please Press \'K/k\':"
 
 If you press M or m. This script will provide all the metadata available for the running instance. By querying each value that it get after querying the base url in a for loop:
  http://169.254.169.254/latest/meta-data/
  
 If you press K or k. This script will promt for "Please Enter meta-data key:". Here you can provide the metadata key that you want to query from a running instance.
 
 If you press any other key apart from above mentioned keys. Script will stop with message "Incorrect Usage".