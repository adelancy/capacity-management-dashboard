import resources

PREFIX = 'data'


def add_restful_endpoints(api):
    api.add_resource(
        resources.data_center.locations.LocationsCollection,
        '/{0}/locations'.format(PREFIX),
        '/{0}/locations/<db_id>'.format(PREFIX),
        endpoint='locations-collection'
    )

    api.add_resource(
        resources.data_center.vms.VMCollection,
        '/{0}/vms'.format(PREFIX),
        '/{0}/vms/<db_id>'.format(PREFIX),
        endpoint='vms-collection'
    )

    api.add_resource(
        resources.data_center.licenses.LicenseCollection,
        '/{0}/licenses'.format(PREFIX),
        '/{0}/licenses/<db_id>'.format(PREFIX),
        endpoint='licenses-collection'
    )

    api.add_resource(
        resources.data_center.outlets.OutletCollection,
        '/{0}/outlets'.format(PREFIX),
        '/{0}/outlets/<db_id>'.format(PREFIX),
        endpoint='outlets-collection'
    )

    api.add_resource(
        resources.data_center.outlets.OutletTypeCollection,
        '/{0}/outlet-types'.format(PREFIX),
        '/{0}/outlet-types/<db_id>'.format(PREFIX),
        endpoint='outlet-types-collection'
    )

    api.add_resource(
        resources.data_center.rack.racks.RacksCollection,
        '/{0}/racks'.format(PREFIX),
        '/{0}/racks/<db_id>'.format(PREFIX),
        endpoint='racks-collection'
    )

    api.add_resource(
        resources.data_center.rack.racks.RackUnitCollection,
        '/{0}/rack-units'.format(PREFIX),
        '/{0}/rack-units/<db_id>'.format(PREFIX),
        endpoint='rack-units-collection'
    )

    api.add_resource(
        resources.team.TeamCollection,
        '/{0}/teams'.format(PREFIX),
        '/{0}/teams/<db_id>'.format(PREFIX),
        endpoint='teams-collection'
    )

    api.add_resource(
        resources.team.VMRequirementsCollection,
        '/{0}/vm-req'.format(PREFIX),
        '/{0}/vm-req/<db_id>'.format(PREFIX),
        endpoint='vm-reqs-collection'
    )

    api.add_resource(
        resources.team.BMRequirementsCollection,
        '/{0}/bm-req'.format(PREFIX),
        '/{0}/bm-req/<db_id>'.format(PREFIX),
        endpoint='bm-reqs-collection'
    )
