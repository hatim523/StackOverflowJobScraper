## Write a Jobs crawler using Python’s Scrapy framework

**Requirements:**

- You will be using this start URL: https://stackoverflow.com/jobs?q=blockchain
- You need to collect all the job postings from this page and go to each job page.
- Pick up the following data points from the job page:
    1. Job Title
    2. Company
    3. Company logo’s image_url
    4. Location
    5. Skills required:  technologies
    6. Perks offered: visa, relocations, remote
    7. About this job
    8. Description
    9. Job link
- Run a full crawl and store all data in the JSON format file.
- Please use download delay to avoid getting blocked by website  :)
- **Bonus Task:** (Optional)
Generalize the start URL. Take Skill and Location as input and search on these parameters.
 For Example: Search for Blockchain(skill) jobs in Boston US(location)

We expect:
  1. a well-structured project with an output file.
  2. clean code (see python’s pep8)
  3. readme file with project approach and how-to instructions.
  4. requirements.txt (see python virtual envs)
  5. All assumptions mentioned in the readme file.
  6. Hours.txt with the detailed distribution of work, including learning time.