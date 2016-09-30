import resources.locations as loc

PREFIX = 'data'


def add_restful_endpoints(api):
    api.add_resource(
        loc.LocationsCollection,
        '/{0}/locations'.format(PREFIX),
        '/{0}/locations/<location_id>'.format(PREFIX)
    )
