from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from .mixins import *


class VendorListCreateView(APIView, PaginationHandlerMixin):
    serializer_class = VendorSerializer
    #permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    pagination_class = CustomPagination

    def post(self, request):
        response = {
            "status":False,
            "message":None,
            "data" : []
        }
        status_code = status.HTTP_400_BAD_REQUEST

        if 'name' not in request.data.keys():
            response['message'] = "Vendor name is required."
            return Response(response, status=status_code)

        if 'contact_details' not in request.data.keys():
            response['message'] = "Vendor contact is required."
            return Response(response, status=status_code)

        if 'address' not in request.data.keys():
            response['message'] = "Vendor address is required."
            return Response(response, status=status_code)

        if 'vendor_code' not in request.data.keys():
            response['message'] = "Vendor code is required."
            return Response(response, status=status_code)

        if 'on_time_delivery_rate' not in request.data.keys():
            response['message'] = "On Time Delivery Rate for Vendor is required."
            return Response(response, status=status_code)

        if 'quality_rating_avg' not in request.data.keys():
            response['message'] = "Quality Rating Average for Vendor is required."
            return Response(response, status=status_code)

        if 'average_response_time' not in request.data.keys():
            response['message'] = "Average Response Time for Vendor is required."
            return Response(response, status=status_code)

        if 'fulfillment_rate' not in request.data.keys():
            response['message'] = "Fulfillment Rate for Vendor is required."
            return Response(response, status=status_code)

        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                response['message'] = 'Vendor created successfully.'
                status_code = status.HTTP_201_CREATED
                response['status'] = True
                response['data'] = serializer.data
            else:
                field_errors = []
                for field, errors in serializer.errors.items():
                    field_errors.append({
                        'field': field,
                        'error': errors[0]
                    })
                response['message'] = field_errors
        except Exception as e:
            response['message'] = 'Something went wrong.'
        
        return Response(response, status=status_code)

    def get(self, request):
        status_code = status.HTTP_200_OK
        response = {}
        
        try:
            page = self.paginate_queryset(self.queryset)
            serializer = self.serializer_class(page, many=True, context={"request":request})
            data = self.get_paginated_response(serializer.data)
            response = data.data
            response['count'] = len(response['results'])
            response['total_count'] = self.queryset.count()
        except Exception as e:
            response = {
                "status" : True,
                "message" : 'No data available.',
                "count" : 0,
                "next" : None,
                "previous" : None,
                "result" : []
            }

        return Response(response, status=status_code)


class VendorDetailView(APIView, PaginationHandlerMixin):
    serializer_class = VendorSerializer
    #permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    pagination_class = CustomPagination

    def get(self, request, vendor_id):
        status_code = status.HTTP_200_OK
        response = {}

        try:
            page = self.paginate_queryset(self.queryset.filter(pk=vendor_id))
            serializer = self.serializer_class(page, many=True, context={"request":request})
            data = self.get_paginated_response(serializer.data)
            response = data.data
            response['count'] = len(response['results'])
            response['total_count'] = self.queryset.count()
        except Exception as e:
            response = {
                "status" : True,
                "message" : 'No data available.',
                "count" : 0,
                "next" : None,
                "previous" : None,
                "result" : []
            }

        return Response(response, status=status_code)

    def put(self, request, vendor_id):
        response = {
            "status": False,
            "message": None,
            "data": {}
        }
        status_code = status.HTTP_400_BAD_REQUEST

        vendor = self.get_vendor(vendor_id)
        if vendor:                
            serializer = self.serializer_class(vendor, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response['message'] = 'Vendor updated successfully.'
                status_code = status.HTTP_200_OK
                response['status'] = True
                response['data'] = serializer.data
            else:
                field_errors = []
                for field, errors in serializer.errors.items():
                    field_errors.append({
                        'field': field,
                        'error': errors[0]
                    })
                response['message'] = field_errors
            
            return Response(response, status=status_code)
        else:
            response['message'] = 'Vendor not found.'
            response['status'] = False

            return Response(response, status=status_code)

    def delete(self, request, vendor_id):
        response = {
            "status": False,
            "message": None,
            "data": {}
        }
        status_code = status.HTTP_400_BAD_REQUEST
        
        vendor = self.get_vendor(vendor_id)
        if vendor:
            vendor.delete()
            response['message'] = 'Vendor deleted successfully.'
            status_code = status.HTTP_200_OK
            response['status'] = True
        
            return Response(response, status=status_code)
        else:
            response['message'] = 'Vendor not found.'
            response['status'] = False

            return Response(response, status=status_code)

    def get_vendor(self, vendor_id):
        try:
            return self.queryset.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            self.response['message'] = "Vendor not found."
            return Response(self.response, status=status.HTTP_404_NOT_FOUND)


class PurchaseOrdersListCreateView(APIView, PaginationHandlerMixin):
    serializer_class = PurchaseOrderSerializer
    #permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    pagination_class = CustomPagination

    def post(self, request):
        response = {
            "status":False,
            "message":None,
            "data" : []
        }
        status_code = status.HTTP_400_BAD_REQUEST

        if 'po_number' not in request.data.keys():
            response['message'] = "Purchase Number is required."
            return Response(response, status=status_code)

        if 'vendor' not in request.data.keys():
            response['message'] = "Vendor is required."
            return Response(response, status=status_code)

        if 'order_date' not in request.data.keys():
            response['message'] = "Order Date is required."
            return Response(response, status=status_code)

        if 'delivery_date' not in request.data.keys():
            response['message'] = "Delivery Date is required."
            return Response(response, status=status_code)

        if 'items' not in request.data.keys():
            response['message'] = "Items are required."
            return Response(response, status=status_code)

        if 'quantity' not in request.data.keys():
            response['message'] = "Quantity is required."
            return Response(response, status=status_code)

        if 'status' not in request.data.keys():
            response['message'] = "Status is required."
            return Response(response, status=status_code)

        if 'quality_rating' not in request.data.keys():
            response['message'] = "Quality Rating is required."
            return Response(response, status=status_code)

        if 'issue_date' not in request.data.keys():
            response['message'] = "Issue Date is required."
            return Response(response, status=status_code)

        if 'acknowledgment_date' not in request.data.keys():
            response['message'] = "Acknowledgement Date is required."
            return Response(response, status=status_code)

        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                response['message'] = 'Purchase Order created successfully.'
                status_code = status.HTTP_201_CREATED
                response['status'] = True
                response['data'] = serializer.data
            else:
                field_errors = []
                for field, errors in serializer.errors.items():
                    field_errors.append({
                        'field': field,
                        'error': errors[0]
                    })
                response['message'] = field_errors
        except Exception as e:
            response['message'] = 'Something went wrong.'
        
        return Response(response, status=status_code)

    def get(self, request):
        status_code = status.HTTP_200_OK
        response = {}
        
        try:
            page = self.paginate_queryset(self.queryset)
            serializer = self.serializer_class(page, many=True, context={"request":request})
            data = self.get_paginated_response(serializer.data)
            response = data.data
            response['count'] = len(response['results'])
            response['total_count'] = self.queryset.count()
        except Exception as e:
            response = {
                "status" : True,
                "message" : 'No data available.',
                "count" : 0,
                "next" : None,
                "previous" : None,
                "result" : []
            }

        return Response(response, status=status_code)


class PurchaseOrdersView(APIView, PaginationHandlerMixin):
    serializer_class = PurchaseOrderSerializer
    #permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    pagination_class = CustomPagination

    def get(self, request, po_id):
        status_code = status.HTTP_200_OK
        response = {}

        try:
            page = self.paginate_queryset(self.queryset.filter(pk=po_id))
            serializer = self.serializer_class(page, many=True, context={"request":request})
            data = self.get_paginated_response(serializer.data)
            response = data.data
            response['count'] = len(response['results'])
            response['total_count'] = self.queryset.count()
        except Exception as e:
            response = {
                "status" : True,
                "message" : 'No data available.',
                "count" : 0,
                "next" : None,
                "previous" : None,
                "result" : []
            }

        return Response(response, status=status_code)

    def put(self, request, po_id):
        response = {
            "status": False,
            "message": None,
            "data": {}
        }
        status_code = status.HTTP_400_BAD_REQUEST

        purchase_order = self.get_purchase_order(po_id)
        if purchase_order:                
            serializer = self.serializer_class(purchase_order, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response['message'] = 'Purchase Order updated successfully.'
                status_code = status.HTTP_200_OK
                response['status'] = True
                response['data'] = serializer.data
            else:
                field_errors = []
                for field, errors in serializer.errors.items():
                    field_errors.append({
                        'field': field,
                        'error': errors[0]
                    })
                response['message'] = field_errors
            
            return Response(response, status=status_code)
        else:
            response['message'] = 'Purchase Order not found.'
            response['status'] = False

            return Response(response, status=status_code)

    def delete(self, request, po_id):
        response = {
            "status": False,
            "message": None,
            "data": {}
        }
        status_code = status.HTTP_400_BAD_REQUEST
        
        purchase_order = self.get_purchase_order(po_id)
        if purchase_order:
            purchase_order.delete()
            response['message'] = 'Purchase Order deleted successfully.'
            status_code = status.HTTP_200_OK
            response['status'] = True
        
            return Response(response, status=status_code)
        else:
            response['message'] = 'Purchase Order not found.'
            response['status'] = False

            return Response(response, status=status_code)

    def get_purchase_order(self, po_id):
        try:
            return self.queryset.get(pk=po_id)
        except PurchaseOrder.DoesNotExist:
            self.response['message'] = "Purchase Order not found."
            return Response(self.response, status=status.HTTP_404_NOT_FOUND)

