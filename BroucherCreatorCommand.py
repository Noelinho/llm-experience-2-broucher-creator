import sys
from weasyprint import HTML
import markdown
from dotenv import load_dotenv

from Services.Scrapper.Scrapper import Scrapper
from Services.Creator.OpenAI.OpenAIBroucherCreator import OpenAIBroucherCreator
from Services.HtmlMaker.HtmlMaker import HtmlMaker

load_dotenv(override=True)

if len(sys.argv) < 2:
    print("Por favor, proporciona una URL como argumento.")
    sys.exit(1)

url = sys.argv[1]

scrapper = Scrapper()
creator = OpenAIBroucherCreator()
broucher = creator.create_broucher(scrapper.scrape(url))
broucher_markdown = markdown.markdown(broucher)
html_template = HtmlMaker().make(broucher_markdown)

# 3. Genera el PDF
HTML(string=html_template).write_pdf('broucher.pdf')
