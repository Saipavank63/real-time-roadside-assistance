provider "aws" {
  region = "us-west-2" # Change as needed
}

resource "aws_kinesis_stream" "roadside_events" {
  name             = "roadside-assistance-events"
  shard_count      = 2
  retention_period = 24

  shard_level_metrics = [
    "IncomingBytes",
    "OutgoingBytes",
    "IncomingRecords",
    "OutgoingRecords",
    "IteratorAgeMilliseconds",
    "ReadProvisionedThroughputExceeded",
    "WriteProvisionedThroughputExceeded"
  ]

  tags = {
    Environment = "production"
    Project     = "RealTimeRoadsideAssistance"
  }
}
