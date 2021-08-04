from rest_framework.views import APIView
from rest_framework.response import Response
from .coordinator import Coordinator
from rest_framework import status
from rest_framework.exceptions import ValidationError,AuthenticationFailed




class Index(APIView):
    
    """
    [This method will return welcome message]
    """
    def get(self,request):
        return Response('Welcome to Login and Registration App')

class RegisterAPI(APIView):
    
    def post(self,request):
        """[This method will take the required input and register the user]

        Returns:
            [returns the message if successfully registered]
        """
        try:
            data=request.data
            get_data=Coordinator().post_data(data)
            if get_data[0]>0:
                return Response({'message': 'Username is already registered with another user.'}, status=status.HTTP_400_BAD_REQUEST)
            get_inserted_data=Coordinator().post_insert_data(data)
            return Response({"message":"Registration Successfull"})
        except ValueError:
            return Response({"message": 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({'message': 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:
            return Response({"message1": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class LogInAPI(APIView):

    def get(self,request):
        """This method will give the string response as given below."""
        return Response("This is LogInAPI")
        
    def post(self,request):
        """[This method will take the required input and do login]

        Returns:
            [returns the message if successfully loggedin]
        """
        try:
            data=request.data
            username=data.get('username')
            password=data.get('password')
            user_auth=Coordinator().post_login_data(username)
            if username==user_auth['username'] and password==user_auth['password']:
                return Response({"msg": "Loggedin Successfully", 'data' : {'username': data.get('username')}}, status=status.HTTP_200_OK)
            return Response({"msg": 'Wrong username or password'}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({"message": 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({'message': "wrong credentials"}, status=status.HTTP_400_BAD_REQUEST) 
        except AuthenticationFailed:
            return Response({'message': 'Authentication Failed'}, status=status.HTTP_400_BAD_REQUEST) 
        except Exception:
            return Response({"msg1": "wrong credentials"}, status=status.HTTP_400_BAD_REQUEST)