# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import json
from django.http import JsonResponse
import datetime
from django.contrib.auth.models import User
from aar.models import Books,Researchconference,Researchguidence,Researchjournal,Sponsers
from login.models import AarDropdown
from login.views import checkpermission 

def index(request):
	data_values={}
	if 'HTTP_COOKIE' in request.META:
		if request.user.is_authenticated():
			check = checkpermission(request,[337])
			if(check == 200):
				if(request.method=='GET'):
					if request.GET['check']=='JOURNAL':
						if request.GET['check2']=='1':#sending books
							emp_id=request.session['hash1']
							s=Researchjournal.objects.filter(emp_id=emp_id).values('journal_name','isbn','approve_status')
							status=200
							data_values={'data':list(s)}
						if request.GET['check2']=='2':#data of user and other data
							emp_id=request.session['hash1']
							isbn=request.GET['isbn']
							d=AarDropdown.objects.filter(field='RESEARCH PAPER IN JOURNAL').exclude(value=None).values('sno','value')
							a=[]
							for i in d:
								query1=AarDropdown.objects.filter(pid=i['sno']).exclude(value=None).values('sno','value')
								i['value']=i['value'].replace('-','_')
								a.append({i['value'].replace(' ', '_'):list(query1)})
							s=Researchjournal.objects.filter(emp_id=emp_id,isbn=isbn).values('category__value','type_of_journal__value','sub_category__value','published_date','paper_title','impact_factor','journal_name','volume_no','issue_no','isbn','page_no','author','publisher_name','publisher_address','publisher_zip_code','publisher_contact','publisher_email','publisher_website')
							status=200
							data_values={'data1':list(s),'data2':list(a)}
							print data_values

					if request.GET['check']=='CONFERANCE':
						if request.GET['check2']=='1':#sending books
							emp_id=request.session['hash1']
							s=Researchconference.objects.filter(emp_id=emp_id).values('journal_name','isbn','approve_status')
							status=200
							data_values={'data':list(s)}
							# print data_values
						if request.GET['check2']=='2':#data of user and other data
							emp_id=request.session['hash1']
							isbn=request.GET['isbn']
							d=AarDropdown.objects.filter(field='RESEARCH PAPER IN CONFERENCE').exclude(value=None).values('sno','value')
							a=[]
							for i in d:
								query1=AarDropdown.objects.filter(pid=i['sno']).exclude(value=None).values('sno','value')
								i['value']=i['value'].replace('-','_')
								a.append({i['value'].replace(' ', '_'):list(query1)})
							s=Researchconference.objects.filter(emp_id=emp_id,isbn=isbn).values('emp_id','category__value','type_of_conference__value','sub_category__value','conference_title','paper_title','published_date','organized_by','journal_name','volume_no','issue_no','isbn','page_no','author__value','conference_from','conference_to','other_description','publisher_name','publisher_address','publisher_zip_code','publisher_contact','publisher_email','publisher_website')
							status=200
							data_values={'data1':list(s),'data2':list(a)}
							# print data_values
						
					if request.GET['check']=='GUIDANCE':
						if request.GET['check2']=='1':
							emp_id=request.session['hash1']
							d=AarDropdown.objects.filter(field='GUIDANCE').exclude(value=None).values('sno','value')
							data_values={'data':list(d)}
							# print data_values
							status=200
							#return JsonResponse(data_values,safe=False)s
						if request.GET['check2']=='2':
							if request.GET['data']=='66':
								emp_id=request.session['hash1']
								s=Researchguidence.objects.filter(emp_id=emp_id,guidence=request.GET['data']).values('emp_id','guidence__value','project_title','area_of_spec')
								data_values={'data':list(s)}
								print data_values
								status=200
								#return JsonResponse(data_values,safe=False)
							if request.GET['data']=='67':
								emp_id=request.session['hash1']
								s=Researchguidence.objects.filter(emp_id=emp_id,guidence=request.GET['data']).values('emp_id','guidence__value','project_title','area_of_spec')
								data_values={'data':list(s)}
								print data_values
								status=200
								#return JsonResponse(data_values,safe=False)
							if request.GET['data']=='68':
								emp_id=request.session['hash1']
								s=Researchguidence.objects.filter(emp_id=emp_id,guidence=request.GET['data']).values('emp_id','guidence__value','project_title','area_of_spec')
								data_values={'data':list(s)}
								# print data_values
								status=200
						if request.GET['check2']=='3':
							if request.GET['data']=='66':
								emp_id=request.session['hash1']
								a=[]
								sno=AarDropdown.objects.filter(field='RESEARCH GUIDANCE',value='COURSES').exclude(value=None).values('sno')
								s1=AarDropdown.objects.filter(pid=sno).exclude(value=None).values('value','sno')
								s2=Researchguidence.objects.filter(emp_id=emp_id,guidence=request.GET['data']).values('emp_id','guidence__value','course__value','degree__value','no_of_students','degree_awarded','status__value','project_title','area_of_spec')
								data_values={'data1':list(s1),'data2':list(s2)}
								print data_values
								status=200
								#return JsonResponse(data_values,safe=False)
							if request.GET['data']=='67':
								emp_id=request.session['hash1']
								a=[]
								sno=AarDropdown.objects.filter(field='RESEARCH GUIDANCE',value='DEGREE').exclude(value=None).values('sno')
								s1=AarDropdown.objects.filter(pid=sno).exclude(value=None).values('value','sno')
								s2=Researchguidence.objects.filter(emp_id=emp_id,guidence=request.GET['data']).values('emp_id','guidence__value','course__value','degree__value','no_of_students','degree_awarded','status__value','project_title','area_of_spec')
								data_values={'data1':list(s1),'data2':list(s2)}
								print data_values
								status=200
								#return JsonResponse(data_values,safe=False)
							if request.GET['data']=='68':
								emp_id=request.session['hash1']
								# sno=AarDropdown.objects.filter(field='GUIDANCE',value='RESEARCH').exclude(value=None).values('sno')
								s1=AarDropdown.objects.filter(pid=request.GET['data']).exclude(value=None).values('value','sno')
								print s1
								s2=Researchguidence.objects.filter(emp_id=emp_id,guidence=request.GET['data']).values('emp_id','guidence__value','course__value','degree__value','no_of_students','degree_awarded','status__value','project_title','area_of_spec')
								data_values={'data1':list(s1),'data2':list(s2)}
								# print data_values
								status=200
								#return JsonResponse(data_values,safe=False)
					if request.GET['check']=='BOOK':
						if request.GET['check2']=='1':
							emp_id=request.session['hash1']
							s=Books.objects.filter(emp_id=emp_id).values('title','isbn')
							status=200
							data_values={'data':list(s)}
						if request.GET['check2']=='2':
							emp_id=request.session['hash1']
							isbn=request.GET['isbn']
							s=Books.objects.filter(emp_id=emp_id,isbn=isbn).values('emp_id','role__value','role_for__value','publisher_type__value','title','edition','published_date','chapter','isbn','copyright_status','copyright_no','author__value','publisher_name','publisher_address','publisher_zip_code','publisher_contact','publisher_email','publisher_website')
							d=AarDropdown.objects.filter(field='BOOKS').exclude(value=None).values('sno','value')
							a=[]
							for i in d:
								query1=AarDropdown.objects.filter(pid=i['sno']).exclude(value=None).values('sno','value')
								i['value']=i['value'].replace('-','_')
								a.append({i['value'].replace(' ', '_'):list(query1)})
							status=200
							data_values={'data':list(s),'data2':list(a)}
				else:
 					status=502
			else:
				status=403
		else:
			status=401
	else:
		status=500
	return JsonResponse(data_values,safe=False,status=status)

def Update_Guidence(request):
	msg=""
	data=""
	data_values={}
	data=json.loads(request.body.decode("utf-8"))
	print data
	if 'HTTP_COOKIE' in request.META:
		if request.user.is_authenticated():
			check = checkpermission(request,[337])
			if(check == 200):
				if(request.method=='POST'):
					if data is not None:
						course=data['Course']
						degree=data['Degree']
						degree_awarded=data['Degree_awarded']
						guid=data['Guidance']
						no_stud=data['No_of_Students']
						a_o_s=data['area_of_specialization']
						title=data['project_title']
						status=data['status']
						emp_id=request.session["hash1"]
						if guid:
							if(course!=None):
								Researchguidence.objects.filter(guidence=guid,emp_id=emp_id).update(guidence=AarDropdown.objects.get(sno=guid),course=AarDropdown.objects.get(sno=course),degree_awarded=degree_awarded,no_of_students=no_stud,area_of_spec=a_o_s,project_title=title,emp_id=emp_id)
								data_values={"OK":"COURSE Inserted Successfully"}
								
							elif(degree!=None):
								print guid
								Researchguidence.objects.filter(guidence=guid,emp_id=emp_id).update(guidence=AarDropdown.objects.get(sno=guid),degree=AarDropdown.objects.get(sno=degree),degree_awarded=degree_awarded,no_of_students=no_stud,area_of_spec=a_o_s,project_title=title,emp_id=emp_id)
								data_values={"OK":"DEGREE Inserted Successfully"}
								
							elif(status!=None):
								Researchguidence.objects.filter(guidence=guid,emp_id=emp_id).update(guidence=AarDropdown.objects.get(sno=guid),status=AarDropdown.objects.get(sno=status),degree_awarded=degree_awarded,no_of_students=no_stud,area_of_spec=a_o_s,project_title=title,emp_id=emp_id)
								data_values={"OK":"STATUS Inserted Successfully"}
				else:
					status=502
			else:
				status=403
		else:
			status=401
	else:
		status=500
	return JsonResponse(data_values,safe=False,status=200)

def Update_Book(request):
	data_values={}
	if 'HTTP_COOKIE' in request.META:
		if request.user.is_authenticated():
			check = checkpermission(request,[337])
			if(check == 200):
				if(request.method=='POST'):
					data=json.loads(request.body)
					role=data['role']
					for_type=data['for_type']
					publisher=data['publisher']
					copyright_no=data['copyright_no']
					copyright_status=data['copyright_status']
					title=data['title']
					chapter=data['chapter']
					publisher_name=data['publisher_name']
					publisher_add=data['publisher_add']
					edition=data['edition']
					date=data['date']
					publisher_email=data['publisher_email']
					author=data['author']
					publisher_website=data['publisher_website']
					isbn=data['isbn']
					publisher_code=data['publisher_code']
					publisher_contact=data['publisher_contact']
					emp_id=request.session['hash1']
					role_type_new=AarDropdown.objects.get(sno=role)
					for_type_new=AarDropdown.objects.get(sno=for_type)
					publisher_new=AarDropdown.objects.get(sno=publisher)
					author_new=AarDropdown.objects.get(sno=author)

					Books.objects.filter(emp_id=emp_id,isbn=isbn).update(role=role_type_new,role_for=for_type_new,publisher_type=publisher_new,title=title,edition=edition,published_date=date,chapter=chapter,isbn=isbn,copyright_status=copyright_status,copyright_no=copyright_no,author=author_new,publisher_name=publisher_name,publisher_address=publisher_add,publisher_zip_code=publisher_code,publisher_contact=publisher_contact,publisher_email=publisher_email,publisher_website=publisher_website)
					data_values={'msg':"Data Successfully updated"}
					status=200
				else:
					status=502
			else:
				status=403
		else:
			status=401
	else:
		status=500
	return JsonResponse(data_values,status=status)

def Update_Journal(request):
	msg={}
	data=""
	data=json.loads(request.body.decode("utf-8"))
	if 'HTTP_COOKIE' in request.META:
		if request.user.is_authenticated():
			check = checkpermission(request,[337])
			if(check == 200):
				if(request.method=='POST'):	
					data=json.loads(request.body.decode("utf-8"))
					if data!=None:
						category=data["category"]
						emp_id=request.session['hash1']
						type_of_journal=data["typeofjournal"]
						sub_category=data["subcategory"]
						paper_title=data["papertitle"]
						impact_factor=data["impacttext"]
						published_date=data["dateofpub"]
						journal_name=data["journalname"]
						volume_no=data["volumeno"]
						issue_no=data["issueno"]
						isbn=data["isbn"]
						page_no=data["pageno"]
						#author=data["typeofAuthor"]
						author=23
						publisher_name=data["publishername"]
						publisher_address=data["publisheraddL1"]
						publisher_zip_code=data["zipc"]
						publisher_contact=data["phone"]
						publisher_email=data["eml"]
						publisher_website=data["website"]
						others=data["subcatText"]
						c=0
						auth=Researchjournal.objects.filter(isbn=isbn).exclude(emp_id=emp_id).values('author')
						check_auth=AarDropdown.objects.filter(sno=author).values('value')
						print check_auth
						if check_auth[0]["value"]=="FIRST AUTHOR":
							for i in auth:
								is_author1=AarDropdown.objects.filter(sno=i["author"]).values('value')
								if(is_author1[0]["value"]=="FIRST AUTHOR"):
									c=1
									break
						if(c==0):
							Researchjournal.objects.filter(emp_id=emp_id,isbn=isbn).update(category=AarDropdown.objects.get(sno=category),author=AarDropdown.objects.get(sno=author),type_of_journal=AarDropdown.objects.get(sno=type_of_journal),sub_category=AarDropdown.objects.get(sno=sub_category),others=others,paper_title=paper_title,published_date=published_date,impact_factor=impact_factor,journal_name=journal_name,volume_no=volume_no,issue_no=issue_no,isbn=isbn,page_no=page_no,publisher_name=publisher_name,publisher_address=publisher_address,publisher_zip_code=publisher_zip_code,publisher_contact=publisher_contact,publisher_email=publisher_email,publisher_website=publisher_website,emp_id=emp_id)
							data_values={"OK":"DATA updated Successfully"}
						else:
							status=409
							data_values={"OK":"failed"}
				else:
					status=502
			else:
				status=403
		else:
			status=401
	else:
		status=500
	return JsonResponse(data_values,status=200)	

def Update_Conferance(request):
	msg=""
	data=""
	data_values={}
	print request.body
	data=json.loads(request.body.decode("utf-8"))
	print data
	if 'HTTP_COOKIE' in request.META:
		if request.user.is_authenticated():
			check = checkpermission(request,[337])
			if(check == 200):
				if(request.method=='POST'):
					if data!=None:
						category=data["category"]
						emp_id=request.session['hash1']
						type_of_conference=data["type"]
						sub_category=data["subCategory"]
						sponsered=data["sponsered"]
						sponsers=data['sponsers']
						conference_title=data["titleConference"]
						paper_title=data["titlePaper"]
						published_date=data["dateOfPublish"]
						organized_by=data["organised"]
						journal_name=data["journalName"]
						volume_no=data["volume"]
						issue_no=data["issue"]
						isbn=data["issn"]
						page_no=data["page"]
						author=data["author"]
						conference_from=data["fromDate"]
						conference_to=data["toDate"]
						other_description=data["description"]
						publisher_name=data["publisherName"]
						publisher_address=data["publisherAddress"]
						publisher_zip_code=data["publisherPincode"]
						publisher_contact=data["publisherContact"]
						publisher_email=data["publisherEmail"]
						publisher_website=data["publisherWebsite"]
						published_date=data["dateOfPublish"]
						others=data["others"]
						c=0
						auth=Researchconference.objects.filter(isbn=isbn).exclude(emp_id=emp_id).values('author')
						check_auth=AarDropdown.objects.filter(sno=author).values('value')
						print check_auth
						if check_auth[0]["value"]=="FIRST AUTHOR":
							for i in auth:
								is_author1=AarDropdown.objects.filter(sno=i["author"]).values('value')
								if(is_author1[0]["value"]=="FIRST AUTHOR"):
									c=1
									break
						if c==0:
							Researchconference.objects.filter(emp_id=emp_id,isbn=isbn).update(category=AarDropdown.objects.get(sno=category),type_of_conference=AarDropdown.objects.get(sno=type_of_conference),sub_category=AarDropdown.objects.get(sno=sub_category),emp_id=emp_id,sponsered=sponsered,conference_title=conference_title,paper_title=paper_title,published_date=published_date,organized_by=organized_by,journal_name=journal_name,volume_no=volume_no,issue_no=issue_no,isbn=isbn,page_no=page_no,author=AarDropdown.objects.get(sno=author),conference_from=conference_from,conference_to=conference_to,other_description=other_description,publisher_name=publisher_name,publisher_address=publisher_address,publisher_zip_code=publisher_zip_code,publisher_contact=publisher_contact,publisher_email=publisher_email,publisher_website=publisher_website,others=others)
							Sponsers.objects.filter(spons_id=emp_id).delete()
							if(sponsered=="Yes"):
								for i in sponsers:
									Sponsers.objects.create(spons_id=emp_id,sponser_name=i["text"])
							if(sponsered=='No'):
								Sponsers.objects.filter(spons_id=emp_id).delete()
							status=200
							data_values={"OK":200}
						else:
							data_values={"sorry":"Failed"}
							status=409
					else:
						data_values={"data not found":"404"}
						status=404
				else:
					status=502
			else:
				status=403
		else:
			status=401
	else:
		status=500
	print data_values
	return JsonResponse(data_values,safe=False,status=status)
#####################################################################################################################################################################################################################################

def index00(request):
	data_values={}
	if 'HTTP_COOKIE' in request.META:
		if request.user.is_authenticated():
			check = checkpermission(request,[337])
			if(check == 200):
				if(request.method=='GET'):
					if request.GET['check']=='JOURNAL':
						s=AarDropdown.objects.filter(field='RESEARCH PAPER IN JOURNAL').exclude(value=None).values('sno','value')
						a=[]
						for i in s:
							query1=AarDropdown.objects.filter(pid=i['sno']).exclude(value=None).values('sno','value')
							i['value']=i['value'].replace('-','_')
							a.append({i['value'].replace(' ', '_'):list(query1)})
						data_values={'data':list(a)}
						print data_values
						status=200
						#return JsonResponse(data_values,safe=False)

					if request.GET['check']=='CONFERANCE':
						s=AarDropdown.objects.filter(field='RESEARCH PAPER IN CONFERENCE').exclude(value=None).values('sno','value')
						a=[]
						for i in s:
							query1=AarDropdown.objects.filter(pid=i['sno']).exclude(value=None).values('sno','value')
							i['value']=i['value'].replace('-','_')
							a.append({i['value'].replace(' ', '_'):list(query1)})
						data_values={'data':list(a)}
						print data_values
						status=200
						#return JsonResponse(data_values,safe=False)

					if request.GET['check']=='GUIDANCE':
						#print request.GET
						if request.GET['check2']=='false':
							s=AarDropdown.objects.filter(field='RESEARCH GUIDANCE').exclude(value=None).values('sno','value')
							print s
							a=[]
							for i in s:
								query1=AarDropdown.objects.filter(pid=i['sno']).exclude(value=None).values('sno','value')
								i['value']=i['value'].replace('-','_')
								a.append({i['value'].replace(' ', '_'):list(query1)})
							data_values={'data':list(a)}
							status=200
							print data_values
							#return JsonResponse(data_values,safe=False)s
						if request.GET['check2']=='true':
							print request.body
							if request.GET['data']=='66':
								a=[]
								sno=AarDropdown.objects.filter(field='RESEARCH GUIDANCE',value='COURSES').exclude(value=None).values('sno')
								s=AarDropdown.objects.filter(pid=sno).exclude(value=None).values('value','sno')
								data_values=list(s)
								status=200
								#return JsonResponse(data_values,safe=False)
							if request.GET['data']=='67':
								print request.GET
								a=[]
								sno=AarDropdown.objects.filter(field='RESEARCH GUIDANCE',value='DEGREE').exclude(value=None).values('sno')
								s=AarDropdown.objects.filter(pid=sno).exclude(value=None).values('value','sno')
								data_values=list(s)
								status=200
								#return JsonResponse(data_values,safe=False)
							if request.GET['data']=='68':
								a=[]
								sno=AarDropdown.objects.filter(field='GUIDANCE',value='RESEARCH').exclude(value=None).values('sno')
								s=AarDropdown.objects.filter(pid=sno).exclude(value=None).values('value','sno')
								data_values=list(s)
								status=200
							print data_values
							#return JsonResponse(data_values,safe=False)

					if request.GET['check']=='BOOK':
						s=AarDropdown.objects.filter(field='BOOKS').exclude(value=None).values('sno','value')
						a=[]
						for i in s:
							query1=AarDropdown.objects.filter(pid=i['sno']).exclude(value=None).values('sno','value')
							i['value']=i['value'].replace('-','_')
							a.append({i['value'].replace(' ', '_'):list(query1)})
						data_values={'data':list(a)}
						status=200

						#return JsonResponse(data_values,safe=False)
				else:
 					status=502
			else:
				status=403
		else:
			status=401
	else:
		status=500
	return JsonResponse(data_values,safe=False,status=status)

def Book(request):
	data_values={}
	if 'HTTP_COOKIE' in request.META:
		if request.user.is_authenticated():
			check = checkpermission(request,[337])
			if(check == 200):
				if(request.method=='POST'):
					data=json.loads(request.body)
					Emp_id=request.session["hash1"]
					role=data['role']
					for_type=data['for_type']
					publisher=data['publisher']
					copyright_no=data['copyright_no']
					copyright_status=data['copyright_status']
					title=data['title']
					chapter=data['chapter']
					publisher_name=data['publisher_name']
					publisher_add=data['publisher_add']
					edition=data['edition']
					date=data['date']
					publisher_email=data['publisher_email']
					author=data['author']
					publisher_website=data['publisher_website']
					isbn=data['isbn']
					publisher_code=data['publisher_code']
					publisher_contact=data['publisher_contact']
					role_type_new=AarDropdown.objects.get(sno=role)
					for_type_new=AarDropdown.objects.get(sno=for_type)
					publisher_new=AarDropdown.objects.get(sno=publisher)
					author_new=AarDropdown.objects.get(sno=author)
					query=Books.objects.create(emp_id=Emp_id,role=role_type_new,role_for=for_type_new,publisher_type=publisher_new,title=title,edition=edition,published_date=date,chapter=chapter,isbn=isbn,copyright_status=copyright_status,copyright_no=copyright_no,author=author_new,publisher_name=publisher_name,publisher_address=publisher_add,publisher_zip_code=publisher_code,publisher_contact=publisher_contact,publisher_email=publisher_email,publisher_website=publisher_website)           
					msg="Data Successfully Added..."
					data_values={'msg':msg}
					status=200
				else:
					status=502
			else:
				status=403
		else:
			status=401
	else:
		status=500
	return JsonResponse(data_values,status=status)

def R_Conference(request):
	msg=""
	data=""
	data_values={}
	data=json.loads(request.body.decode("utf-8"))
	if 'HTTP_COOKIE' in request.META:
		if request.user.is_authenticated():
			check = checkpermission(request,[337])
			if(check == 200):
				if(request.method=='POST'):
					if data!=None:
						category=data["category"]
						emp_id=request.session["hash1"]
						type_of_conference=data["type"]
						sub_category=data["subCategory"]
						sponsered=data["sponsered"]
						sponsers=data['sponsers']
						conference_title=data["titleConference"]
						paper_title=data["titlePaper"]
						published_date=data["dateOfPublish"]
						organized_by=data["organised"]
						journal_name=data["journalName"]
						volume_no=data["volume"]
						issue_no=data["issue"]
						isbn=data["issn"]
						page_no=data["page"]
						author=data["author"]
						conference_from=data["fromDate"]
						conference_to=data["toDate"]
						other_description=data["description"]
						publisher_name=data["publisherName"]
						publisher_address=data["publisherAddress"]
						publisher_zip_code=data["publisherPincode"]
						publisher_contact=data["publisherContact"]
						publisher_email=data["publisherEmail"]
						publisher_website=data["publisherWebsite"]
						published_date=data["dateOfPublish"]
						others=data["others"]
						dup=Researchconference.objects.filter(isbn=isbn,emp_id=emp_id).values('isbn')
						#print dup[0]["isbn"]
						if(dup[0]["isbn"]!=isbn):
							c=0
							auth=Researchconference.objects.filter(isbn=isbn).values('author')
							check_auth=AarDropdown.objects.filter(sno=author).values('value')
							print check_auth
							if check_auth[0]["value"]=="FIRST AUTHOR":
								for i in auth:
									is_author1=AarDropdown.objects.filter(sno=i["author"]).values('value')
									if(is_author1[0]["value"]=="FIRST AUTHOR"):
										c=1
										break
							if c==0:
								print(type(AarDropdown.objects.get(sno=category)))
								Researchconference.objects.create(category=AarDropdown.objects.get(sno=category),type_of_conference=AarDropdown.objects.get(sno=type_of_conference),sub_category=AarDropdown.objects.get(sno=sub_category),emp_id=emp_id,sponsered=sponsered,conference_title=conference_title,paper_title=paper_title,published_date=published_date,organized_by=organized_by,journal_name=journal_name,volume_no=volume_no,issue_no=issue_no,isbn=isbn,page_no=page_no,author=AarDropdown.objects.get(sno=author),conference_from=conference_from,conference_to=conference_to,other_description=other_description,publisher_name=publisher_name,publisher_address=publisher_address,publisher_zip_code=publisher_zip_code,publisher_contact=publisher_contact,publisher_email=publisher_email,publisher_website=publisher_website,others=others)
								if(sponsered=="Yes"):
									for i in sponsers:
										print i
										Sponsers.objects.create(spons_id=emp_id,sponser_name=i["text"])
								data_values={"OK":"DATA Inserted Successfully"}
								status=200
							else:
								data_values={"sorry":"Failed"}
								status=401
						else:
							data_values={"sorry":"Failed"}
							status=409
					else:
						data_values={"data not found":"404"}
						status=404
				else:
					status=502
			else:
				status=403
		else:
			status=401
	else:
		status=500
	print data_values
	return JsonResponse(data_values,safe=False,status=status)

def R_Guidence(request):
	msg=""
	data=""
	data_values={}
	data=json.loads(request.body.decode("utf-8"))
	if 'HTTP_COOKIE' in request.META:
		if request.user.is_authenticated():
			check = checkpermission(request,[337])
			if(check == 200):
				if(request.method=='POST'):
					if data is not None:
						course=data['Course']
						degree=data['Degree']
						degree_awarded=data['Degree_awarded']
						guid=data['Guidance']
						no_stud=data['No_of_Students']
						a_o_s=data['area_of_specialization']
						title=data['project_title']
						status=data['status']
						emp_id=request.session["hash1"]
						if guid:
							if(course!=None):
								print(guid)
								
								Researchguidence.objects.create(guidence=AarDropdown.objects.get(sno=guid),course=AarDropdown.objects.get(sno=course),degree_awarded=degree_awarded,no_of_students=no_stud,area_of_spec=a_o_s,project_title=title,emp_id=emp_id)
								data_values={"OK":"COURSE Inserted Successfully"}
								
							elif(degree!=None):
								Researchguidence.objects.create(guidence=AarDropdown.objects.get(sno=guid),degree=AarDropdown.objects.get(sno=degree),degree_awarded=degree_awarded,no_of_students=no_stud,area_of_spec=a_o_s,project_title=title,emp_id=emp_id)
								data_values={"OK":"DEGREE Inserted Successfully"}
								
							elif(status!=None):
								Researchguidence.objects.create(guidence=AarDropdown.objects.get(sno=guid),status=AarDropdown.objects.get(sno=status),degree_awarded=degree_awarded,no_of_students=no_stud,area_of_spec=a_o_s,project_title=title,emp_id=emp_id)
								data_values={"OK":"STATUS Inserted Successfully"}
				else:
					status=502
			else:
				status=403
		else:
			status=401
	else:
		status=500
	return JsonResponse(data_values,safe=False,status=200)


def R_journal(request):
	msg={}
	data=""
	data=json.loads(request.body.decode("utf-8"))
	if 'HTTP_COOKIE' in request.META:
		if request.user.is_authenticated():
			check = checkpermission(request,[337])
			if(check == 200):
				if(request.method=='POST'):	
					if data!=None:
						category=data["category"]
						emp_id=requst.session["hash1"]
						type_of_journal=data["typeofjournal"]
						sub_category=data["subcategory"]
						paper_title=data["papertitle"]
						impact_factor=data["impacttext"]
						published_date=data["dateofpub"]
						journal_name=data["journalname"]
						volume_no=data["volumeno"]
						issue_no=data["issueno"]
						isbn=data["isbn"]
						page_no=data["pageno"]
						author=data["typeofAuthor"]
						publisher_name=data["publishername"]
						publisher_address=data["publisheraddL1"]
						publisher_zip_code=data["zipc"]
						publisher_contact=data["phone"]
						publisher_email=data["eml"]
						publisher_website=data["website"]
						others=data["subcatText"]
						if(category!=None):
							c=0
							auth=Researchjournal.objects.filter(isbn=isbn).values('author')
							check_auth=AarDropdown.objects.filter(sno=author).values('value')
							print check_auth
							if check_auth[0]["value"]=="FIRST AUTHOR":
								for i in auth:
									is_author1=AarDropdown.objects.filter(sno=i["author"]).values('value')
									if(is_author1[0]["value"]=="FIRST AUTHOR"):
										c=1
										break
							if(c==0):
								Researchjournal.objects.create(category=AarDropdown.objects.get(sno=category),author=AarDropdown.objects.get(sno=author),type_of_journal=AarDropdown.objects.get(sno=type_of_journal),sub_category=AarDropdown.objects.get(sno=sub_category),others=others,paper_title=paper_title,published_date=published_date,impact_factor=impact_factor,journal_name=journal_name,volume_no=volume_no,issue_no=issue_no,isbn=isbn,page_no=page_no,publisher_name=publisher_name,publisher_address=publisher_address,publisher_zip_code=publisher_zip_code,publisher_contact=publisher_contact,publisher_email=publisher_email,publisher_website=publisher_website,emp_id=emp_id)
								data_values={"OK":"DATA Inserted Successfully"}
								status=200
							else:
								data_values={"OK":"failed"}
				else:
					status=502
			else:
				status=403
		else:
			status=401
	else:
		status=500
	return JsonResponse(data_values,status=200)
