from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import SpatialDatasetServiceSetting


class Swe(TethysAppBase):
    """
    Tethys app class for SWE.
    """

    name = 'SWE'
    index = 'home'
    icon = 'swe/images/Superior.jpg'
    package = 'swe'
    root_url = 'swe'
    color = '#8e44ad'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []
    controller_modules = [ 'controllers' ]
    THREDDS_SERVICE_NAME = 'thredds_service'


    def spatial_dataset_service_settings(self):
        """
        Spatial Dataset service settings method
        """
        sds_settings = (
            SpatialDatasetServiceSetting(
                name=self.THREDDS_SERVICE_NAME,
                description='THREDDS service for app to use',
                engine=SpatialDatasetServiceSetting.THREDDS,
                required=False,
            ),
        )

        return sds_settings
