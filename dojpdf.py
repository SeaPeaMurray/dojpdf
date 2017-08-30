import pdfquery
import xml.etree.ElementTree as ET
import pandas as pd

def conv(file):
	# assert type(file) == <type 'str'>
	pdf = pdfquery.PDFQuery(file)
	pdf.load()
	pdf.tree.write(str(file).split(".")[0] + '.xml', pretty_print=True)
	myxml = open(str(file).split('.')[0] + '.xml').read()
	xmlread = ET.XML(myxml)
	print "There are {} pages in the file.".format(len(xmlread))
	for page in xmlread:
		for element in page:
			if element.tag != 'LTRect':
				for subelement in element:
					print subelement.text
					print subelement.attrib['y0']

conv('L107-tbl_FOIA_case.pdf')