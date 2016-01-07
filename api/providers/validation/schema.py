FORMATS = ['gtiff', 'hdf-eos2', 'envi']

RESAMPLING_METHODS = ['nn', 'bil', 'cc']

PRODUCTS = [{'type': 'list',
             'allowed': ['tm_sr', 'tm_toa', 'tm_l1']},
            {'type': 'list',
             'allowed': ['etm_sr', 'etm_toa', 'etm_l1']},
            {'type': 'list',
             'allowed': ['olitirs_sr', 'olitirs_toa', 'olitirs_l1']},
            {'type': 'list',
             'allowed': ['oli_l1']}]

               # Albers
PROJECTIONS = [{'type': 'dict',
                'schema': {'name': {'type': 'string',
                                    'required': True,
                                    'allowed': ['AlbersEqualArea', 'aea']},
                           'standard_parallel_1': {'type': 'float',
                                                   'required': True,
                                                   'min': -90.0,
                                                   'max': 90.0},
                           'standard_parallel_2': {'type': 'float',
                                                   'required': True,
                                                   'min': -90.0,
                                                   'max': 90.0},
                           'central_meridian': {'type': 'float',
                                                'required': True,
                                                'min': -180.0,
                                                'max': 180.0},
                           'latitude_of_origin': {'type': 'float',
                                                  'required': True,
                                                  'min': -90.0,
                                                  'max': 90.0},
                           'false_easting': {'type': 'float',
                                             'required': True},
                           'false_northing': {'type': 'float',
                                              'required': True}}},
               # UTM
               {'type': 'dict',
                'schema': {'name': {'type': 'string',
                                    'required': True,
                                    'allowed': ['utm']},
                           'zone': {'type': 'integer',
                                    'required': True,
                                    'min': 1,
                                    'max': 60},
                           'zone_ns': {'type': 'string',
                                       'required': True,
                                       'allowed': ['north', 'south']}}},
               # Geographic
               {'type': 'dict',
                'schema': {'name': {'type': 'string',
                                    'required': True,
                                    'allowed': ['Geographic', 'lonlat']}}},
               # Sinusoidal
               {'type': 'dict',
                'schema': {'name': {'type': 'string',
                                    'required': True,
                                    'allowed': ['Sinusoidal', 'sinu']},
                           'central_meridian': {'type': 'float',
                                                'required': True,
                                                'min': -180.0,
                                                'max': 180.0},
                           'false_easting': {'type': 'float',
                                             'required': True},
                           'false_northing': {'type': 'float',
                                              'required': True}}},
               # Polar
               {'type': 'dict',
                'schema': {'name': {'type': 'string',
                                    'required': True,
                                    'allowed': ['PolarStereographic', 'ps']},
                           'longitudinal_pole': {'type': 'float',
                                                 'required': True,
                                                 'min': -180.0,
                                                 'max': 180.0},
                           'latitude_true_scale': {'type': 'float',
                                                   'required': True,
                                                   'anyof': [{'min': -90.0, 'max': -60.0},
                                                             {'min': 60.0, 'max': 90.0}]}}}]

CUSTOMIZATIONS = {'projection': {'type': 'list',
                                 'oneof': PROJECTIONS},
                  'format': {'type': 'list',
                             'oneof': FORMATS},
                  'resampling': {'type': 'list',
                                 'oneof': RESAMPLING_METHODS}}


DEVELOPER_OPTIONS = {'keep_directory': {'type': 'boolean'},
                     'keep_intermediate_data': {'type': 'boolean'},
                     'keep_log': {'type': 'boolean'}}


REQUEST_SCHEMA = {'products': {'type': 'list',
                               'required': True,
                               'oneof': PRODUCTS},
                  'customizations': {'type': 'dict',
                                     'required': False,
                                     'schema': CUSTOMIZATIONS},
                  'developer_options': {'type': 'dict',
                                        'required': False,
                                        'schema': DEVELOPER_OPTIONS}}


