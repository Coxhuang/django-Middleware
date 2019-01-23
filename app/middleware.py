from django.utils.deprecation import MiddlewareMixin
import datetime

class myMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print("This is process_request : ",datetime.datetime.now())

        return None

    def process_response(self, request, response):
        print("This is process_request : ",datetime.datetime.now())

        return response # 必须要有

    def process_view(self, request, callback, callback_args, callback_kwargs):

        print("This is process_view : ", datetime.datetime.now())

    def process_exception(self, request, exception):

        print("This is process_exception : ", datetime.datetime.now())












        # def process_exception(self, request, exception):
    #     print('M2的process_exception')
    #     print(exception)
    #     return Response({"success":False,"msg":"ok","results":None},status=status.HTTP_400_BAD_REQUEST)

