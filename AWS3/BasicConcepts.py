# Section A: Basics

# 1. What type of storage does Amazon S3 provide: Block, File, or Object?
    # S3 provides Object storage, EFS is file storage and EBS is for block storage, all withing AWS.

# 2. What is the minimum number of S3 buckets you can create in AWS?
    # We need to make at least 1 bucket to be able to use S3 services.

# 3. Write the CLI command to create a bucket named de-course-bucket.
    # aws s3 mb s3://autopulse-data-lake-12345

# 4. How do you upload a file named data.csv into an S3 bucket using CLI?
    # aws s3 cp <data.csv local path> <s3 URI>

# 5. What’s the difference between an object key and an object URL?
    # An object key identifies an object inside a bucket, while an object URL is the web address used to access that object.


# Section B: Core Operations

# aws s3 mb s3://student-data-lake-julio --region us-east-1

# aws s3 cp "C:\Users\Julio Diaz\Downloads\students.csv" s3://student-data-lake-julio/raw

# aws s3 cp s3://student-data-lake-julio/raw "C:\Users\Julio Diaz\Downloads\students.csv"

# aws s3api put-bucket-versioning --bucket student-data-lake-julio --versioning-configuration Status=Enabled

# Both versions are there.
    #  aws s3api list-object-versions --bucket student-data-lake-julio --prefix raw/students.csv --no-cli-pager
        # {
        #     "RequestCharged": null,
        #     "Prefix": "raw/students.csv"
        # }


# Standard version we can pick between infrequent access and frequent access. Standard is for frequent access and Standard-IA is for infrequent access.
# Intelligent-Tiering is for us alloing AWS3 to decide weather something needs to be frequent access or infrequent access depending on the current usage, this will cost more because we'll need to let AWS3 scan.

# SSE-S3 is encryption managed by the S3 service, it is the lowest level of encryption offered.
# SSE-KMS is encryption managed by KMS, Key Management System it is a better encryption which offers full control of the encryption by accessing it through a complete service only dedicated to it.
# SSE-C is double the encryption offered by KMS.