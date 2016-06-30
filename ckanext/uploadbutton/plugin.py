""" Upload button extension """

import ckan.plugins as p
import ckan.plugins.toolkit as tk

from ckan.common import c

class UploadButtonPlugin(p.SingletonPlugin):
    """
    Makes the button to upload resources more easily accessible.
    Saves a bunch of clicks when uploading resources.
    """

    p.implements(p.IConfigurer)
    def update_config(self, config):
        tk.add_template_directory(config, 'templates')
