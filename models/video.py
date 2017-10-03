from odoo import models, api, fields




class VideoRadio(models.Model):
    _name = 'video.radio'
    
    url_radio = fields.Char('URL')
    
    
    @api.multi
    def ecouter_video_radio(self):

        url_radio = self.url_radio.replace("watch?v=", "embed/")  
        
        iframe = "<iframe style='height:300px;' width='900' height='315' src='%s' frameborder='0' allowfullscreen></iframe>"%(url_radio)
        
        return {
                'name' : "Watch Video",
                 'type': 'ir.actions.act_window',
                 'res_model': 'vision.radio',
                 'view_type': 'form',
                 'view_mode': 'form',
                 'context': {'default_url_radio': iframe},
                 'target': 'new',
                }

class VisionRadio(models.TransientModel):
    _name = 'vision.radio'
    
    url_radio = fields.Text('Lien video')



class VideoTele(models.Model):
    _name = 'video.tele'
    
    url_tele = fields.Char('URL')
    
    
    @api.multi
    def regarder_video_tele(self):

        url_tele = self.url_tele.replace("watch?v=", "embed/")  
        
        iframe = "<iframe style='height:400px;' width='560' height='315' src='%s' frameborder='0' allowfullscreen></iframe>"%(url_tele)
        
        return {
                'name' : "Watch Video",
                 'type': 'ir.actions.act_window',
                 'res_model': 'vision.tele',
                 'view_type': 'form',
                 'view_mode': 'form',
                 'context': {'default_url_tele': iframe},
                 'target': 'new',
                }


class VisionTele(models.TransientModel):
    _name = 'vision.tele'
    
    url_tele = fields.Text('Lien video')
