import requests
from xlwt import Workbook
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

BASE_URL='https://remoteok.com/api/'
USER_AGENT='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
 
REQUEST_HEADER={
    'User-Agent': USER_AGENT,
    'Accept_language':'en-Us , en;q=0.5'
}
 
def req_get_job_postings():
    res= requests.get(BASE_URL,headers=REQUEST_HEADER)
    return res.json()

def to_xls(data):
    wb = Workbook()
    sheet = wb.add_sheet('Jobs')
    headers = list(data[0].keys())
    for i in range(len(headers)):
        sheet.write(0,i,headers[i])
    for i in range(len(data)):
        values = list(data[i].values())
        for j in range(len(values)):
            sheet.write(i+1, j, values[j])
    wb.save("remote_jobs.xls")

 
if __name__== "__main__":
    data=req_get_job_postings()[1:]
    to_xls(data)