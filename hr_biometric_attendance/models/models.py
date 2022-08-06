# -*- coding: utf-8 -*-
import pytz
from datetime import datetime
import logging
from datetime import date

from odoo import api, fields, models
from odoo import _
from datetime import timedelta

from odoo.exceptions import UserError, ValidationError
_logger = logging.getLogger(__name__)
try:
    from zk import ZK, const
except ImportError:
    _logger.error("Unable to import pyzk library. Try 'pip3 install pyzk'.")

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    device_id = fields.Char(string='Biometric Device ID')

    @api.constrains('device_id')
    def check_unique_deviceid(self):
        records = self.env['hr.employee'].search([('device_id', '=', self.device_id),('device_id', '!=', False ),('id', '!=', self.id)])
        if records:
            raise UserError(_('Another User with same Biometric Device ID already exists.'))

class ZkMachine(models.Model):
    _name = 'zk.machine.attendance'
    _inherit = 'hr.attendance'

    @api.constrains('check_in', 'check_out', 'employee_id')
    def _check_validity(self):
        """overriding the __check_validity function for employee attendance."""
        # pass
        c = self

    device_id = fields.Char(string='Biometric Device ID')
    punch_type = fields.Selection([('0', 'Check In'),
                                   ('1', 'Check Out'),
                                   ('2', 'Break Out'),
                                   ('3', 'Break In'),
                                   ('4', 'Overtime In'),
                                   ('5', 'Overtime Out')],
                                  string='Punching Type')

    attendance_type = fields.Selection([('1', 'Finger'),
                                        ('15', 'Face'),
                                        ('2','Type_2'),
                                        ('3','Password'),
                                        ('4','Card')], string='Category')
    punching_time = fields.Datetime(string='Punching Time')
    address_id = fields.Many2one('res.partner', string='Working Address')


class ZkMachine(models.Model):
    _name = 'zk.machine'

    activity_date = fields.Date()
    zk_after_date = fields.Datetime(string='Attend Start Date',
                                    help='If provided, Attendance module will ignore records before this date.')

    # cron job function to check dailybiometric attendance
    def check_daily_biometric_attend(self):
        dt = date.today()
        today = datetime.combine(dt, datetime.min.time())
        today = today - timedelta(days=1)
        current_date = today + timedelta(hours=0, minutes=0, seconds=1)
        current_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
        daily_biometric_attends = self.env['hr.attendance'].search([('generated_via','=','biometric'),('check_in','>=',current_date)])
        if not daily_biometric_attends:
            raise ValidationError("No Biometric Attendance till: "+str(current_date))

    def download_attendance(self, user, list_attend):
        zk_attendance = self.env['zk.machine.attendance']
        att_obj = self.env['hr.attendance']
        try:
            user = user
        except:
            user = False
        try:
            dt = date.today()
            today = datetime.combine(dt, datetime.min.time())
            # today = today - timedelta(days=1)
            current_date = today + timedelta(hours=23, minutes=59)
            today = today.strftime('%Y-%m-%d %H:%M:%S')
            current_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
            attendance_list = list_attend
            attendance_employee_list = []
            for item in attendance_list:
                test = item["timestamp"]
                if item["timestamp"] >= today and item["timestamp"] <= current_date:
                    attendance_employee_list.append(item)
            attendance = attendance_employee_list
        except:
            attendance = False
        if attendance:
            for each in attendance:
                atten_time = each['timestamp']
                atten_time_d = datetime.strptime(atten_time, '%Y-%m-%d %H:%M:%S')
                atten_time = datetime.strptime(atten_time_d.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
                if self.zk_after_date == False:
                    tmp_zk_after_date = datetime.strptime('2000-01-01', "%Y-%m-%d")
                else:
                    tmp_zk_after_date = datetime.strptime(self.zk_after_date, '%Y-%m-%d %H:%M:%S')
                if atten_time != False and atten_time > tmp_zk_after_date:
                    local_tz = pytz.timezone(
                        self.env.user.partner_id.tz or 'GMT')
                    if self.zk_after_date == False:
                        tmp_zk_after_date = datetime.strptime('2000-01-01', "%Y-%m-%d")
                    else:
                        tmp_zk_after_date = datetime.strptime(self.zk_after_date, '%Y-%m-%d %H:%M:%S')
                    # if atten_time != False and atten_time > tmp_zk_after_date:
                    if atten_time:
                        local_tz = pytz.timezone(
                            self.env.user.partner_id.tz or 'GMT')
                        local_dt = local_tz.localize(atten_time, is_dst=None)
                        utc_dt = local_dt.astimezone(pytz.utc)
                        utc_dt = utc_dt.strftime("%Y-%m-%d %H:%M:%S")
                        atten_time = datetime.strptime(
                            utc_dt, "%Y-%m-%d %H:%M:%S")
                        atten_time = atten_time - timedelta(hours=5)
                        # tmp_utc = local_dt.astimezone(pytz.utc)
                        # tmp_attend = tmp_utc.strftime("%m-%d-%Y %H:%M:%S")
                        # atten_time = fields.Datetime.to_string(atten_time)
                        # c = atten_time
                    if user:
                        for uid in user:
                            if uid['user_id'] == each['user_id']:
                                get_user_id = self.env['hr.employee'].search(
                                    [('device_id', '=', each['user_id'])])
                                if get_user_id:
                                    duplicate_atten_ids = zk_attendance.search(
                                        [('device_id', '=', each['user_id']), ('punching_time', '=', atten_time)])
                                        # [('device_id', '=', each['user_id']), ('punching_time', '=', '2000-01-01')])
                                    if duplicate_atten_ids:
                                        continue
                                    else:
                                        # zk_attendance.create({'employee_id': get_user_id.id,
                                        #                       'device_id': each.user_id,
                                        #                       'attendance_type': str(each.status),
                                        #                       'punch_type': str(each.punch),
                                        #                       # 'punching_time': atten_time,
                                        #                       'address_id': self.address_id.id})
                                        att_var = att_obj.search([('employee_id', '=', get_user_id.id),
                                                                  ('check_out', '=', False)])
                                        att_var_check_in = att_obj.search([('employee_id', '=', get_user_id.id),
                                                                  ('check_in', '=', False)])
                                        if each['punch'] == 0:  # check-in
                                            _logger.info("check 1")
                                            if not att_var:
                                                _logger.info("check 2")
                                                attend_rec_tmp = att_obj.search([('employee_id', '=', get_user_id.id),
                                                                                 ('check_out', '>', atten_time)])
                                                # creating attendance
                                                if not attend_rec_tmp:
                                                    _logger.info("check 3")


                                                    att_rec = att_obj.search([('employee_id','=',get_user_id.id),('check_in','>=',atten_time)], order='check_in desc', limit=1)
                                                    _logger.info("JJJJJJJJJJJJJJJJJJ")
                                                    _logger.info(atten_time)
                                                    _logger.info(today)
                                                    _logger.info(att_rec)
                                                    _logger.info(get_user_id)
                                                    _logger.info("JJJJJJJJJJJJJJJJJJ")
                                                    if not att_rec:

                                                        att_obj.create({
                                                                        'generated_via': 'biometric',
                                                                        'activity_date': today,
                                                                        'employee_id': get_user_id.id,
                                                                        'check_in': atten_time,})
                                                        _logger.info("check 4")


                                        # if each['punch'] == 1:  # check-out
                                        #
                                        #     if len(att_var) == 1:
                                        #         if att_var.check_in:
                                        #             if not att_var.check_out:
                                        #                 _logger.info("W1")
                                        #                 _logger.info(atten_time)
                                        #                 _logger.info(att_var.check_in)
                                        #                 _logger.info(att_var.employee_id)
                                        #                 att_var.write({'check_out': atten_time})
                                        #                 _logger.info("WD1")
                                        #     else:
                                        #         att_var1 = att_obj.search([('employee_id', '=', get_user_id.id)])
                                        #         if att_var1:
                                        #             if att_var1[-1].check_in:
                                        #                 if not att_var1[-1].check_out:
                                        #                     _logger.info("W2")
                                        #                     att_var1[-1].write({'check_out': atten_time})
                                        #                     _logger.info("WD2")

                                        # else:
                                        #
                                        #     # adding check_out as max time of a day if a person dont add checkout
                                        #     test = att_var.check_in
                                        #     if att_var:
                                        #         if att_var.check_in:
                                        #             check_out_time = att_var.check_in + timedelta(hours=8)
                                        #
                                        #
                                        #             if check_out_time.day > att_var.check_in.day:
                                        #                 check_out_time = att_var.check_in.replace(day=atten_time.day, hour=23,
                                        #                                                     minute=59, second=59)
                                        #
                                        #             if len(att_var) == 1:
                                        #                 if att_var.check_in:
                                        #                     att_var.write({'check_out': check_out_time})
                                        #             else:
                                        #                 att_var1 = att_obj.search([('employee_id', '=', get_user_id.id)])
                                        #                 if att_var1:
                                        #                     if att_var1.check_in:
                                        #                         att_var1[-1].write({'check_out': check_out_time})


                                else:
                                    pass
                            else:
                                pass
            return True
        else:
            raise UserError(_('No attendances found in Attendance Device to Download.'))


    def update_check_out_attendance(self, user, list_attend):
        _logger.info("in my update_check_out_attendance function")
        zk_attendance = self.env['zk.machine.attendance']
        att_obj = self.env['hr.attendance']
        try:
            user = user
        except:
            user = False
        try:
            dt = date.today()
            today = datetime.combine(dt, datetime.min.time())
            # today = today - timedelta(days=1)
            current_date = today + timedelta(hours=23, minutes=59)
            today = today.strftime('%Y-%m-%d %H:%M:%S')
            current_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
            attendance_list = list_attend
            attendance_employee_list = []
            for item in attendance_list:
                test = item["timestamp"]
                if item["timestamp"] >= today and item["timestamp"] <= current_date:
                    attendance_employee_list.append(item)
            attendance = attendance_employee_list
        except:
            attendance = False
        if attendance:
            for each in attendance:
                atten_time = each['timestamp']
                atten_time_d = datetime.strptime(atten_time, '%Y-%m-%d %H:%M:%S')
                atten_time = datetime.strptime(atten_time_d.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
                if self.zk_after_date == False:
                    tmp_zk_after_date = datetime.strptime('2000-01-01', "%Y-%m-%d")
                else:
                    tmp_zk_after_date = datetime.strptime(self.zk_after_date, '%Y-%m-%d %H:%M:%S')
                if atten_time != False and atten_time > tmp_zk_after_date:
                    local_tz = pytz.timezone(
                        self.env.user.partner_id.tz or 'GMT')
                    if self.zk_after_date == False:
                        tmp_zk_after_date = datetime.strptime('2000-01-01', "%Y-%m-%d")
                    else:
                        tmp_zk_after_date = datetime.strptime(self.zk_after_date, '%Y-%m-%d %H:%M:%S')
                    if atten_time:
                        local_tz = pytz.timezone(
                            self.env.user.partner_id.tz or 'GMT')
                        local_dt = local_tz.localize(atten_time, is_dst=None)
                        utc_dt = local_dt.astimezone(pytz.utc)
                        utc_dt = utc_dt.strftime("%Y-%m-%d %H:%M:%S")
                        atten_time = datetime.strptime(
                            utc_dt, "%Y-%m-%d %H:%M:%S")
                        atten_time = atten_time - timedelta(hours=5)

                    if user:
                        for uid in user:
                            if uid['user_id'] == each['user_id']:
                                get_user_id = self.env['hr.employee'].search(
                                    [('device_id', '=', each['user_id'])])
                                if get_user_id:
                                    duplicate_atten_ids = zk_attendance.search(
                                        [('device_id', '=', each['user_id']), ('punching_time', '=', atten_time)])
                                        # [('device_id', '=', each['user_id']), ('punching_time', '=', '2000-01-01')])
                                    if duplicate_atten_ids:
                                        continue
                                    else:
                                        att_var = att_obj.search([('employee_id', '=', get_user_id.id),
                                                                  ('check_out', '=', False)])
                                        att_var_check_in = att_obj.search([('employee_id', '=', get_user_id.id),
                                                                  ('check_in', '=', False)])
                                        if each['punch'] == 1:  # check-out

                                            if len(att_var) == 1:
                                                if att_var.check_in:
                                                    if not att_var.check_out:
                                                        _logger.info("W3")
                                                        att_var.write({'check_out': atten_time})
                                                        _logger.info("WD3")
                                            else:
                                                att_var1 = att_obj.search([('employee_id', '=', get_user_id.id)])
                                                if att_var1:
                                                    if att_var1[-1].check_in:
                                                        if not att_var1[-1].check_out:
                                                            _logger.info("W4")
                                                            att_var1[-1].write({'check_out': atten_time})
                                                            _logger.info("WD4")

                                        else:
                                            _logger.info("RRRRRRRRRRRRRRRRRR")
                                            # adding check_out as max time of a day if a person dont add checkout
                                            test = att_var.check_in
                                            if att_var:
                                                if att_var.check_in:
                                                    check_out_time = att_var.check_in + timedelta(hours=8)


                                                    if check_out_time.day > att_var.check_in.day:
                                                        if check_out_time.hour > 5 and check_out_time.minute > 0 and check_out_time.second > 0:
                                                            check_out_time = att_var.check_in.replace(day=att_var.check_in.day, hour=18, minute=59, second=59)

                                                    if len(att_var) == 1:
                                                        if att_var.check_in:
                                                            if not att_var.check_out:
                                                                _logger.info("W5")
                                                                att_var.write({'check_out': check_out_time})
                                                                _logger.info("WD5")
                                                    else:
                                                        att_var1 = att_obj.search([('employee_id', '=', get_user_id.id)])
                                                        if att_var1:
                                                            if att_var1.check_in:
                                                                if not  att_var1[-1].check_out:
                                                                    _logger.info("W6")
                                                                    att_var1[-1].write({'check_out': check_out_time})
                                                                    _logger.info("WD6")


                                else:
                                    pass
                            else:
                                pass
            return True
        else:
            raise UserError(_('No attendances found in Attendance Device to Download.'))
