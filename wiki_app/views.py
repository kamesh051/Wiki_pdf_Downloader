from django.shortcuts import render
from django.http import HttpResponse
from .requestapi import WikiApi
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
import json

def home_page(request):
	''' home_page method renders template '''

	return render(request,'wiki_app/home.html')


def search_view(request):
	'''search_view method process the user search item and process
	the corresponing search keywords'''
	search_data = request.GET['search_word']
	loaded_data = wiki.process_request(search_data)
	json_data = json.dumps(loaded_data)
	return render(request,'wiki_app/home.html',{'json_data':json_data})

def get_article(request):

    """In this method searchword summarized and converted to pdf format"""

    article = request.GET['article']
    print(article)
    try:
        page = wiki.get_article(article)
        if page is not None:
            context = {
                'title': article,
                'content': page.content
            }
            pdf = render_to_pdf('wiki_app/content.html', context)
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = '{}-wiki.pdf'.format(article)
            content = "attachment; filename={}".format(filename)
            response['Content-Disposition'] = content
            return response
        else:
            return HttpResponse('Please provide an valid name get wiki data')
    except ConnectionError:
        return HttpResponse('Please check the connectivity')

def render_to_pdf(template, context={}):
    """

    This method is based on xhtml2pdf package and
    returns a pdf from a supplied html document.

    """
    template = get_template(template)
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(html, result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

wiki = WikiApi()