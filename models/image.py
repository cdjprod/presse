# -*- coding: utf-8 -*-
# © 2014 Serv. Tecnol. Avanzados (http://www.serviciosbaeza.com)
#        Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>
# © 2015 Antiun Ingeniería S.L. - Jairo Llopis
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import base64
import urllib
import os
import logging
from odoo import models, fields, api, exceptions, _
from odoo import tools

_logger = logging.getLogger(__name__)


class Image(models.Model):
    _name = "image.image"

    storage = fields.Char(default='url')
    filename = fields.Char()
    url = fields.Char('URL')
    image = fields.Binary(compute="_get_image")

    @api.multi
    @api.depends('storage','url')
    def _get_image(self):
        """Get image data from the right storage type."""
        for r in self:
            r.image = getattr(r, "_get_image_from_%s" % r.storage)()

    @api.multi
    def _get_image_from_url(self):
       return self._get_image_from_url_cached(self.url)

    @api.model
    @tools.ormcache("url")
    def _get_image_from_url_cached(self, url):
        """Allow to download an image and cache it by its URL."""
        if url:
            try:
                (filename, header) = urllib.urlretrieve(url)
                with open(filename, 'rb') as f:
                    return base64.b64encode(f.read())
            except:
                _logger.error("URL %s cannot be fetched", url,
                              exc_info=True)
        return False