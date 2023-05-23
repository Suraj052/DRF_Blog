
from pickle import FALSE
from blog.models import Post,Category
from rest_framework import viewsets
from .serializers import PostSerializer,CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions

class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only'
    def has_object_permission(self,request,view,obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.author == request.user

class PostList(viewsets.ModelViewSet):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer
    queryset = Post.postobjects.all()

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, title=item)

    # Define Custom Queryset
    def get_queryset(self):
        return Post.objects.all()
    
class CategoryList(viewsets.ModelViewSet):
    permission_classes = [PostUserWritePermission]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_object(self,queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return super().get_object_or_404(Category,name = item)
    
    def get_queryset(self):
        return Category.objects.all()




# class PostDetail(generics.RetrieveUpdateDestroyAPIView,PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all() #Collect the data and filter the data out based on the id
#     serializer_class = PostSerializer
    
#     def get_object(self,queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post,slug=item)




#perform list item and create item
# class PostList(generics.ListCreateAPIView):
#     queryset = Post.postobjects.all() 
#     serializer_class = PostSerializer
#     permission_classes = [DjangoModelPermissions]
    

# class PostDetail(generics.RetrieveUpdateDestroyAPIView,PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all() #Collect the data and filter the data out based on the id
#     serializer_class = PostSerializer #use the same serializer class
 
# 127.0.0..1/api/1 -> Post detail for individual post  


# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)