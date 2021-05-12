from django.test import TestCase

from .models import Todo


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='first todo', description='first todo body')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        self.assertEqual(todo.title, 'first todo')

    def test_description_content(self):
        todo = Todo.objects.get(id=1)
        self.assertEqual(todo.description, 'first todo body')
