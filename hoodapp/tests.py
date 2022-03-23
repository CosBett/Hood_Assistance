from django.test import TestCase
from . models import Hood,Profile,Post
from django.contrib.auth.models import User


class TestHood(TestCase):
    def setUp(self):
        
        self.hood = Hood(name = 'Clayworks',location='Kasarani',occupants_count= 150,admin= 'Prime', description = 'This is a test hood description',photo= 'clayworks.png', police_contact = 912, health_contact = 1234)
        self.hood.save()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Hood))
        
    def test_save_hood(self):
        hood = Hood.objects.all()
        self.assertTrue(len(hood)>0)
        
    def test_delete_hood(self):
        hoods = Hood.objects.all().delete()
        self.assertTrue(len(hoods)>0)
        
        
class  TestProfile(TestCase):
    def setUp(self):
        self.user = User(username = 'Prime',email= 'prime@gmail.com', password = 'qwerty123')
        self.user.save()
          
        self.hood = Hood(name = 'Clayworks',location='Kasarani',occupants_count= 150,admin= 'Prime', description = 'This is a test hood description',photo= 'clayworks.png', police_contact = 912, health_contact = 1234)
        self.hood.save()
        
        self.profile = Profile(user=self.user, name='Prime', bio='This is test bio description',profile_picture = 'profile.png', location = 'Kasarani', hood = self.hood)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
        
    def test_save_profile(self):
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
        
    def test_delete_profile(self):
        profile = Profile.objects.all().delete()
        self.assertTrue(len(profile)>0)
        
    def tearDown(self):
        Profile.objects.all().delete()

class TestPost(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Prime')
        self.post = Post.objects.create(id=1, title='Post testing', photo='image.png',hood='clayworks',date='28-03-2022', user='Prime' , description='This is test description')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Post.all_posts()
        self.assertTrue(len(posts) > 0)

    def test_search_post(self):
        self.post.save()
        post = Post.search_project('test')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.search_project('test')
        self.assertTrue(len(post) < 1)