resource "aws_dynamodb_table" "roadside_events" {
  name           = "RoadsideEvents"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "eventId"

  attribute {
    name = "eventId"
    type = "S"
  }
}
