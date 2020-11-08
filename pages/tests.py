from django.test import SimpleTestCase,TestCase
from .models import Post
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
class SimpleTests(SimpleTestCase):
    
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

class PostModelTest(TestCase):
    
    def setUp(self):
        Post.objects.create(text='just a test')
    
    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')        

class HomePageViewTest(TestCase): # new
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='pages',
            email='pages@email.com',
            password='1234'
            )
        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
            )
    def test_string_representation(self):
            post = Post(title='A sample title')
            self.assertEqual(str(post), post.title)

    def test_post_content(self):
            self.assertEqual(f'{self.post.title}', 'A good title')
            self.assertEqual(f'{self.post.author}', 'testuser')
            self.assertEqual(f'{self.post.body}', 'Nice body content')
    def test_post_list_view(self):
            response = self.client.get(reverse('home'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'Nice body content')
            self.assertTemplateUsed(response, 'home.html')
    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')