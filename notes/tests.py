from django.test import TestCase
from django.urls import reverse
from .models import StickyNote, Tag
from .forms import StickyNoteForm
from django.contrib.auth.models import User


class StickyNoteModelTest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name="Work")
        self.tag2 = Tag.objects.create(name="Important")
        self.note = StickyNote.objects.create(
            title="Test Note", content="This is a test note.",
            background_color="#FFFF00"
        )
        self.note.tags.add(self.tag1, self.tag2)

    def test_sticky_note_creation(self):
        self.assertTrue(isinstance(self.note, StickyNote))
        self.assertEqual(str(self.note), "Test Note")
        self.assertEqual(self.note.background_color, "#FFFF00")

    def test_tag_creation(self):
        self.assertTrue(isinstance(self.tag1, Tag))
        self.assertEqual(str(self.tag1), "Work")

    def test_sticky_note_tags(self):
        self.assertIn(self.tag1, self.note.tags.all())
        self.assertIn(self.tag2, self.note.tags.all())


class StickyNoteViewTest(TestCase):

    def setUp(self):
        self.tag1 = Tag.objects.create(name="Work")
        self.tag2 = Tag.objects.create(name="Important")
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        # Login the user
        self.note = StickyNote.objects.create(
            title="Test Note", content="This is a test note.",
            background_color="#FFFF00"
        )
        self.note.tags.add(self.tag1, self.tag2)

    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_list.html')
        self.assertContains(response, "Test Note")

    def test_note_detail_view(self):
        response = self.client.get(reverse('note_detail', args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_detail.html')
        self.assertContains(response, "Test Note")
        self.assertContains(response, "This is a test note.")

    def test_note_create_view(self):
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'This is a new note.',
            'background_color': '#00FF00'
        })
        self.assertEqual(response.status_code, 302)
        # Redirect after successful creation
        self.assertRedirects(response, reverse('note_detail', args=[2]))
        # Assuming this is the second note
        self.assertEqual(StickyNote.objects.count(), 2)

    def test_note_update_view(self):
        response = self.client.post(reverse('note_update',
                                            args=[self.note.pk]), {
            'title': 'Updated Note',
            'content': 'This note has been updated.',
            'background_color': '#0000FF'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('note_detail',
                                               args=[self.note.pk]))
        updated_note = StickyNote.objects.get(pk=self.note.pk)
        self.assertEqual(updated_note.title, 'Updated Note')
        self.assertEqual(updated_note.background_color, '#FFFF00')

    def test_note_delete_view(self):
        response = self.client.post(reverse('note_delete',
                                            args=[self.note.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('note_list'))
        self.assertEqual(StickyNote.objects.count(), 0)


class StickyNoteFormTest(TestCase):
    def test_valid_form(self):
        data = {'title': "New Note", 'content': "Some content",
                'background_color': "#FF0000"}
        form = StickyNoteForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'title': "", 'content': "Some content"}
        # Missing background color
        form = StickyNoteForm(data=data)
        self.assertFalse(form.is_valid())
