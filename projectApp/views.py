from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('index page is apear...')
    return render(request, 'index.html')
