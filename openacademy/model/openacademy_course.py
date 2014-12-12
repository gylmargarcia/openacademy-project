from openerp import models, fields, api

class Course(models.Model):
    '''
    This class create model of course

    '''
    _name = 'openacademy.course' #Model odooname

    name = fields.Char(string='Title', required=True) #Fields reserved to identify name record
    description = fields.Text(string='Description')
