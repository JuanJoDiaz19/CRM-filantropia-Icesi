from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from CRM_app.models import Donation, Allie, Investigation_Project
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.db.models import Sum, F


class Reports(View):

    def get(self, request):

        # Donations through the year graph -------------------------------------------------------

        months_dict = {
            'January': 0,
            'February': 1,
            'March': 2,
            'April': 3,
            'May': 4,
            'June': 5,
            'July': 6,
            'August': 7,
            'September': 8,
            'October': 9,
            'November': 10,
            'December': 11
        }

        count = [0,0,0,0,0,0,0,0,0,0,0,0]
        # Create a queryset that groups donations by month and counts the occurrences
        monthly_donation_counts = Donation.objects.annotate(month=TruncMonth('date')).values('month').annotate(count=Count('month')).order_by('month')

        # Iterate through the results and append the counts to the list
        for entry in monthly_donation_counts:
            count[months_dict[entry['month'].strftime('%B')]] =  entry['count']

        # Top donators -------------------------------------------------------------------------------

        top_donators_query = Allie.objects.annotate(total_donations=Sum('donation__amount')).order_by('-total_donations')[:3]
        total_donations = Donation.objects.aggregate(total_donations = Sum('amount'))

        # Puedes acceder al nombre del aliado y la suma de las donaciones de la siguiente manera
        top_donators_labels = []
        top_donators = []

        other_donations = total_donations['total_donations']

        for allie in top_donators_query:
            top_donators_labels.append(allie.name)
            if allie.total_donations == None:
                top_donators.append(0)
            else:
                top_donators.append(allie.total_donations)
                other_donations-= allie.total_donations
            #print(f'Aliado: {allie.name}, Total de Donaciones: {allie.total_donations}')
        top_donators_labels.append('Otros')
        top_donators.append(other_donations)

        
        # Types of donations -------------------------------------------------------------------------------
        aliados_por_area = Allie.objects.values('area_id__area_description') \
                               .annotate(total_aliados=Count('id'))
        

        area_donators_labels = []
        area_donators_data = []
        # The result is a queryset with the area descriptions and the corresponding counts.
        for area in aliados_por_area:
            area_donators_labels.append(area['area_id__area_description'])
            area_donators_data.append(area['total_aliados'])

        # Investigation projcts active - Finished

        
        # Proyectos con fecha de finalización igual a None
        proyectos_sin_fecha_de_finalizacion = Investigation_Project.objects.filter(finish_date__isnull=True)

        # Proyectos con fecha de finalización diferente de None
        proyectos_con_fecha_de_finalizacion = Investigation_Project.objects.exclude(finish_date__isnull=True)

        # Obtener el recuento de proyectos para cada categoría
        count_proyectos_sin_fecha = proyectos_sin_fecha_de_finalizacion.count()
        count_proyectos_con_fecha = proyectos_con_fecha_de_finalizacion.count()

        investigation_projects_finished_data = []
        investigation_projects_finished_data.append(count_proyectos_con_fecha)
        investigation_projects_finished_data.append(count_proyectos_sin_fecha)


        # Investigation projects through the year:

         # Create a queryset that groups donations by month and counts the occurrences
        investigation_projects_by_month = Investigation_Project.objects.annotate(month=TruncMonth('start_date')).values('month').annotate(count=Count('month')).order_by('month')
        final_count_motnth = [0,0,0,0,0,0,0,0,0,0,0,0]

        for count_month in investigation_projects_by_month: 
            final_count_motnth[months_dict[count_month['month'].strftime('%B')]] =  count_month['count']

        
        print(final_count_motnth)



        return render(request, 'reports.html', {
            'data': count, 
            'top_donators_labels': top_donators_labels,
            'top_donators': top_donators, 
            'area_donators_labels': area_donators_labels,
            'area_donators_data': area_donators_data, 
            'investigation_projects_finished': investigation_projects_finished_data 
            })