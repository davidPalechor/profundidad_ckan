from django.shortcuts import render
import ckanclient
import json
import ast
import os

# Create your views here.
def index(request):
	out = []
	# Instantiate the CKAN client.
	#ckan = ckanclient.CkanClient(base_location='http://open.alberta.ca/api')
	ckan = ckanclient.CkanClient(base_location='https://datahub.io/api')
	#ckan = ckanclient.CkanClient(base_location='http://opendata.aragon.es/api')
	i = 0
	out = {}
	out['nodes'] = []
	out['links'] = []
	title = []
	org = []

	# Get the package list.
	package_list = ckan.package_register_get()
	for pack in package_list:
		if i < 15:
			ckan.package_entity_get(pack)
			package_entity = ckan.last_message
			if package_entity.has_key('organization'):
			#print True
				title.append(package_entity['title'])
				org.append(package_entity['organization']['title'])
			i+=1
		else:
			break

	for ti in title:
		nodos = ast.literal_eval('{"name":"' + ti.encode('utf-8') + '","group":"uno"}')
		out['nodes'].append(nodos)

	j = 0
	for res in org:
		k = 0
		for lov in org:
			if res == lov:
				links = ast.literal_eval('{"source":' + str(j) + ',"target":' + str(k) + ',"weight":1}')
				out['links'].append(links)
				print res, " ", j, ",", k
			k+=1
		j+=1

	os.getcwd()
	os.path.exists("profundidad_ckan")
	with open('profundidad_ckan'+'/static/profundidad_ckan/data.json','w') as fs:
		json.dump(out, fs)

	return render(request,"index.html", {'out': out['nodes'],'tam':len(package_list)})

	#return render(request, index.html)
