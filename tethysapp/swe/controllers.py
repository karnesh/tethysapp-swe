from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import SelectInput
from .app import Swe as app
from .thredds_methods import parse_datasets, get_layers_for_wms
from django.http import HttpResponseNotAllowed, JsonResponse
import logging

log = logging.getLogger(__name__)




@controller(name='home',url='swe')
def home(request):
    """
    Controller for the app home page.
    """
    catalog = app.get_spatial_dataset_service(app.THREDDS_SERVICE_NAME, as_engine=True)

    # Retrieve dataset options from the THREDDS service
    log.info('Retrieving Datasets...')
    datasets = parse_datasets(catalog)
    initial_dataset_option = datasets[0]
    log.debug(datasets)
    log.debug(initial_dataset_option)

    dataset_select = SelectInput(
        display_text='Dataset',
        name='dataset',
        multiple=False,
        options=datasets,
        initial=initial_dataset_option,
        select2_options={'placeholder': 'Select a dataset',
                         'allowClear': False}
    )

    variable_select = SelectInput(
        display_text='Variable',
        name='variable',
        multiple=False,
        options=(),
        select2_options={'placeholder': 'Select a variable',
                         'allowClear': False}
    )

    style_select = SelectInput(
        display_text='Style',
        name='style',
        multiple=False,
        options=[('RedBlue', 'boxfill/redblue'), ('Rainbow', 'boxfill/rainbow'), ('Occam', 'boxfill/occam'), ('Ferret', 'boxfill/ferret')],
        #options=(),
        select2_options={'placeholder': 'Select a style',
                         'allowClear': False}
    )

    context = {
        'dataset_select': dataset_select,
        'variable_select': variable_select,
        'style_select': style_select,
    }

    return render(request, 'swe/home.html', context)


@controller(name='get_wms_layers',url='swe/get-wms-layers')
def get_wms_layers(request):
    json_response = {'success': False}

    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    try:
        wms_url = request.GET.get('wms_url', None)

        log.info(f'Retrieving layers for: {wms_url}')
        layers = get_layers_for_wms(wms_url)

        json_response.update({
            'success': True,
            'layers': layers
        })

    except Exception:
        json_response['error'] = f'An unexpected error has occurred. Please try again.'

    return JsonResponse(json_response)
