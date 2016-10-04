import resources.locations as loc
import resources.vms

PREFIX = 'data'


def add_restful_endpoints(api):
    api.add_resource(
        loc.LocationsCollection,
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
