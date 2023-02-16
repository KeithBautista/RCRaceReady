Project milestone 5 for Code Institute Full-stack development program: Django Framework.<br>
RCReadyRace is an online store dedicated to providing the latest and greatest in remote controlled vehicles. Our inventory includes a wide variety of RC cars, trucks, planes, boats, and drones, perfect for both hobbyists and serious racers.

This website features an intuitive and easy-to-navigate interface, allowing you to easily browse and select from our extensive selection of high-quality products. It offers detailed product descriptions, specifications, and customer reviews to help you make an informed purchasing decision.

[Live Project Here](https://rcraceready.herokuapp.com/)

README Table Content


- [AWS Setup Process](#aws-setup-process)
    - [AWS S3 Bucket](#aws-s3-bucket)
    - [IAM Set Up](#iam-set-up)


### AWS S3 Bucket 

The deployed website utilizes AWS S3 Buckets to store static and media files. Here's a step-by-step guide to setting up an AWS S3 Bucket:

1.Create an AWS account by following this link.
2.Log in to your account and type "S3" in the search bar.
3.Click on "Create Bucket" on the S3 page.
4.Name the bucket and select the region closest to you.
5.Under "Object Ownership," select "ACLs enabled."
6.Uncheck "Block Public Access" and acknowledge that the bucket will be made public, then click "Create Bucket."
7.In the created bucket, click on the "Properties" tab. Under "Static Website Hosting," click "Edit," and enable static website hosting. Copy the default values for the index and error documents and click "Save Changes."
8.Go to the "Permissions" tab, click "Edit" below "Cross-origin Resource Sharing (CORS)," and paste in the following code:

  ```
    [
        {
            "AllowedHeaders": [
            "Authorization"
            ],
            "AllowedMethods": [
            "GET"
            ],
            "AllowedOrigins": [
            "*"
            ],
            "ExposeHeaders": []
        }
    ]
  ```

  Go to the "Bucket Policy" section and click "Edit."
9.Click "Policy Generator."
10.In the "Select Type of Policy" dropdown, select "S3 Bucket Policy."
11.In the "Principle" field, allow all principals by typing "*."
12.In the "Actions" dropdown menu, select "Get Object."
13.In the previous tab, copy the "Bucket ARN number."
14.Paste the ARN number into the "Amazon Resource Name (ARN)" field in the policy generator.
15.Click "Add statement > Generate Policy."
16.Copy the generated policy and paste it into the "Bucket Policy Editor."
17.Before saving, add "/*" at the end of your "Resource Key" to allow access to all resources within the bucket.
18.Once saved, go to the "Access Control List (ACL)" and click "Edit."
19.Next to "Everyone (public access)," check the "list" checkbox.
20.Save your changes.