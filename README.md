# Software Engineer

Hello, and welcome from the Syniti Engineering Team!

Thank you for your interest in joining Syniti, we're working on some
interesting and challenging problems and are looking for engineers with a
growth mindset to join our team. Our interview process helps us learn about
you as a person and at a technical level. But it's just as important that you
learn about us, our work, and our expectations so you know what you're
getting into. We foster a work environment where we are all comfortable and
love coming to work each day. We don't hire lightly and expect everyone to
contribute on day one.

Let's get started!

Please clone or download this repo and use it for the exercises described below.
Once completed you may either send us the URL to your git repo or a zip of
the folder.

We have four questions that we like to ask to get a sense of who you are, 
followed by a coding question we use to understand your technical strengths. 
You can write your responses to the first four questions directly in the README 
or as a separate file.

In answering the code question, please submit code as if you intended to
ship it to production. The details matter. Tests are expected, as is
well-written, simple, idiomatic code. While there are many libraries you
could use, we're expecting to mostly see code that you write yourself. Please
only use critical libraries for common functionality, such as parsing JSON or
writing tests.

We'd recommend you use whatever language you feel strongest in. It doesn't have
to be one we use (mostly Go and JavaScript) — we believe good engineers can be 
productive in any language.

Here are the questions, good luck!

1. What’s your proudest achievement? It can be a personal project or something
   you’ve worked on professionally. Just a short paragraph is fine, but I’d
   love to know why you’re proud of it.

   I generally have the habit of taking up complex stories one such story was developing Glue terraform module it was extremely challenging as there were no reference for creating it, also it was an urgent requirement and delivered it within the stipulated time by gathering all the necessary information from scratch. I am very proud to say that I completed this without taking any help from my senior members and this also gave me more confidence to do complex stories.

2. What's a personal project you're currently working on? This could be a
   coding side project, hobby, or otherwise real world project you're working
   on.

   Currently working on building real time compliance detector and remediator module using Config, SSM document and Lambda, Using this framework we can immediately detect non-compliance AWS resource as per our compliance rules and remediate them in near real time.

3. Tell us about a technical book or article you read recently, why you liked
   it, and why we should read it.

   https://aws.amazon.com/blogs/storage/migrate-your-amazon-ebs-volumes-from-gp2-to-gp3-and-save-up-to-20-on-costs/ 
   AWS announced general availability of a new Amazon EBS General Purpose SSD volume type, gp3. AWS designed gp3 to provide predictable 3,000 IOPS baseline performance and 125 MiB/s, regardless of volume size. With gp3 volumes, you can provision IOPS and throughput independently, without increasing storage size, at costs up to 20% lower per GB compared to gp2 volumes. 
   Incase if you are using GP2 volumes we can have a migration plan to convert existing GP2 volumes to GP3 and avail the cost benefits.

4. Tell us about one of your favorite products (physical or software) and one
   specific aspect that makes it truly great.

   I really liked digital wallet platform and online payment system especially Google Pay, which eradicates the normal payment scenario that does not require recipient bank details like account number, IFSC code which completely makes payment difficult. With google pay all that is required is the phone number or QR code, enter the amount and secret code, amount is sent to recipients.

5. In this repo is a `data.json` file. It contains an imaginary example set
   of data a customer might need to migrate from one system to another. It's a
   JSON encoded array of objects. The customer understands some of the data
   might be bad and wants to know which records are invalid so they can ensure
   the new system will only have valid data. Write a program that will read
   in the data and mark any records:

   1. That are a duplicate of another record
   2. `name` field is null, missing, or blank
   3. `address` field is null, missing, or blank
   4. `zip` is null, missing, or an invalid U.S. zipcode

   Each record has an ID but that should only be used to identify a record,
   not for validity or duplication testing (eg, two records may be identical
   but have different IDs).

The output of the program should list the IDs of each invalid or duplicate
record, one per line. In the case of duplicates, mark both.

Example:

```
123ba
439a2
99abc
bac34
```

If you have any questions about the coding questions, please let us know.
