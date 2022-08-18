from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import SelectInput
from .app import Swe as app
from .thredds_methods import parse_datasets


@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    catalog = app.get_spatial_dataset_service(app.THREDDS_SERVICE_NAME, as_engine=True)

    # Retrieve dataset options from the THREDDS service
    print("Retrieving Datasets...")
    datasets = parse_datasets(catalog)
    initial_dataset_option = datasets[0]
    from pprint import pprint
    pprint(datasets)
    pprint(initial_dataset_option)

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
        options=(),
        select2_options={'placeholder': 'Select a style',
                         'allowClear': False}
    )

    context = {
        'dataset_select': dataset_select,
        'variable_select': variable_select,
        'style_select': style_select,
    }

    return render(request, 'swe/home.html', context)
