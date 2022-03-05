# check whether duplicate via hash?
import PyPDF2

class pdf:
    def __init__(self):
        pass

    def read_pdf(self):
        pdf_file_obj = open('C:\\Users\\kbr\\Downloads\\NgR_Beitrittserklaerung-und-Einzugsermaechtigung.pdf', 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
        print(pdf_reader.numPages)
        page_obj = pdf_reader.getPage(0)
        print(page_obj.extractText())
        pdf_file_obj.close()
