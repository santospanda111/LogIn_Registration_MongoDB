
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .coordinator import Note_Coordinator
from rest_framework.exceptions import ValidationError

class NotesAPI(APIView):
    

    def get(self, request):
        """This method will read the data from the collection."""
        try:
            data= request.data
            user_note = Note_Coordinator().get_notes(data)
            return Response({"data":user_note}, status=status.HTTP_200_OK)    
        except AssertionError as e:
            return Response({"message":"Put user id to get notes"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """
            :param: title, description and user id as parameter.
            :return: It's return response that notes succcessfully created or not.
        """
        try:
            data=request.data
            id= Note_Coordinator().post_notes(data)
            if id is True:
                return Response({'message': 'Notes created successfully'}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({'message': 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({'message': 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({'message': 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

 
    def put(self,request):
        """This method is used to update the data from the collection by using id as a parameter"""
        try:
            data=request.data
            updated_data=Note_Coordinator().put_data(data)
            if updated_data is True:
                return Response({'msg':'Complete Data Updated'}, status=status.HTTP_200_OK)
        except ValueError:
            return Response({"message": 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({"message": 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        """This method is used to delete the data from the collection by using id as a parameter"""
        try:
            data=request.data
            deleted_data=Note_Coordinator().delete_data(data)
            if deleted_data is True:
                return Response({'msg':'Data Deleted'}, status=status.HTTP_200_OK) 
        except ValueError:
            return Response({"message": 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
