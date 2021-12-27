import requests, json

# Version: 1.2.5

class GeodesignHubClient():
	'''
	This a a Python client that make calls to the Geodesignhub API
	and return data. It requires the requests package and the json module. 

	'''

	def __init__(self, url, token, project_id):
		'''
		Declare your project id, token and the url (optional). 
		'''
		self.project_id = project_id
		self.token = token
		self.securl = url if url else 'https://www.geodesignhub.com/api/v1/'		
		self.session = requests.Session()

	def get_project_id(self):
		''' This method gets all systems for a particular project.  '''
		securl = self.securl+ 'projects'+ '/' + self.project_id + '/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.get(securl, headers=headers)
		return r
	def get_all_systems(self):
		''' This method gets all systems for a particular project.  '''
		securl = self.securl+ 'projects'+ '/' + self.project_id + '/' +'systems' + '/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.get(securl, headers=headers)
		return r

	def get_single_system(self, system_id):
		''' This method gets details  a single system for a particular project.  '''
		securl = self.securl+ 'projects'+ '/' + self.project_id + '/' +'systems' + '/' + str(system_id) +'/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.get(securl, headers=headers)
		return r

	def get_constraints(self):
		''' This method gets the geometry of constraints for a project if available '''
		securl = self.securl+ 'projects'+ '/' + self.project_id + '/' +'constraints' + '/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.get(securl, headers=headers)
		return r

	def get_first_boundaries(self):
		''' Gets the first boundaries if defined for a project '''
		securl = self.securl+ 'projects'+ '/' + self.project_id + '/' +'boundaries' + '/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.get(securl, headers=headers)
		return r

	def get_second_boundaries(self):
		''' Gets the second boundaries if defined for a project.  '''
		securl = self.securl+ 'projects'+ '/' + self.project_id + '/' +'secondboundaries' + '/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.get(securl, headers=headers)
		return r

	def get_project_bounds(self):
		''' Returns a string with bounding box for the project study area coordinates in a 'southwest_lng,southwest_lat,northeast_lng,northeast_lat' format. '''
		securl = self.securl+ 'projects'+ '/' + self.project_id + '/' +'bounds' + '/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.get(securl, headers=headers)
		return r

	def get_all_design_teams(self):
		''' Return all the change teams for that project. '''
		securl = self.securl+ 'projects'+ '/' + self.project_id + '/' +'cteams' + '/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.get(securl, headers=headers)
		return r

	def get_all_details_for_design_team(self, teamid):
		''' Return all the synthesis in the change team.  '''
		assert type(teamid) is int, "Team id is not a integer: %r" % teamid
		securl = self.securl+ 'projects'+ '/' + self.project_id + '/' +'cteams' + '/'+ str(teamid) +'/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.get(securl, headers=headers)
		return r
		
	def get_single_synthesis(self, teamid, synthesisid):
		assert type(teamid) is int, "Team id is not a integer: %r" % teamid
		assert len(synthesisid)  == 16, "Synthesis : %s" % synthesisid
		securl = self.securl + 'projects'+ '/' + self.project_id + '/cteams/'+ str(teamid) +'/' + str(synthesisid) + '/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.get(securl, headers=headers)
		return r

	def get_single_synthesis_diagrams(self, teamid, synthesisid):
		assert type(teamid) is int, "Team id is not a integer: %r" % teamid
		securl = self.securl + 'projects'+ '/' + self.project_id + '/cteams/'+ str(teamid) +'/' + str(synthesisid) + '/diagrams/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.get(securl, headers=headers)
		return r

	def get_synthesis_timeline(self, teamid, synthesisid):
		assert type(teamid) is int, "Team id is not a integer: %r" % teamid
		securl = self.securl + 'projects'+ '/' + self.project_id + '/cteams/'+ str(teamid) +'/' + str(synthesisid) + '/timeline/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.get(securl, headers=headers)
		return r

	def get_synthesis_diagrams(self, teamid, synthesisid):
		assert type(teamid) is int, "Team id is not a integer: %r" % teamid
		securl = self.securl + 'projects'+ '/' + self.project_id + '/cteams/'+ str(teamid) +'/' + str(synthesisid) + '/diagrams/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.get(securl, headers=headers)
		return r

	def get_design_team_members(self, teamid):
		''' Return all the change teams for that project. '''
		assert type(teamid) is int, "Team id is not a integer: %r" % teamid
		securl = self.securl+ 'projects'+ '/' + self.project_id + '/' +'cteams' + '/'+ str(teamid) +'/' +'members' + '/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.get(securl, headers=headers)
		return r

	def get_synthesis_system_projects(self, sysid, teamid, synthesisid):
		assert type(teamid) is int, "Team id is not a integer: %r" % teamid
		assert type(sysid) is int ,"System id is not a integer %r" % sysid
		securl = self.securl + 'projects'+ '/' + self.project_id + '/cteams/'+ str(teamid) +'/' + str(synthesisid) + '/systems/' + str(sysid) + '/projects/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.get(securl, headers=headers)
		return r

	def post_as_diagram(self, geoms, projectorpolicy, featuretype, description, sysid, fundingtype):
		''' Create a self.session object with correct headers and creds. '''
		securl = self.securl+ 'projects'+ '/' + self.project_id + '/' +'systems'+'/'+ str(sysid) + '/'+ 'add' +'/' + projectorpolicy +'/'
		headers = {'Authorization': 'Token '+ self.token, 'content-type': 'application/json'}
		postdata = {'geometry':geoms, 'description':description, 'featuretype':featuretype, 'fundingtype':fundingtype}
		r = self.session.post(securl, headers= headers, data = json.dumps(postdata))
		return r

	def get_single_diagram(self, diagid):
		''' This method gets the geometry of a diagram given a digram id.  '''
		assert type(diagid) is int, "diagram id is not an integer: %r" % id
		securl = self.securl+ 'projects'+ '/' + self.project_id + '/' +'diagrams' + '/'+ str(diagid) +'/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.get(securl, headers=headers)
		return r

	def get_all_diagrams(self):
		''' This method gets the geometry of all diagrams in a project .  '''		
		securl = self.securl+ 'projects'+ '/' + self.project_id + '/' + 'diagrams/all/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.get(securl, headers=headers)
		return r

	def get_diagram_changeid(self, diagid):
		''' Returns the a hash of the last modified date, can be used to see if a diagram has changed from the last time it was accessed. '''
		assert type(diagid) is int, "diagram id is not an integer: %r" % id
		securl = self.securl+ 'projects'+ '/' + self.project_id + '/' +'diagrams' + '/'+ str(diagid) +'/changeid/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.get(securl, headers=headers)
		return r

	def post_as_ealuation_JSON(self, geoms, sysid, username=None):
		''' Create a self.session object with correct headers and creds. '''
		securl = self.securl+ 'projects'+ '/' + self.project_id + '/' +'systems'+'/'+ str(sysid) + '/e/map/json/'
		if username:
			securl += username +'/'
		
		headers = {'Authorization': 'Token '+ self.token, 'content-type': 'application/json'}

		r = self.session.post(securl, headers= headers, data = json.dumps(geoms))
		return r

	def post_as_impact_JSON(self, geoms, sysid, username=None):
		''' Create a self.session object with correct headers and creds. '''
		securl = self.securl+ 'projects'+ '/' + self.project_id + '/' +'systems'+'/'+ str(sysid) + '/i/map/json/'
		if username:
			securl += username +'/'
		headers = {'Authorization': 'Token '+ self.token, 'content-type': 'application/json'}
		r = self.session.post(securl, headers= headers, data = json.dumps(geoms))
		return r

	def post_as_evaluation_GBF(self, geoms, sysid, username=None):
		''' Create a self.session object with correct headers and creds. '''
		securl = self.securl+ 'projects'+ '/' + self.project_id + '/' +'systems'+'/'+ str(sysid) + '/e/map/gbf/'
		if username:
			securl += username +'/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.post(securl, headers= headers, files = {'geoms.gbf':geoms})
		return r

	def post_gdservice_JSON(self, geometry, jobid):
		''' Create a self.session object with correct headers and creds. '''
		securl = self.securl+ 'gdservices/callback/'
		headers = {'Authorization': 'Token '+ self.token, 'content-type': 'application/json'}
		data = {"geometry": geometry, "jobid": jobid}
		r = self.session.post(securl, headers= headers, data = json.dumps(data))
		return r

	def post_as_impact_GBF(self, geoms, sysid, username=None):
		''' Create a self.session object with correct headers and creds. '''
		securl = self.securl+ 'projects'+ '/' + self.project_id + '/' +'systems'+'/'+ str(sysid) + '/i/map/gbf/'
		if username:
			securl += username +'/'
		headers = {'Authorization': 'Token '+ self.token}
		r = self.session.post(securl, headers= headers, files = {'geoms.gbf':geoms})
		return r
