from django.http import JsonResponse
from CRM_app.models import Allie, Donation, Investigation_Project, Publication, Meeting, Event
from django.shortcuts import render
from django.views import View
from django.db.models import Count, Sum, F, Q
from django.db.models.functions import TruncMonth
from django.utils import timezone
from datetime import timedelta
from CRM_app.models import Donation
from django.db.models import Sum
from django.db.models.functions import ExtractYear

class AllyReport(View):
    def get(self, request, allie_id):
        query = request.GET.get('q', '').strip()

        try:
            ally = Allie.objects.get(id=allie_id)
            
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
            
            monthly_donation_counts = Donation.objects.filter(allie_id=allie_id).annotate(month=TruncMonth('date')).values('month').annotate(count=Count('month')).order_by('month')

            
                
            for entry in monthly_donation_counts:
                count[months_dict[entry['month'].strftime('%B')]] =  entry['count']
            
            #--------------------------------------
            
            current_year = timezone.now().year
            five_years_ago = current_year - 4

            # Lista para almacenar los nombres de los últimos 5 años
            top_donators_labels = [str(year) for year in range(five_years_ago, current_year + 1)]


            # Inicializa un diccionario para almacenar las sumas de donaciones por año
            donations_per_year = {year: 0 for year in range(five_years_ago, current_year + 1)}

            # Filtra las donaciones del aliado en los últimos 5 años y agrúpalas por año
            donations_by_year = Donation.objects.filter(
                allie_id=allie_id, 
                date__year__gte=five_years_ago
            ).annotate(year=ExtractYear('date')).values('year').annotate(total=Sum('amount'))

            # Rellena el diccionario con los totales obtenidos
            for donation in donations_by_year:
                donations_per_year[donation['year']] = donation['total']

            # Convierte los valores del diccionario en una lista
            total_donations_for_ally_last_5_years = [donations_per_year[year] for year in range(five_years_ago, current_year + 1)]

            #------------------------------------
            
            
            
            meetings_count = Meeting.objects.filter(
                allie_id=allie_id, 
                date__year=current_year
            ).count()

            # Contar los eventos del aliado en el año actual
            events_count = Event.objects.filter(
                eventallie__allie_id=allie_id, 
                date__year=current_year
            ).count()
            
            data_allie_types = [meetings_count,events_count]
            
            #---------------------------------------
            
            investigation_projects_by_month = Investigation_Project.objects.filter(
                allieproject__allie_id=allie_id  # Asumiendo que existe una relación allieproject que conecta con Allie
            ).annotate(month=TruncMonth('start_date')).values('month').annotate(count=Count('month')).order_by('month')

            # Inicializa el conteo de proyectos por mes
            final_count_month = [0] * 12

            # Rellena el conteo de proyectos por mes
            for count_month in investigation_projects_by_month:
                month_index = months_dict[count_month['month'].strftime('%B')]
                final_count_month[month_index] = count_month['count']
                
            #-------------------
            
            publications_by_month = Publication.objects.filter(
                investigation_project_id__allieproject__allie_id=allie_id  # Asumiendo una relación indirecta a través de allieproject
            ).annotate(month=TruncMonth('date')).values('month').annotate(count=Count('id')).order_by('month')

            # Inicializa el conteo de publicaciones por mes
            final_count_month_publication = [0] * 12

            # Rellena el conteo de publicaciones por mes
            for count_month in publications_by_month:
                month_index = months_dict[count_month['month'].strftime('%B')]
                final_count_month_publication[month_index] = count_month['count']
                
            projects = Investigation_Project.objects.filter(allieproject__allie_id=allie_id)

            # Contar los proyectos terminados y no terminados
            finished_projects_count = projects.filter(finish_date__isnull=False).count()
            unfinished_projects_count = projects.filter(finish_date__isnull=True).count()

            investigation_projects_finished_data = [finished_projects_count, unfinished_projects_count]



            projects = Investigation_Project.objects.filter(allieproject__allie_id=allie_id)

            # Anota cada proyecto con el conteo de sus publicaciones y ordena por este número
            projects_ranked_by_publications = projects.annotate(
                total_publications=Count('publication')
            ).order_by('-total_publications')[:3] 

            #total_publications = Publication.objects.filter(investigation_project_id__in=projects).count()
            
            total_publications = Publication.objects.filter(
                investigation_project_id__in=projects
            ).aggregate(total_publications=Count('id'))['total_publications']
            
            top_publications_labels = []
            top_donators = []
            
           

            other_donations = total_publications

            for proyect in projects_ranked_by_publications:
                top_publications_labels.append(proyect.name)
                if proyect.total_publications == None:
                    top_donators.append(0)
                else:
                    top_donators.append(proyect.total_publications)
                    other_donations-= proyect.total_publications
                #print(f'Aliado: {allie.name}, Total de Donaciones: {allie.total_donations}')
            top_publications_labels.append('Otros')
            top_donators.append(other_donations)
            
            print(projects_ranked_by_publications)
                
            return render(request,'allies/single_page_ally_report.html',{'ally': ally,
            'data': count, 
            'top_donators_labels': top_donators_labels,
            'total_donations_for_ally_last_5_years': total_donations_for_ally_last_5_years,
            'data_allie_types': data_allie_types, 
            'data_donators_month': final_count_month, 
            'publications_by_month': final_count_month_publication,
            'investigation_projects_finished': investigation_projects_finished_data, 
              'top_publications_labels': top_publications_labels,
            'top_donators': top_donators, 
            })

        except Allie.DoesNotExist:
            # Si el aliado no existe, redirigir a una página de error o mostrar un mensaje
            return render(request, 'error.html', {'message': 'El aliado no existe o el ID es incorrecto.'})
