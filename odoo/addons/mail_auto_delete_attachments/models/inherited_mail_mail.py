# -*- coding: utf-8 -*-

import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class MailMail(models.Model):
    """Override existing mail.mail model.

    Accept delete attachments into post process of sent message
    """

    # region Private attributes
    _inherit = 'mail.mail'
    # endregion

    # region Default methods
    # endregion

    # region Fields declaration
    auto_delete_attachments = fields.Boolean(string="Auto delete attachments", default=False)
    # endregion

    # region Fields method
    # endregion

    # region Constrains and Onchange
    # endregion

    # region CRUD (overrides)
    # endregion

    # region Actions
    # endregion

    # region Model methods
    @api.multi
    def _postprocess_sent_message(self, mail_sent=True):
        attachments = list()

        for mail in self:
            if mail_sent and mail.auto_delete and mail.auto_delete_attachments:
                attachments.append(mail.mail_message_id.attachment_ids)

        res = super(MailMail, self)._postprocess_sent_message(mail_sent)

        for attachment in attachments:
            attachment.unlink()

        return res
    # endregion

    pass
