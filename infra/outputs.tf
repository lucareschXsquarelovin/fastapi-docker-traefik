output "terraform_state_bucket_name" {
  description = "Name of the Terraform state S3 bucket"
  value       = aws_s3_bucket.terraform_state.bucket
}

output "k3s_instance_public_ip" {
  description = "Public IP of the k3s EC2 instance"
  value       = aws_instance.k3s.public_ip
}

output "k3s_instance_id" {
  description = "Instance ID of the k3s EC2 instance"
  value       = aws_instance.k3s.id
}
