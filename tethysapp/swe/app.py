from tethys_sdk.base import TethysAppBase, url_map_maker


class Swe(TethysAppBase):
    """
    Tethys app class for SWE.
    """

    name = 'SWE'
    index = 'swe:home'
    icon = 'swe/images/icon.gif'
    package = 'swe'
    root_url = 'swe'
    color = '#8e44ad'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='swe',
                controller='swe.controllers.home'
            ),
        )

        return url_maps