from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import SelectInput


@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    # Retrieve dataset options from the THREDDS service
    datasets = []

    dataset_select = SelectInput(
        display_text='Dataset',
        name='dataset',
        multiple=False,
        options=datasets,
        initial=None,
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
