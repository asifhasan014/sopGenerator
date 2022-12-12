from datetime import datetime


from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    # date_str = '2022-11-21 00:00:00:000'
    # date_obj = datetime.strptime(date_str,'%d/%m/%y %H:%M:%S').time()
    # print(date_obj)
    # mylist = ["2022-11-10 00:00:00:000", "2022-11-11 00:00:00:000", "2022-11-12 00:00:00:000"]
    # for x in mylist:
    #     print("Date time formate ...")
    #     print(x)
    # logger.info('index page is apear...')
    return render(request, 'index.html')
