# AWS

## CLI

Create profile.  

You need a user in AWS. Create one on the online  AWS Console.  
You will obtain the secret and public keys.  

> aws configure [--profile profile-name]
By default the profile is names "default", use _--profile_ to assigna a different one

In order to create teh bucket the profile must have the **"AmazonS3FullAccess"** policy.  
