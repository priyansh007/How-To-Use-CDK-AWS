## README: How to Use AWS CDK, Terraform CDK, and Hashicorp Terraform

This project demonstrates the usage of AWS CDK (Cloud Development Kit) in Python, Terraform CDK in Python, and Hashicorp Terraform to create a basic queue in AWS.

### Prerequisites 
Configure your AWS credentials:
   `aws configure`

### AWS CDK

1. Install the AWS CDK globally:
   `npm install -g aws-cdk@2.136.1`
2. Create a virtual environment and install the required dependencies:
   `python3 -m venv myLib`
   `pip3 install -r requirements.txt`
3. Navigate to the `aws-cdk-demo` directory:
   `cd aws-cdk-demo`
4. Initialize the AWS CDK project:
   `cdk init app --language python`
5. To deploy the AWS CDK stack:
   `cdk synth`
   `cdk deploy`
   This will create an SQS queue and a CloudFormation template named "AwsCdkDemoStack-CIC".

### Terraform CDK

1. Install the Terraform CDK:
   `brew install cdktf`
2. Navigate to the `terraform-cdk-demo` directory:
   `cd terraform-cdk-demo`
3. Initialize the Terraform CDK project:
   `cdktf init`
4. To deploy the Terraform CDK stack:
   `cdktf synth`
   `cd cdktf.out/stacks/aws-cdk-demo``
   `terraform init`
   `terraform apply`

### Hashicorp Terraform

1. Navigate to the `terraform-hashicorp` directory:
   `cd terraform-hashicorp`
2. Initialize Terraform:
   `terraform init`
3. Validate the Terraform configuration:
   `terraform validate`
4. Apply the Terraform configuration:
   `terraform apply -auto-approve`
5. To delete the resources:
   `terraform destroy`

Remember to clean up the resources created by each approach to avoid incurring unnecessary costs.