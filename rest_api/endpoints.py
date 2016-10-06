import resources.locations
import resources.vms
import resources.licenses
import resources.outlets
import resources.racks

PREFIX = 'data'


def add_restful_endpoints(api):
    api.add_resource(
        resources.locations.LocationsCollection,
        '/{0}/locations'.format(PREFIX),
        '/{0}/locations/<db_id>'.format(PREFIX),
        endpoint='locations-collection'
    )

    api.add_resource(
        resources.vms.VMCollection,
        '/{0}/vms'.format(PREFIX),
        '/{0}/vms/<db_id>'.format(PREFIX),
        endpoint='vms-collection'
    )

    api.add_resource(
        resources.licenses.LicenseCollection,
        '/{0}/licenses'.format(PREFIX),
        '/{0}/licenses/<db_id>'.format(PREFIX),
        endpoint='licenses-collection'
    )

    api.add_resource(
            resources.outlets.OutletCollection,
            '/{0}/outlets'.format(PREFIX),
            '/{0}/outlets/<db_id>'.format(PREFIX),
            endpoint='outlets-collection'
        )

    api.add_resource(
        resources.outlets.OutletTypeCollection,
        '/{0}/outlet-types'.format(PREFIX),
        '/{0}/outlet-types/<db_id>'.format(PREFIX),
        endpoint='outlet-types-collection'
    )

    api.add_resource(
        resources.racks.RacksCollection,
        '/{0}/racks'.format(PREFIX),
        '/{0}/racks/<db_id>'.format(PREFIX),
        endpoint='racks-collection'
    )

    api.add_resource(
        resources.racks.RackUnitCollection,
        '/{0}/rack-units'.format(PREFIX),
        '/{0}/rack-units/<db_id>'.format(PREFIX),
        endpoint='rack-units-collection'
    )

