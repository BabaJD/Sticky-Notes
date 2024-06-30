from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import StickyNote
from .forms import StickyNoteForm
from django.db.models import Q


def note_list(request):
    query = request.GET.get('q')
    sort_by = request.GET.get('sort_by', '-created_at')
    # Default: sort by latest first
    notes = StickyNote.objects.all().order_by(sort_by)

    if query:
        notes = notes.filter(Q(title__icontains=query)
                             | Q(content__icontains=query))

    return render(request, 'notes/note_list.html',
                  {'notes': notes, 'query': query, 'sort_by': sort_by})


def note_create(request):
    if request.method == 'POST':
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.created_at = timezone.now()
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = StickyNoteForm()
    return render(request, 'notes/note_form.html', {'form': form})


def note_detail(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})


def note_update(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    if request.method == 'POST':
        form = StickyNoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()  # Save the updated note object
            return redirect('note_detail', pk=note.pk)
    else:
        form = StickyNoteForm(instance=note)
    return render(request, 'notes/note_form.html',
                  {'form': form, 'note': note})


def note_delete(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})
