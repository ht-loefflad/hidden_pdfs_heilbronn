# check whether duplicate via hash?
import PyPDF2
import json


class Reader:

    def read_json(self):
        json_file_obj = open('C:\\Users\\kbr\\Desktop\\testjson.json')
        data = json.load(json_file_obj)
        for i in data['Result']:
            print(i)
        json_file_obj.close()

    def read_pdf(self):
        # TODO use actually useful pdf
        pdf_file_obj = open('C:\\Users\\kbr\\Downloads\\NgR_Beitrittserklaerung-und-Einzugsermaechtigung.pdf', 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
        print(pdf_reader.numPages)
        page_obj = pdf_reader.getPage(0)
        print(page_obj.extractText())
        pdf_file_obj.close()
