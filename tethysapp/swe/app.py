from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import SpatialDatasetServiceSetting


class Swe(TethysAppBase):
    """
    Tethys app class for SWE.
    """

    name = 'SWE'
    index = 'swe:home'
    icon = 'swe/images/Superior.jpg'
    package = 'swe'
    root_url = 'swe'
    color = '#8e44ad'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    THREDDS_SERVICE_NAME = 'thredds_service'

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
            UrlMap(
                name='get_wms_layers',
                url='swe/get-wms-layers',
                controller='swe.controllers.get_wms_layers'
            ),
        )

        return url_maps

    def spatial_dataset_service_settings(self):
        """
        Spatial Dataset service settings method
        """
        sds_settings = (
            SpatialDatasetServiceSetting(
                name=self.THREDDS_SERVICE_NAME,
                description='THREDDS service for app to use',
                engine=SpatialDatasetServiceSetting.THREDDS,
                required=True,
            ),
        )

        return sds_settings
