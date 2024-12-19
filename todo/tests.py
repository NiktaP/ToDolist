from django.test import TestCase
from .models import Todo
from django.utils import timezone
# Create your tests here.

class TodoTest(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(
            id=1,
            title="Test Todo",
            description="A test todo",
            is_completed=False,
            due_date=timezone.now() + timezone.timedelta(days=7)
        )

    def test_todo_creation(self):

        todo=Todo.objects.get(pk=1)
        due_date_diff = self.todo.due_date - timezone.now()
        self.assertEqual(todo.title,"Test Todo")
        self.assertEqual(todo.description,"A test todo")
        self.assertEqual(todo.is_completed,False)
        self.assertAlmostEqual(due_date_diff.days, 7, delta=1)
