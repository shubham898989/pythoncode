import jenkins
jenkins_client = jenkins.Jenkins('http://52.7.104.67/', username='user', password='pCG3tQreFus5')
jobs = jenkins_client.get_all_jobs(folder_depth=None)
for job in jobs:
    print(job['fullname'])