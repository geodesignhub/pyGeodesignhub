from functools import wraps
import requests
from urllib.parse import urljoin, urlparse
from os.path import join
from typing import Optional, Dict, Any

# Version: 1.5.0

class GeodesignHubClient:
    def __init__(self, token: str, url: Optional[str] = None, project_id: str = ""):
        assert project_id, "Project id is required"
        self.project_id = project_id
        self.token = token
        self.sec_url = urlparse(url or "https://www.geodesignhub.com/api/v1/")
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Token {self.token}"})

    def _build_url(self, *parts):
        return urljoin(self.sec_url.geturl(), join(*parts))

    @wraps(requests.Session.request)
    def _request(self, method, url, *args, **kwargs):
        full_url = self._build_url(url)
        return self.session.request(method, full_url, *args, **kwargs)

    def get_project_details(self):
        return self._request("GET", join("projects", self.project_id))

    def get_all_systems(self):
        return self._request("GET", join("projects", self.project_id, "systems"))

    def get_project_center(self):
        return self._request("GET", join("projects", self.project_id, "center"))

    def get_single_system(self, system_id: int):
        return self._request(
            "GET", join("projects", self.project_id, "systems", str(system_id))
        )

    def get_constraints(self):
        return self._request("GET", join("projects", self.project_id, "constraints"))

    def get_first_boundaries(self):
        return self._request("GET", join("projects", self.project_id, "boundaries"))

    def get_second_boundaries(self):
        return self._request(
            "GET", join("projects", self.project_id, "secondboundaries")
        )

    def get_project_bounds(self):
        return self._request("GET", join("projects", self.project_id, "bounds"))

    def get_project_tags(self):
        return self._request("GET", join("projects", self.project_id, "tags"))

    def get_all_design_teams(self):
        return self._request("GET", join("projects", self.project_id, "cteams"))

    def get_single_synthesis(self, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), f"Team id is not an integer: {teamid}"
        assert len(synthesisid) == 16, f"Synthesis: {synthesisid}"
        return self._request(
            "GET",
            join("projects", self.project_id, "cteams", str(teamid), f"{synthesisid}/"),
        )

    def get_single_synthesis_details(self, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), f"Team id is not an integer: {teamid}"
        assert len(synthesisid) == 16, f"Synthesis: {synthesisid}"
        return self._request(
            "GET",
            join(
                "projects",
                self.project_id,
                "cteams",
                str(teamid),
                synthesisid,
                "details",
            ),
        )

    def get_single_synthesis_esri_json(self, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), f"Team id is not an integer: {teamid}"
        assert len(synthesisid) == 16, f"Synthesis: {synthesisid}"
        return self._request(
            "GET",
            join(
                "projects", self.project_id, "cteams", str(teamid), synthesisid, "esri"
            ),
        )

    def get_single_synthesis_diagrams(self, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), f"Team id is not an integer: {teamid}"
        return self._request(
            "GET",
            join(
                "projects",
                self.project_id,
                "cteams",
                str(teamid),
                synthesisid,
                "diagrams",
            ),
        )

    def get_synthesis_timeline(self, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), f"Team id is not an integer: {teamid}"
        return self._request(
            "GET",
            join(
                "projects",
                self.project_id,
                "cteams",
                str(teamid),
                synthesisid,
                "timeline",
            ),
        )

    def get_synthesis_diagrams(self, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), f"Team id is not an integer: {teamid}"
        return self._request(
            "GET",
            join(
                "projects",
                self.project_id,
                "cteams",
                str(teamid),
                synthesisid,
                "diagrams",
            ),
        )

    def get_design_team_members(self, teamid: int):
        assert isinstance(teamid, int), f"Team id is not an integer: {teamid}"
        return self._request(
            "GET", join("projects", self.project_id, "cteams", str(teamid), "members")
        )

    def get_synthesis_system_projects(self, sysid: int, teamid: int, synthesisid: str):
        assert isinstance(teamid, int), f"Team id is not an integer: {teamid}"
        assert isinstance(sysid, int), f"System id is not an integer: {sysid}"
        return self._request(
            "GET",
            join(
                "projects",
                self.project_id,
                "cteams",
                str(teamid),
                synthesisid,
                "systems",
                str(sysid),
                "projects",
            ),
        )

    def post_as_diagram(
        self,
        geoms,
        projectorpolicy: str,
        featuretype: str,
        description: str,
        sysid: str,
        fundingtype: str,
    ):
        postdata = {
            "geometry": geoms,
            "description": description,
            "featuretype": featuretype,
            "fundingtype": fundingtype,
        }
        return self._request(
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
        postdata = {
            "url": url,
            "description": description,
            "layer_type": layer_type,
            "featuretype": featuretype,
            "fundingtype": fundingtype,
            "cost": cost,
            "costtype": costtype,
            "additional_metadata": additional_metadata or {},
        }
        return self._request(
            "POST",
            join(
                "projects",
                self.project_id,
                "systems",
                str(sysid),
                "add",
                "external",
                projectorpolicy,
            ),
            json=postdata,
        )

    def get_single_diagram(self, diagid: int):
        assert isinstance(diagid, int), f"diagram id is not an integer: {diagid}"
        return self._request(
            "GET", join("projects", self.project_id, "diagrams", str(diagid))
        )

    def get_all_diagrams(self):
        return self._request(
            "GET", join("projects", self.project_id, "diagrams", "all")
        )

    def get_diagram_changeid(self, diagid: int):
        assert isinstance(diagid, int), f"diagram id is not an integer: {diagid}"
        return self._request(
            "GET",
            join("projects", self.project_id, "diagrams", str(diagid), "changeid"),
        )

    def post_as_ealuation_JSON(self, geoms, sysid: int, username: Optional[str] = None):
        sec_url = join(
            "projects", self.project_id, "systems", str(sysid), "e", "map", "json"
        )
        if username:
            sec_url = join(sec_url, username)
        return self._request("POST", sec_url, json=geoms)

    def add_project_tags(self, tag_ids):
        return self._request(
            "POST", join("projects", self.project_id, "tags"), json=tag_ids
        )

    def get_project_plugins(self):
        return self._request("GET", join("projects", self.project_id, "plugins"))

    def add_plugins_to_project(self, tag_ids):
        return self._request(
            "POST", join("projects", self.project_id, "plugins"), json=tag_ids
        )

    def create_diagram_groups(self, diagram_groups_payload):
        return self._request(
            "POST",
            join("projects", self.project_id, "diagrams", "groups"),
            json=diagram_groups_payload,
        )

    def post_as_impact_JSON(self, geoms, sysid: int, username: Optional[str] = None):
        sec_url = join(
            "projects", self.project_id, "systems", str(sysid), "i", "map", "json"
        )
        if username:
            sec_url = join(sec_url, username)
        return self._request("POST", sec_url, json=geoms)

    def post_as_evaluation_GBF(self, geoms, sysid: int, username: Optional[str] = None):
        sec_url = join(
            "projects", self.project_id, "systems", str(sysid), "e", "map", "gbf"
        )
        if username:
            sec_url = join(sec_url, username)
        return self._request("POST", sec_url, files={"geoms.gbf": geoms})

    def post_gdservice_JSON(self, geometry, jobid: str):
        data = {"geometry": geometry, "jobid": jobid}
        return self._request("POST", join("gdservices", "callback"), json=data)

    def post_as_impact_GBF(self, geoms, sysid: int, username: Optional[str] = None):
        sec_url = join(
            "projects", self.project_id, "systems", str(sysid), "i", "map", "gbf"
        )
        if username:
            sec_url = join(sec_url, username)
        return self._request("POST", sec_url, files={"geoms.gbf": geoms})

    def create_new_project(self, project_create_payload):
        return self._request(
            "POST", join("projects", "create"), json=project_create_payload
        )

    def create_new_igc_project(self, project_create_payload):
        return self._request(
            "POST", join("projects", "create-igc-project"), json=project_create_payload
        )
