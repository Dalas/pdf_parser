import PyPDF2


KEY = '/Annots'
URI = '/URI'
ANK = '/A'


def get_urls_from_file(fp):
    file = PyPDF2.PdfFileReader(fp)
    pages = file.getNumPages()

    result = []

    for page in range(pages):

        page_sliced = file.getPage(page)
        page_object = page_sliced.getObject()

        if KEY in page_object:
            ann = page_object[KEY]

            for a in ann:
                u = a.getObject()

                if ANK in u and URI in u[ANK]:
                    result.append(u[ANK][URI])

    return result
