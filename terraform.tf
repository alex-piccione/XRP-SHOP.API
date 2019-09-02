provider "aws" {
    profile = "xrp-shop"
    region = "eu-west-2"
}

resource "aws_s3_bucket" "b" {
    bucket = "xrpshop-1"
    acl = "private"    
    
    tags = {
        Name = "XRP-SHOP"
        Environment = "Dev"
    }
}
   