from functools import wraps
import requests
import json
from urllib.parse import urljoin, urlparse, ParseResult
from os.path import join
from typing import Optional, Dict, Any


class GeodesignHubClient:
    """
    This is a Python client that makes calls to the Geodesignhub API.
    """

    project_id: str
    token: str
    sec_url: ParseResult
    session: requests.Session

    def __init__(self, token: str, url: Optional[str] = None, project_id: str = ""):
        """
        Declare your project id, token and the url (optional).
        """
        assert project_id, "Project id is required"
        self.project_id = project_id
        self.token = token
        self.sec_url = urlparse(url or "https://www.geodesignhub.com/api/v1/")
        self.session = requests.Session()
        headers = {"Authorization": "Token " + self.token}
        self.session.headers.update(headers)

    @wraps(requests.Session.request)
    def _request(self, *args, **kwargs):
        """
        Make a request to the Geodesignhub API
        """
        method, url = args[:2]
        joined_url = urljoin(self.sec_url.geturl(), url)
        return self.session.request(method, joined_url, *args[2:], **kwargs)

    def get_project_details(self):
        """This method gets all systems for a particular project."""
        r = self._request("GET", join("projects", self.project_id))
        return r

    def get_all_systems(self):
        """This method gets all systems for a particular project."""
        r = self._request("GET", join("projects", self.project_id, "systems"))
        return r

    def get_project_center(self):
        """This method gets the center as lat,lng for a particular project."""
        r = self._request("GET", join("projects", self.project_id, "center"))
        return r

    def get_single_system(self, system_id: int):
        """This method gets details  a single system for a particular project."""
        r = self._request(
            "GET", join("projects", self.project_id, "systems", str(system_id))
        )
        return r

    def get_constraints(self):
        """This method gets the geometry of constraints for a project if available"""
        r = self._request("GET", join("projects", self.project_id, "constraints"))
        return r

    def get_first_boundaries(self):
        """Gets the first boundaries if defined for a project"""
        r = self._request("GET", join("projects", self.project_id, "boundaries"))
        return r

    def get_second_boundaries(self):
        """Gets the second boundaries if defined for a project."""
        r = self._request("GET", join("projects", self.project_id, "secondboundaries"))
        return r

    def get_project_bounds(self):
        """Returns a string with bounding box for the project study area coordinates in a 'southwest_lng,southwest_lat,northeast_lng,northeast_lat' format."""
        r = self._request("GET", join("projects", self.project_id, "bounds"))
        return r

    def get_project_tags(self):
        """Returns a list of tags created in the project."""
        r = self._request("GET", join("projects", self.project_id, "tags"))
        return r

    def get_all_design_teams(self):
        """Return all the change teams for that project."""
        r = self._request("GET", join("projects", self.project_id, "cteams"))
        return r

    def get_single_synthesis(self, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), "Team id is not a integer: %r" % teamid
        assert len(synthesisid) == 16, "Synthesis : %s" % synthesisid
        r = self._request(
            "GET",
            join(
                "projects",
                self.project_id,
                "cteams",
                str(teamid),
                str(synthesisid) + "/",
            ),
        )
        return r

    def get_single_synthesis_details(self, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), "Team id is not a integer: %r" % teamid
        assert len(synthesisid) == 16, "Synthesis : %s" % synthesisid
        r = self._request(
            "GET",
            join(
                "projects",
                self.project_id,
                "cteams",
                str(teamid),
                str(synthesisid),
                "details",
            ),
        )
        return r

    def get_single_synthesis_esri_json(self, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), "Team id is not a integer: %r" % teamid
        assert len(synthesisid) == 16, "Synthesis : %s" % synthesisid
        r = self._request(
            "GET",
            join(
                "projects",
                self.project_id,
                "cteams",
                str(teamid),
                str(synthesisid),
                "esri",
            ),
        )
        return r

    def get_single_synthesis_diagrams(self, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), "Team id is not a integer: %r" % teamid
        r = self._request(
            "GET",
            join(
                "projects",
                self.project_id,
                "cteams",
                str(teamid),
                str(synthesisid),
                "diagrams",
            ),
        )
        return r

    def get_synthesis_timeline(self, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), "Team id is not a integer: %r" % teamid
        r = self._request(
            "GET",
            join(
                "projects",
                self.project_id,
                "cteams",
                str(teamid),
                str(synthesisid),
                "timeline",
            ),
        )
        return r

    def get_synthesis_diagrams(self, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), "Team id is not a integer: %r" % teamid
        r = self._request(
            "GET",
            join(
                "projects",
                self.project_id,
                "cteams",
                str(teamid),
                str(synthesisid),
                "diagrams",
            ),
        )
        return r

    def get_design_team_members(self, teamid: int):
        """Return all the change teams for that project."""
        assert isinstance(teamid, int), "Team id is not a integer: %r" % teamid
        r = self._request(
            "GET",
            join("projects", self.project_id, "cteams", str(teamid), "members"),
        )
        return r

    def get_synthesis_system_projects(self, sysid: int, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), "Team id is not a integer: %r" % teamid
        assert isinstance(sysid, int), "System id is not a integer %r" % sysid
        r = self._request(
            "GET",
            join(
                "projects",
                self.project_id,
                "cteams",
                str(teamid),
                str(synthesisid),
                "systems",
                str(sysid),
                "projects",
            ),
        )
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
        r = self._request(
            "POST",
            join(
                "projects",
                self.project_id,
                "systems",
                str(sysid),
                "add",
                projectorpolicy,
            ),
        )

        postdata = {
            "geometry": geoms,
            "description": description,
            "featuretype": featuretype,
            "fundingtype": fundingtype,
        }
        r = self._request(
            "POST",
            join(
                "projects",
                self.project_id,
                "systems",
                str(sysid),
                "add",
                projectorpolicy,
            ),
            json=postdata,
        )
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
        cost: int,
        costtype: str,
        additional_metadata: Optional[Dict[Any, Any]] = None,
    ):
        """Create a self.session object with correct headers and creds."""
        securl = join(
            "projects",
            self.project_id,
            "systems",
            str(sysid),
            "add",
            "external",
            projectorpolicy,
        )
        additional_metadata = additional_metadata or {}

        postdata = {
            "url ": url,
            "description": description,
            "layer_type": layer_type,
            "featuretype": featuretype,
            "fundingtype": fundingtype,
            "cost": cost,
            "costtype": costtype,
            "additional_metadata": additional_metadata,
        }
        r = self._request("POST", securl, json=postdata)
        return r

    def get_single_diagram(self, diagid: int):
        """This method gets the geometry of a diagram given a digram id."""
        assert isinstance(diagid, int), "diagram id is not an integer: %r" % id
        sec_url = join(
            "projects",
            self.project_id,
            "diagrams",
            str(diagid),
        )
        r = self._request("GET", sec_url)
        return r

    def get_all_diagrams(self):
        """This method gets the geometry of all diagrams in a project ."""
        sec_url = join(
            "projects",
            self.project_id,
            "diagrams",
            "all",
        )
        r = self._request("GET", sec_url)
        return r

    def get_diagram_changeid(self, diagid: int):
        """Returns the a hash of the last modified date, can be used to see if a diagram has changed from the last time it was accessed."""
        assert isinstance(diagid, int), "diagram id is not an integer: %r" % id
        sec_url = join(
            "projects",
            self.project_id,
            "diagrams",
            str(diagid),
            "changeid",
        )
        r = self._request("GET", sec_url)
        return r

    def post_as_ealuation_JSON(self, geoms, sysid: int, username: Optional[str] = None):
        """Create a self.session object with correct headers and creds."""
        sec_url = join(
            "projects",
            self.project_id,
            "systems",
            str(sysid),
            "e",
            "map",
            "json",
        )
        if username:
            sec_url = join(sec_url, username)

        r = self._request("POST", sec_url, json=geoms)
        return r

    def add_project_tags(self, tag_ids):
        """Add tags to a project"""
        sec_url = join(
            "projects",
            self.project_id,
            "tags",
        )

        r = self._request("POST", sec_url, json=tag_ids)
        return r

    def get_project_plugins(self):
        """Get plugins for a project"""
        sec_url = join(
            "projects",
            self.project_id,
            "plugins",
        )

        r = self._request("GET", sec_url)
        return r

    def add_plugins_to_project(self, tag_ids):
        """Add tags to a project"""
        sec_url = join(
            "projects",
            self.project_id,
            "plugins",
        )

        r = self._request("POST", sec_url, json=tag_ids)
        return r

    def create_diagram_groups(self, diagram_groups_payload):
        """Create multiple diagram groups"""
        sec_url = join(
            "projects",
            self.project_id,
            "diagrams",
            "groups",
        )
        r = self._request("POST", sec_url, json=diagram_groups_payload)
        return r

    def post_as_impact_JSON(self, geoms, sysid: int, username: Optional[str] = None):
        """Create a self.session object with correct headers and creds."""
        sec_url = join(
            "projects",
            self.project_id,
            "systems",
            str(sysid),
            "i",
            "map",
            "json",
        )
        if username:
            sec_url = join(sec_url, username)

        r = self._request("POST", sec_url, json=geoms)
        return r

    def post_as_evaluation_GBF(self, geoms, sysid: int, username: Optional[str] = None):
        """Create a self.session object with correct headers and creds."""
        sec_url = join(
            "projects",
            self.project_id,
            "systems",
            str(sysid),
            "e",
            "map",
            "gbf",
        )
        if username:
            sec_url = join(sec_url, username)

        r = self._request("POST", sec_url, files={"geoms.gbf": geoms})
        return r

    def post_gdservice_JSON(self, geometry, jobid: str):
        """Create a self.session object with correct headers and creds."""
        sec_url = join(
            "gdservices",
            "callback",
        )

        data = {"geometry": geometry, "jobid": jobid}
        r = self._request("POST", sec_url, data=json.dumps(data))
        return r

    def post_as_impact_GBF(self, geoms, sysid: int, username: Optional[str] = None):
        """Create a self.session object with correct headers and creds."""
        sec_url = join(
            "projects",
            self.project_id,
            "systems",
            str(sysid),
            "i",
            "map",
            "gbf",
        )
        if username:
            sec_url = join(sec_url, username)

        r = self._request("POST", sec_url, files={"geoms.gbf": geoms})
        return r

    def create_new_project(self, project_create_payload):
        """Create a self.session object with correct headers and creds."""
        sec_url = join(
            "projects",
            "create",
        )

        r = self._request("POST", sec_url, json=project_create_payload)
        return r

    def create_new_igc_project(self, project_create_payload):
        """Create a self.session object with correct headers and creds."""
        sec_url = join(
            "projects",
            "create-igc-project",
        )

        r = self._request("POST", sec_url, json=project_create_payload)
        return r
