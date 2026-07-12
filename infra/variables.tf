variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "eu-central-1"
}

variable "terraform_state_bucket_name" {
  description = "Name of the S3 bucket for Terraform state"
  type        = string
  default     = "devops-weiterbildung-terraform-state"
}

variable "environment" {
  description = "Environment name (staging or prod)"
  type        = string
  default     = "staging"
}

variable "ec2_ami" {
  description = "AMI ID for EC2 instance (Ubuntu 22.04 eu-central-1)"
  type        = string
  default     = "ami-0faab6bdbac9486fb"
}

variable "key_name" {
  description = "Name of the AWS key pair for SSH access"
  type        = string
  default     = "devops-weiterbildung"
}
