import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import re
import os
import math
import time

os.chdir("C:/Users/Kile/Desktop")

url = urllib.request.urlopen("http://linguistlist.org/jobs/browse-jobs.cfm")
url_text = "http://linguistlist.org/jobs/browse-jobs.cfm"
jobs_count = int(BeautifulSoup(url).find("div", {"id":"content"}).h1.get_text().split()[0])
pages_count = math.ceil(jobs_count/15)


job_list = []
job_txt = []
job_txt.append("Location~Specialty~Date~URL\n")
n = 0

for i in range(pages_count):
    n+=1
    values = {"sortBy":"ISSUEDATEPOSTED", "order":"DESC",  "current":"2", "startrow":str(i*15+1), "Submit":str(i+1)}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url_text, data)
    req_url = urllib.request.urlopen(req)
    bsobj = BeautifulSoup(req_url)
    
    job = bsobj.findAll("tr",{"title":"Click to view job details"})
    for i in range(len(job)):
        temp = job[i].findAll("td")
        job_list.append({})
        job_list[i]["Location"] = temp[1].get_text().replace(" ","").replace("\n", "").split(":")[0]
        job_list[i]["Specialty"] = temp[3].get_text().replace("\n", "").split(";")
        job_list[i]["Specialty"][:] = [vac.strip() for vac in  job_list[i]["Specialty"]]        
        job_list[i]["Date"] = temp[5].get_text().replace(" ","").replace("\n", "").split("-")[0:3]
        job_list[i]["Date"][2] = job_list[i]["Date"][2][0:4]
        job_list[i]["Date"] = job_list[i]["Date"][0]+","+job_list[i]["Date"][1]+","+job_list[i]["Date"][2]
        job_list[i]["URL"] = "http://linguistlist.org"+job[i].attrs["onclick"][13:-2]

        for j in job_list[i]["Specialty"]:
            job_txt.append(job_list[i]["Location"]+"~"+j+"~"+job_list[i]["Date"]+"~"+job_list[i]["URL"]+"\n")
            
    print(n)
    time.sleep(0.1)



job_info_file = open("job_info_file.txt", "w",errors='ignore')
job_info_file.writelines(job_txt)
job_info_file.close()
        


        

"""
values = {"sortBy":"ISSUEDATEPOSTED", "order":"DESC",  "current":"2", "startrow":"136", "Submit":"10"}
data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url, data)
a = urllib.request.urlopen(req)
bsobj = BeautifulSoup(a)
print(bsobj)
"""
