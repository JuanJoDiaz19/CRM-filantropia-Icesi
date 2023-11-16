from django.shortcuts import render, redirect
from django.views import View
from CRM_app.models import Event,Comment
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

class FollowUpEvent(View):
    @method_decorator(login_required)
    def get(self, request,follow_up_id):
        return render(request, 'follow_up_event.html',{'id': id})
    
    def post(self, request, follow_up_id):
        descripcion = request.POST.get('descripcion')
        autor = request.POST.get('autor')
        event = get_object_or_404(Event, id=follow_up_id)

        # Crear el comentario
        comment = Comment(event=event, autor=autor, contenido=descripcion)
        comment.save()

        # Redirigir a alguna parte o regresar al formulario con un mensaje
        return redirect(f'/calendar/all')
 