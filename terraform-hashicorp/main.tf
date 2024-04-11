provider "aws" {
    region = "${var.aws_region}"
}

resource "aws_sqs_queue" "TerraformHQueue" {
  name                      = "TerraformHQueue"
  visibility_timeout_seconds = 300
}

output "queue_name" {
  value = aws_sqs_queue.TerraformHQueue.name
}