import requests
import json

# Version: 1.4.0


class GeodesignHubClient:
    """
    This a a Python client that make calls to the Geodesignhub API
    and return data. It requires the requests package and the json module.

    """

    def __init__(self, token: str, url: str = None, project_id: str = None):
        """
        Declare your project id, token and the url (optional).
        """
        self.project_id = project_id
        self.token = token
        self.sec_url = url if url else "https://www.geodesignhub.com/api/v1/"
        self.session = requests.Session()
        headers = {"Authorization": "Token " + self.token}
        self.session.headers = headers

    def get_project_id(self):
        """This method gets all systems for a particular project."""
        sec_url = self.sec_url + "projects" + "/" + self.project_id + "/"
        r = self.session.get(sec_url)
        return r

    def get_all_systems(self):
        """This method gets all systems for a particular project."""
        sec_url = (
            self.sec_url + "projects" + "/" + self.project_id + "/" + "systems" + "/"
        )
        r = self.session.get(sec_url)
        return r

    def get_project_center(self):
        """This method gets the center as lat,lng for a particular project."""
        sec_url = (
            self.sec_url + "projects" + "/" + self.project_id + "/" + "center" + "/"
        )
        r = self.session.get(sec_url)
        return r

    def get_single_system(self, system_id: int):
        """This method gets details  a single system for a particular project."""
        sec_url = (
            self.sec_url
            + "projects"
            + "/"
            + self.project_id
            + "/"
            + "systems"
            + "/"
            + str(system_id)
            + "/"
        )
        r = self.session.get(sec_url)
        return r

    def get_constraints(self):
        """This method gets the geometry of constraints for a project if available"""
        sec_url = (
            self.sec_url
            + "projects"
            + "/"
            + self.project_id
            + "/"
            + "constraints"
            + "/"
        )
        r = self.session.get(sec_url)
        return r

    def get_first_boundaries(self):
        """Gets the first boundaries if defined for a project"""
        sec_url = (
            self.sec_url + "projects" + "/" + self.project_id + "/" + "boundaries" + "/"
        )
        r = self.session.get(sec_url)
        return r

    def get_second_boundaries(self):
        """Gets the second boundaries if defined for a project."""
        sec_url = (
            self.sec_url
            + "projects"
            + "/"
            + self.project_id
            + "/"
            + "secondboundaries"
            + "/"
        )
        r = self.session.get(sec_url)
        return r

    def get_project_bounds(self):
        """Returns a string with bounding box for the project study area coordinates in a 'southwest_lng,southwest_lat,northeast_lng,northeast_lat' format."""
        sec_url = (
            self.sec_url + "projects" + "/" + self.project_id + "/" + "bounds" + "/"
        )
        r = self.session.get(sec_url)
        return r

    def get_project_tags(self):
        """Returns a list of tags created in the project."""
        sec_url = self.sec_url + "projects" + "/" + self.project_id + "/" + "tags" + "/"
        r = self.session.get(sec_url)
        return r

    def get_all_design_teams(self):
        """Return all the change teams for that project."""
        sec_url = (
            self.sec_url + "projects" + "/" + self.project_id + "/" + "cteams" + "/"
        )
        r = self.session.get(sec_url)
        return r

    def get_single_synthesis(self, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), "Team id is not a integer: %r" % teamid
        assert len(synthesisid) == 16, "Synthesis : %s" % synthesisid
        sec_url = (
            self.sec_url
            + "projects"
            + "/"
            + self.project_id
            + "/cteams/"
            + str(teamid)
            + "/"
            + str(synthesisid)
            + "/"
        )
        r = self.session.get(sec_url)
        return r

    def get_single_synthesis_details(self, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), "Team id is not a integer: %r" % teamid
        assert len(synthesisid) == 16, "Synthesis : %s" % synthesisid
        sec_url = (
            self.sec_url
            + "projects"
            + "/"
            + self.project_id
            + "/cteams/"
            + str(teamid)
            + "/"
            + str(synthesisid)
            + "/details/"
        )
        r = self.session.get(sec_url)
        return r

    def get_single_synthesis_esri_json(self, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), "Team id is not a integer: %r" % teamid
        assert len(synthesisid) == 16, "Synthesis : %s" % synthesisid
        sec_url = (
            self.sec_url
            + "projects"
            + "/"
            + self.project_id
            + "/cteams/"
            + str(teamid)
            + "/"
            + str(synthesisid)
            + "/esri/"
        )
        r = self.session.get(sec_url)
        return r

    def get_single_synthesis_diagrams(self, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), "Team id is not a integer: %r" % teamid
        sec_url = (
            self.sec_url
            + "projects"
            + "/"
            + self.project_id
            + "/cteams/"
            + str(teamid)
            + "/"
            + str(synthesisid)
            + "/diagrams/"
        )
        r = self.session.get(sec_url)
        return r

    def get_synthesis_timeline(self, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), "Team id is not a integer: %r" % teamid
        sec_url = (
            self.sec_url
            + "projects"
            + "/"
            + self.project_id
            + "/cteams/"
            + str(teamid)
            + "/"
            + str(synthesisid)
            + "/timeline/"
        )
        r = self.session.get(sec_url)
        return r

    def get_synthesis_diagrams(self, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), "Team id is not a integer: %r" % teamid
        sec_url = (
            self.sec_url
            + "projects"
            + "/"
            + self.project_id
            + "/cteams/"
            + str(teamid)
            + "/"
            + str(synthesisid)
            + "/diagrams/"
        )
        r = self.session.get(sec_url)
        return r

    def get_design_team_members(self, teamid: int):
        """Return all the change teams for that project."""
        assert isinstance(teamid, int), "Team id is not a integer: %r" % teamid
        sec_url = (
            self.sec_url
            + "projects"
            + "/"
            + self.project_id
            + "/"
            + "cteams"
            + "/"
            + str(teamid)
            + "/"
            + "members"
            + "/"
        )
        r = self.session.get(sec_url)
        return r

    def get_synthesis_system_projects(self, sysid: int, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), "Team id is not a integer: %r" % teamid
        assert isinstance(sysid, int), "System id is not a integer %r" % sysid
        sec_url = (
            self.sec_url
            + "projects"
            + "/"
            + self.project_id
            + "/cteams/"
            + str(teamid)
            + "/"
            + str(synthesisid)
            + "/systems/"
            + str(sysid)
            + "/projects/"
        )
        r = self.session.get(sec_url)
        return r

    def post_as_diagram(
        self,
        geoms,
        projectorpolicy: str,
        featuretype: str,
        description: str,
        sysid: str,
        fundingtype: str,
    ):
        """Create a self.session object with correct headers and creds."""
        sec_url = (
            self.sec_url
            + "projects"
            + "/"
            + self.project_id
            + "/"
            + "systems"
            + "/"
            + str(sysid)
            + "/"
            + "add"
            + "/"
            + projectorpolicy
            + "/"
        )

        postdata = {
            "geometry": geoms,
            "description": description,
            "featuretype": featuretype,
            "fundingtype": fundingtype,
        }
        r = self.session.post(sec_url, data=json.dumps(postdata))
        return r

    def post_as_diagram_with_external_geometries(
        self,
        url: str,
        layer_type: str,
        projectorpolicy: str,
        featuretype: str,
        description: str,
        sysid: str,
        fundingtype: str,
    ):
        """Create a self.session object with correct headers and creds."""
        securl = (
            self.securl
            + "projects"
            + "/"
            + self.project_id
            + "/"
            + "systems"
            + "/"
            + str(sysid)
            + "/"
            + "add/external/"
            + projectorpolicy
            + "/"
        )

        postdata = {
            "url ": url,
            "description": description,
            "layer_type": layer_type,
            "featuretype": featuretype,
            "fundingtype": fundingtype,
        }
        r = self.session.post(securl, data=json.dumps(postdata))
        return r

    def get_single_diagram(self, diagid: int):
        """This method gets the geometry of a diagram given a digram id."""
        assert isinstance(diagid, int), "diagram id is not an integer: %r" % id
        sec_url = (
            self.sec_url
            + "projects"
            + "/"
            + self.project_id
            + "/"
            + "diagrams"
            + "/"
            + str(diagid)
            + "/"
        )
        r = self.session.get(sec_url)
        return r

    def get_all_diagrams(self):
        """This method gets the geometry of all diagrams in a project ."""
        sec_url = (
            self.sec_url + "projects" + "/" + self.project_id + "/" + "diagrams/all/"
        )
        r = self.session.get(sec_url)
        return r

    def get_diagram_changeid(self, diagid: int):
        """Returns the a hash of the last modified date, can be used to see if a diagram has changed from the last time it was accessed."""
        assert isinstance(diagid, int), "diagram id is not an integer: %r" % id
        sec_url = (
            self.sec_url
            + "projects"
            + "/"
            + self.project_id
            + "/"
            + "diagrams"
            + "/"
            + str(diagid)
            + "/changeid/"
        )
        r = self.session.get(sec_url)
        return r

    def post_as_ealuation_JSON(self, geoms, sysid: int, username: str = None):
        """Create a self.session object with correct headers and creds."""
        sec_url = (
            self.sec_url
            + "projects"
            + "/"
            + self.project_id
            + "/"
            + "systems"
            + "/"
            + str(sysid)
            + "/e/map/json/"
        )
        if username:
            sec_url += username + "/"

        r = self.session.post(sec_url, data=json.dumps(geoms))
        return r

    def add_project_tags(self, tag_ids):
        """Add tags to a project"""
        sec_url = self.sec_url + "projects" + "/" + self.project_id + "/" + "tags" + "/"

        r = self.session.post(sec_url, data=json.dumps(tag_ids))
        return r

    def get_project_plugins(self):
        """Get plugins for a project"""
        sec_url = (
            self.sec_url + "projects" + "/" + self.project_id + "/" + "plugins" + "/"
        )

        r = self.session.get(sec_url)
        return r

    def add_plugins_to_project(self, tag_ids):
        """Add tags to a project"""
        sec_url = (
            self.sec_url + "projects" + "/" + self.project_id + "/" + "plugins" + "/"
        )

        r = self.session.post(sec_url, data=json.dumps(tag_ids))
        return r

    def create_diagram_groups(self, diagram_groups_payload):
        """Create multiple diagram groups"""
        sec_url = self.sec_url + "projects" + "/" + self.project_id + "/diagrams/groups/"
        r = self.session.post(sec_url, data=json.dumps(diagram_groups_payload))
        return r

    def post_as_impact_JSON(self, geoms, sysid: int, username: str = None):
        """Create a self.session object with correct headers and creds."""
        sec_url = (
            self.sec_url
            + "projects"
            + "/"
            + self.project_id
            + "/"
            + "systems"
            + "/"
            + str(sysid)
            + "/i/map/json/"
        )
        if username:
            sec_url += username + "/"

        r = self.session.post(sec_url, data=json.dumps(geoms))
        return r

    def post_as_evaluation_GBF(self, geoms, sysid: int, username: str = None):
        """Create a self.session object with correct headers and creds."""
        sec_url = (
            self.sec_url
            + "projects"
            + "/"
            + self.project_id
            + "/"
            + "systems"
            + "/"
            + str(sysid)
            + "/e/map/gbf/"
        )
        if username:
            sec_url += username + "/"
        r = self.session.post(sec_url, files={"geoms.gbf": geoms})
        return r

    def post_gdservice_JSON(self, geometry, jobid: str):
        """Create a self.session object with correct headers and creds."""
        sec_url = self.sec_url + "gdservices/callback/"

        data = {"geometry": geometry, "jobid": jobid}
        r = self.session.post(sec_url, data=json.dumps(data))
        return r

    def post_as_impact_GBF(self, geoms, sysid: int, username: str = None):
        """Create a self.session object with correct headers and creds."""
        sec_url = (
            self.sec_url
            + "projects"
            + "/"
            + self.project_id
            + "/"
            + "systems"
            + "/"
            + str(sysid)
            + "/i/map/gbf/"
        )
        if username:
            sec_url += username + "/"
        r = self.session.post(sec_url, files={"geoms.gbf": geoms})
        return r

    def create_new_project(self, project_create_payload):
        """Create a self.session object with correct headers and creds."""
        sec_url = self.sec_url + "projects/create/"

        r = self.session.post(sec_url, data=json.dumps(project_create_payload))
        return r

    def create_new_igc_project(self, project_create_payload):
        """Create a self.session object with correct headers and creds."""
        sec_url = self.sec_url + "projects/create-igc-project/"

        r = self.session.post(sec_url, data=json.dumps(project_create_payload))
        return r
