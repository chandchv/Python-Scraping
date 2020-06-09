import requests

from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET 
import csv
URL = 'https://ca.indeed.com/jobs?q=programmer&l=london'

# driver = webdriver.Chrome('C:/Users/chand/Downloads/chromedriver_win32/chromedriver.exe')
# driver.get(URL)
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')
# i = 10
# list_1 = [i for i in range(10, 300) if i % 10 == 0]
# length = len(list_1)
# print(length)
#for i in range(length): 
#    print(list[list_1])
#for list_1 in list:
#soup1 = ('https://ca.indeed.com/jobs?q=programmer&l=london&start='+format(i).text)
#    print('https://ca.indeed.com/jobs?q=programmer&l=london&start='+str(list_1))
with open("indeed_programmer_jobs.xml", "wb") as f: 
    data = ET.Element('Indeed_ca') 
    element1 = ET.SubElement(data, 'Jobs')
    x1 = 10
    x_list = [x1 for x1 in range(1, 11) if x1 % 10 == 0]
    print(x_list)
    length1 = len(x_list)
    #print (length1)

    for i11 in x_list: 
        #print (URL+'&start='+str(i11))
        soup1 = (URL+'&start='+str(i11))
        print (soup1)
        # f = open( './file.html', 'w' )
        # f.write( 'soup1 = ' + repr(soup1) + '\n' )
        # f.close()
        for urlnew in soup1:
            page = requests.get(soup1)
            soup = BeautifulSoup(page.content, 'html.parser')
            #print(page)
            results = soup.find('td', attrs={'id':'resultsCol'})
            #print(results) 
            #print(results.prettify())
            job_elems = results.find_all('div', attrs ={'data-tn-component':'organicJob'})
            #print(job_elems)
                    
            # with open("indeed"+str(soup1.rsplit('=', 1)[1])+".xml", "wb") as f: 
                # data = ET.Element('Indeed_ca') 
                # element1 = ET.SubElement(data, 'Jobs')

            for job_elem in job_elems:
                title_elem = job_elem.find('h2', class_='title')
                company_elem = job_elem.find('span', class_='company')
                location_elem = job_elem.find('span', class_='location')
                print(title_elem.text)
                print(company_elem.text)
                print(location_elem.text)
                s_elem1 = ET.SubElement(element1, 'title') 
                s_elem2 = ET.SubElement(element1, 'company')
                s_elem3 = ET.SubElement(element1, 'location') 
                s_elem4 = ET.SubElement(element1, 'summary')       
                s_elem1.text = title_elem.text
                s_elem2.text = company_elem.text
                s_elem3.text = location_elem.text
                summary_list = soup.find('div', class_='summary') # Start here
                for Lis in summary_list.find_all("li"):
                    print("->"+Lis.text)
                    s_elem4.text = Lis.text
                
    b_xml = ET.tostring(data)
    f.write(b_xml)
            