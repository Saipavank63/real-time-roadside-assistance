resource "aws_s3_bucket" "roadside_archive" {
  bucket = "roadside-event-archive"
}

resource "aws_s3_bucket_lifecycle_configuration" "archive_policy" {
  bucket = aws_s3_bucket.roadside_archive.id

  rule {
    id     = "archive-rule"
    status = "Enabled"

    transition {
      days          = 30
      storage_class = "STANDARD_IA"
    }

    transition {
      days          = 90
      storage_class = "GLACIER"
    }

    expiration {
      days = 365
    }
  }
}
