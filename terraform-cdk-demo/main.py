import os
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.sqs_queue import SqsQueue

class AwsCdkDemoStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Configure the AWS provider
        AwsProvider(self, "aws",
                    region=os.getenv('CDK_DEFAULT_REGION', 'us-east-2'))

        # Create an SQS queue
        queue = SqsQueue(self, "AwsCdkDemoQueue",
                         visibility_timeout_seconds=300)

        # Output the queue name
        TerraformOutput(self, "queue_name",
                        value=queue.name)

if __name__ == "__main__":
    app = App()
    AwsCdkDemoStack(app, "aws-cdk-demo")
    app.synth()