from __future__ import unicode_literals
# -*- coding: utf-8 -*-


from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


from models import Entry
from forms import EntryForm, PictureFormSet


class EntryListView(ListView):
    """
    View for create Entry List
    """
    model = Entry
    template_name = 'entry/entry_list.html'
    context_object_name = 'entry_list'
    paginate_by = 3

    def get_queryset(self):
        return Entry.objects.filter(owner=self.request.user)


class EntryCreateView(CreateView):
    """
    View for create Entry
    """
    model = Entry
    form_class = EntryForm
    template_name = 'entry/entry_form.html'
    success_url = reverse_lazy('entry_add')

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        picture_form = PictureFormSet()
        return self.render_to_response(
            self.get_context_data(form=form, picture_form=picture_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        picture_form = PictureFormSet(request.POST, request.FILES)
        if form.is_valid() and picture_form.is_valid():
            return self.form_valid(form, picture_form)
        else:
            return self.form_invalid(form, picture_form)

    def form_valid(self, form, picture_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.instance
        form.instance.owner = self.request.user
        form.instance.save()
        picture_form.instance = self.object
        picture_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, picture_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, picture_form=picture_form))


class EntryUpdateView(UpdateView):
    """
    View for create Entry
    """

    model = Entry
    form_class = EntryForm
    success_url = reverse_lazy('entry_list')


    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = self.get_object()  # return self object
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        picture_form = PictureFormSet(instance=self.object)
        return self.render_to_response(
            self.get_context_data(form=form, picture_form=picture_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        picture_form = PictureFormSet(request.POST, request.FILES, instance=self.object)
        if form.is_valid() and picture_form.is_valid():
            return self.form_valid(form, picture_form)
        else:
            return self.form_invalid(form, picture_form)

    def form_valid(self, form, picture_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """

        # self.object = form.save(commit=False)
        # self.object.user = self.request.user
        # self.object.save()

        self.object = form.instance
        form.instance.owner = self.request.user
        form.instance.save()
        picture_form.instance = self.object
        picture_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, picture_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  picture_form=picture_form))


class EntryDeleteView(DeleteView):
    model = Entry
    template_name = 'entry/entry_confirm_delete.html'
    success_url = reverse_lazy('entry_list')