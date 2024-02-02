import PyPDF2


class FileReader:
    @staticmethod
    def read_pdf_files(path):
        with open(path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            all_text = ''
            for page in pdf_reader.pages:
                text = page.extract_text()
                all_text = all_text + text

        return all_text
