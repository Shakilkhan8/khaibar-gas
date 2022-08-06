from odoo import http
from datetime import date, timedelta, datetime
import logging
_logger = logging.getLogger(__name__)


class IzHrAllowances(http.Controller):
    @http.route('/bio_checkin', type='json', auth='none', methods=['POST'], csrf=False, cors='*')
    # @http.route('/bio_attendance', type='json', auth='none', methods=['POST'], csrf=False, cors='*')
    def bio_checkin_fun(self,  **kwargs):
        user = eval(kwargs.get('users'))
        list_attend = kwargs.get('list_attend')
        user_list = http.request.env['zk.machine'].sudo().search([])
        current_datetime = datetime.now()

        # below function should be called between 4:30 am to 5:00 am
        _logger.info ("Biometric attendance cron job")
        # t1 = current_datetime - timedelta(days=1)
        # t1 = t1.replace(hour=22, minute=30, second=1)
        # t2 = current_datetime.replace(hour=0, minute=1, second=59)
        # t3 = current_datetime
        # _logger.info(t1)
        # _logger.info(t2)
        # _logger.info(current_datetime)
        # if t1 <= current_datetime <= t2:
        #     _logger.info("Biometric Check out cron job has been executed at: "+str(current_datetime + timedelta(hours=5)))
        #     user_list.update_check_out_attendance(user, list_attend)
        # else:
        user_list.download_attendance(user, list_attend)

    @http.route('/bio_checkout', type='json', auth='none', methods=['POST'], csrf=False, cors='*')
    # @http.route('/bio_attendance', type='json', auth='none', methods=['POST'], csrf=False, cors='*')
    def bio_checkout_fun(self,  **kwargs):
        user = eval(kwargs.get('users'))
        list_attend = kwargs.get('list_attend')
        user_list = http.request.env['zk.machine'].sudo().search([])
        current_datetime = datetime.now()

        # below function should be called between 4:30 am to 5:00 am
        # _logger.info ("Biometric attendance cron job")
        # t1 = current_datetime - timedelta(days=1)
        # t1 = t1.replace(hour=22, minute=30, second=1)
        # t2 = current_datetime.replace(hour=0, minute=1, second=59)
        # t3 = current_datetime
        # _logger.info(t1)
        # _logger.info(t2)
        # _logger.info(current_datetime)
        # if t1 <= current_datetime <= t2:
        _logger.info("Biometric Check out cron job has been executed at: "+str(current_datetime + timedelta(hours=5)))
        user_list.update_check_out_attendance(user, list_attend)
        # else:
        #     user_list.download_attendance(user, list_attend)

