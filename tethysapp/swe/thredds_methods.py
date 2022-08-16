def parse_datasets(catalog):
    """
    Collect all available datasets that have the WMS service enabled.

    Args:
        catalog(siphon.catalog.TDSCatalog): A Siphon catalog object bound to a valid THREDDS service.

    Returns:
        list<2-tuple<dataset_name, wms_url>: One 2-tuple for each dataset.
    """
    datasets = []

    for dataset_name, dataset_obj in catalog.datasets.items():
        dataset_wms_url = dataset_obj.access_urls.get('wms', None)
        if dataset_wms_url:
            datasets.append((dataset_name, f'{dataset_name};{dataset_wms_url}'))

    for catalog_name, catalog_obj in catalog.catalog_refs.items():
        d = parse_datasets(catalog_obj.follow())
        datasets.extend(d)

    return datasets
