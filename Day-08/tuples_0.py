# s3_bucket_lists = ["surendra-demo-bucket", "abhishek-demo-bucket", "ram-demo-bucket", "krishna-demo-bucket"]
# print(s3_bucket_lists[0])

s3_bucket_lists = ["surendra-demo-bucket", "abhishek-demo-bucket", "ram-demo-bucket", "krishna-demo-bucket"]
print(len(s3_bucket_lists))

s3_bucket_lists.append("raju-demo-bucket")
print(len(s3_bucket_lists))

s3_bucket_lists.remove("raju-demo-bucket")
s3_bucket_lists.remove("krishna-demo-bucket")
print(len(s3_bucket_lists))