provider "aws" {
  region = "eu-central-1"
}

terraform {
  backend "s3" {
    bucket = "askdevops-s3-terraform-backend"
    key    = "eu-central-1/vpc/vpc.tf"
    region = "eu-central-1"
  }
}