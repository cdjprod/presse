# -*- coding: utf-8 -*-

from datetime import timedelta, datetime
from odoo import models, fields, api

class Bruteradio(models.Model):
    _name = 'brute.radio'#'openacademy.session'
    _inherit = 'video.radio'

    name = fields.Char(string="CHAINE")
    date = fields.Datetime(string="DATE", default=fields.Date.today)
    datesearch = fields.Date(string=" Date Recherche", compute="_date_definition", store="True")
    categoryradio = fields.Char(string="Catégorie")
    secteurradio = fields.Char(string="SECTEUR")
    societeradio = fields.Char(string="SOCIETE")
    typeradio = fields.Char(string="TYPE")
    emissionradio = fields.Char(string="EMISSION")
    campagneradio = fields.Char(string="CAMPAGNE") 
    versionradio = fields.Char(string="VERSION")
    rangradio = fields.Char(string="RANG")
    timeslotradio = fields.Char(string="TRANCHE 3H", compute="_timeslotradio3_definition", store="True")
    dureeradio = fields.Integer (String="Durée")
    prixradio = fields.Integer(string="Valeur insertion", default=0)
    dayofdaterd = fields.Char(string="Jour", compute="_date_definition", store="True")
    grpens = fields.Float(string="GRP ENSEMBLE", default=0)
    grpcsp = fields.Float(string="GRP CSP+", default=0)
    grppopact = fields.Float(string="GRP POP ACT", default=0)
    grpjeune = fields.Float(string="GRP JEUNE", default=0)
    grpmf = fields.Float(string="GRP MF", default=0)
    timeofdaterd = fields.Char(string="TIME", compute="_time_definition", store="True")
    timeslotgrp = fields.Char(string="Tranche 15Min", compute="_timeslotradio15_definition", store="True")
    dayforgrp = fields.Char(string="Jour GRP", compute="_get_dayforgrp_rd", store="True")
    moisgrp = fields.Char(string="Mois", compute="_get_moisgrp_rd", store="True")
    annee = fields.Char(string="Annee", compute="_get_annee", store="True")
#^^^^^^^pour la semaine dayforgrp

    @api.depends('date')
    def _date_definition(self):
        for r in self:
            dt_obj = datetime.strptime(r.date,'%Y-%m-%d %H:%M:%S')
            if r.dayofdaterd == 0:
                r.dayofdaterd = datetime.strftime(dt_obj,'%A')
                r.datesearch = datetime.strftime(dt_obj,'%Y-%m-%d')
            else:
                r.dayofdaterd = 'False'

    @api.depends('date')
    def _get_moisgrp_rd(self):
        for r in self:
            dt_obj = datetime.strptime(r.date,'%Y-%m-%d %H:%M:%S')
            if r.moisgrp == 0:
                r.moisgrp = datetime.strftime(dt_obj,'%B')
            else:
                r.moisgrp = 'False'

    @api.depends('date')
    def _get_annee(self):
        for r in self:
            dt_obj = datetime.strptime(r.date,'%Y-%m-%d %H:%M:%S')
            if r.annee == 0:
                r.annee = datetime.strftime(dt_obj,'%Y')
            else:
                r.annee = 'False'

    @api.depends('date')
    def _time_definition(self):
        for r in self:
            dt_obj2 = datetime.strptime(r.date,'%Y-%m-%d %H:%M:%S')+timedelta(hours=3)
            if r.timeofdaterd == 0:
                r.timeofdaterd = datetime.strftime(dt_obj2,'%H:%M:%S')
            else:
                r.timeofdaterd = 'False'


# ra atao donnée ATW dia ovaina week-end ny samedi dimanche dia ny sql koa atao dayofdaterd = jour mediametrie
    @api.depends('dayofdaterd')
    def _get_dayforgrp_rd(self):
        for r in self:
            if r.dayofdaterd == 'dimanche':
                r.dayforgrp = 'dimanche'
            elif r.dayofdaterd == 'samedi':
                r.dayforgrp = 'samedi'
            else:
                r.dayforgrp = 'Semaine'

    @api.depends('timeofdaterd')
    def _timeslotradio3_definition(self):
        for r in self:
            if '03:00:00' <= r.timeofdaterd <= '06:00:00':
                r.timeslotradio = '03H-06H'
            elif '06:00:00' <= r.timeofdaterd <= '08:59:59':
                r.timeslotradio = '06H-09H'
            elif '09:00:00' <= r.timeofdaterd <= '11:59:59':
                r.timeslotradio = '09H-12H'
            elif '12:00:00' <= r.timeofdaterd <= '14:59:59':
                r.timeslotradio = '12H-15H'
            elif '15:00:00' <= r.timeofdaterd <= '17:59:59':
                r.timeslotradio = '15H-18H'
            elif '18:00:00' <= r.timeofdaterd <= '20:59:59':
                r.timeslotradio = '18H-21H'
            elif '21:00:00' <= r.timeofdaterd <= '23:59:59':
                r.timeslotradio = '21H-00H'
            elif '00:00:00' <= r.timeofdaterd <= '02:59:59':
                r.timeslotradio = '00H-3H'
            else:
                r.timeslotradio = 'False'

    @api.depends('timeofdaterd')
    def _timeslotradio15_definition(self):
        for r in self:
            if '05:00:00' <= r.timeofdaterd <= '05:15:00':
                r.timeslotgrp = '5h00-5h15'
            elif '05:30:00' <= r.timeofdaterd <= '05:45:00':
                r.timeslotgrp = '5h30-5h45'
            elif '06:00:00' <= r.timeofdaterd <= '06:15:00':
                r.timeslotgrp = '6h00-6h15'
            elif '06:30:00' <= r.timeofdaterd <= '06:45:00':
                r.timeslotgrp = '6h30-6h45'
            elif '07:00:00' <= r.timeofdaterd <= '07:15:00':
                r.timeslotgrp = '7h00-7h15'
            elif '07:30:00' <= r.timeofdaterd <= '07:45:00':
                r.timeslotgrp = '7h30-7h45'
            elif '08:00:00' <= r.timeofdaterd <= '08:15:00':
                r.timeslotgrp = '8h00-8h15'
            elif '08:30:00' <= r.timeofdaterd <= '08:45:00':
                r.timeslotgrp = '8h30-8h45'
            elif '09:00:00' <= r.timeofdaterd <= '09:15:00':
                r.timeslotgrp = '9h00-9h15'
            elif '09:30:00' <= r.timeofdaterd <= '09:45:00':
                r.timeslotgrp = '9h30-9h45'
            elif '10:00:00' <= r.timeofdaterd <= '10:15:00':
                r.timeslotgrp = '10h00-10h15'
            elif '10:30:00' <= r.timeofdaterd <= '10:45:00':
                r.timeslotgrp = '10h30-10h45'
            elif '11:00:00' <= r.timeofdaterd <= '11:15:00':
                r.timeslotgrp = '11h00-11h15'
            elif '11:30:00' <= r.timeofdaterd <= '11:45:00':
                r.timeslotgrp = '11h30-11h45'
            elif '12:00:00' <= r.timeofdaterd <= '12:15:00':
                r.timeslotgrp = '12h00-12h15'
            elif '12:30:00' <= r.timeofdaterd <= '12:45:00':
                r.timeslotgrp = '12h30-12h45'
            elif '13:00:00' <= r.timeofdaterd <= '13:15:00':
                r.timeslotgrp = '13h00-13h15'
            elif '13:30:00' <= r.timeofdaterd <= '13:45:00':
                r.timeslotgrp = '13h30-13h45'
            elif '14:00:00' <= r.timeofdaterd <= '14:15:00':
                r.timeslotgrp = '14h00-14h15'
            elif '14:30:00' <= r.timeofdaterd <= '14:45:00':
                r.timeslotgrp = '14h30-14h45'
            elif '15:00:00' <= r.timeofdaterd <= '15:15:00':
                r.timeslotgrp = '15h00-15h15'
            elif '15:30:00' <= r.timeofdaterd <= '15:45:00':
                r.timeslotgrp = '15h30-15h45'
            elif '16:00:00' <= r.timeofdaterd <= '16:15:00':
                r.timeslotgrp = '16h00-16h15'
            elif '16:30:00' <= r.timeofdaterd <= '16:45:00':
                r.timeslotgrp = '16h30-16h45'
            elif '17:00:00' <= r.timeofdaterd <= '17:15:00':
                r.timeslotgrp = '17h00-17h15'
            elif '17:30:00' <= r.timeofdaterd <= '17:45:00':
                r.timeslotgrp = '17h30-17h45'
            elif '18:00:00' <= r.timeofdaterd <= '18:15:00':
                r.timeslotgrp = '18h00-18h15'
            elif '18:30:00' <= r.timeofdaterd <= '18:45:00':
                r.timeslotgrp = '18h30-18h45'
            elif '19:00:00' <= r.timeofdaterd <= '19:15:00':
                r.timeslotgrp = '19h00-19h15'
            elif '19:30:00' <= r.timeofdaterd <= '19:45:00':
                r.timeslotgrp = '19h30-19h45'
            elif '20:00:00' <= r.timeofdaterd <= '20:15:00':
                r.timeslotgrp = '20h00-20h15'
            elif '20:30:00' <= r.timeofdaterd <= '20:45:00':
                r.timeslotgrp = '20h30-20h45'
            elif '21:00:00' <= r.timeofdaterd <= '21:15:00':
                r.timeslotgrp = '21h00-21h15'
            elif '21:30:00' <= r.timeofdaterd <= '21:45:00':
                r.timeslotgrp = '21h30-21h45'
            elif '22:00:00' <= r.timeofdaterd <= '22:15:00':
                r.timeslotgrp = '22h00-22h15'
            elif '22:30:00' <= r.timeofdaterd <= '22:45:00':
                r.timeslotgrp = '22h30-22h45'
            elif '23:00:00' <= r.timeofdaterd <= '23:15:00':
                r.timeslotgrp = '23h00-23h15'
            elif '23:30:00' <= r.timeofdaterd <= '23:45:00':
                r.timeslotgrp = '23h30-23h45'
            elif '00:00:00' <= r.timeofdaterd <= '00:15:00':
                r.timeslotgrp = '0h00-0h15'
            elif '00:30:00' <= r.timeofdaterd <= '00:45:00':
                r.timeslotgrp = '0h30-0h45'
            elif '01:00:00' <= r.timeofdaterd <= '01:15:00':
                r.timeslotgrp = '1h00-1h15'
            elif '01:30:00' <= r.timeofdaterd <= '01:45:00':
                r.timeslotgrp = '1h30-1h45'
            elif '02:00:00' <= r.timeofdaterd <= '02:15:00':
                r.timeslotgrp = '2h00-2h15'
            elif '02:30:00' <= r.timeofdaterd <= '02:45:00':
                r.timeslotgrp = '2h30-2h45'
            elif '03:00:00' <= r.timeofdaterd <= '03:15:00':
                r.timeslotgrp = '3h00-3h15'
            elif '03:30:00' <= r.timeofdaterd <= '03:45:00':
                r.timeslotgrp = '3h30-3h45'
            elif '04:00:00' <= r.timeofdaterd <= '04:15:00':
                r.timeslotgrp = '4h00-4h15'
            elif '04:30:00' <= r.timeofdaterd <= '04:45:00':
                r.timeslotgrp = '4h30-4h45'
            elif '05:15:00' <= r.timeofdaterd <= '05:30:00':
                r.timeslotgrp = '5h15-5h30'
            elif '05:45:00' <= r.timeofdaterd <= '06:00:00':
                r.timeslotgrp = '5h45-6h00'
            elif '06:15:00' <= r.timeofdaterd <= '06:30:00':
                r.timeslotgrp = '6h15-6h30'
            elif '06:45:00' <= r.timeofdaterd <= '07:00:00':
                r.timeslotgrp = '6h45-7h00'
            elif '07:15:00' <= r.timeofdaterd <= '07:30:00':
                r.timeslotgrp = '7h15-7h30'
            elif '07:45:00' <= r.timeofdaterd <= '08:00:00':
                r.timeslotgrp = '7h45-8h00'
            elif '08:15:00' <= r.timeofdaterd <= '08:30:00':
                r.timeslotgrp = '8h15-8h30'
            elif '08:45:00' <= r.timeofdaterd <= '09:00:00':
                r.timeslotgrp = '8h45-9h00'
            elif '09:15:00' <= r.timeofdaterd <= '09:30:00':
                r.timeslotgrp = '9h15-9h30'
            elif '09:45:00' <= r.timeofdaterd <= '10:00:00':
                r.timeslotgrp = '9h45-10h00'
            elif '10:15:00' <= r.timeofdaterd <= '10:30:00':
                r.timeslotgrp = '10h15-10h30'
            elif '10:45:00' <= r.timeofdaterd <= '11:00:00':
                r.timeslotgrp = '10h45-11h00'
            elif '11:15:00' <= r.timeofdaterd <= '11:30:00':
                r.timeslotgrp = '11h15-11h30'
            elif '11:45:00' <= r.timeofdaterd <= '12:00:00':
                r.timeslotgrp = '11h45-12h00'
            elif '12:15:00' <= r.timeofdaterd <= '12:30:00':
                r.timeslotgrp = '12h15-12h30'
            elif '12:45:00' <= r.timeofdaterd <= '13:00:00':
                r.timeslotgrp = '12h45-13h00'
            elif '13:15:00' <= r.timeofdaterd <= '13:30:00':
                r.timeslotgrp = '13h15-13h30'
            elif '13:45:00' <= r.timeofdaterd <= '14:00:00':
                r.timeslotgrp = '13h45-14h00'
            elif '14:15:00' <= r.timeofdaterd <= '14:30:00':
                r.timeslotgrp = '14h15-14h30'
            elif '14:45:00' <= r.timeofdaterd <= '15:00:00':
                r.timeslotgrp = '14h45-15h00'
            elif '15:15:00' <= r.timeofdaterd <= '15:30:00':
                r.timeslotgrp = '15h15-15h30'
            elif '15:45:00' <= r.timeofdaterd <= '16:00:00':
                r.timeslotgrp = '15h45-16h00'
            elif '16:15:00' <= r.timeofdaterd <= '16:30:00':
                r.timeslotgrp = '16h15-16h30'
            elif '16:45:00' <= r.timeofdaterd <= '17:00:00':
                r.timeslotgrp = '16h45-17h00'
            elif '17:15:00' <= r.timeofdaterd <= '17:30:00':
                r.timeslotgrp = '17h15-17h30'
            elif '17:45:00' <= r.timeofdaterd <= '18:00:00':
                r.timeslotgrp = '17h45-18h00'
            elif '18:15:00' <= r.timeofdaterd <= '18:30:00':
                r.timeslotgrp = '18h15-18h30'
            elif '18:45:00' <= r.timeofdaterd <= '19:00:00':
                r.timeslotgrp = '18h45-19h00'
            elif '19:15:00' <= r.timeofdaterd <= '19:30:00':
                r.timeslotgrp = '19h15-19h30'
            elif '19:45:00' <= r.timeofdaterd <= '20:00:00':
                r.timeslotgrp = '19h45-20h00'
            elif '20:15:00' <= r.timeofdaterd <= '20:30:00':
                r.timeslotgrp = '20h15-20h30'
            elif '20:45:00' <= r.timeofdaterd <= '21:00:00':
                r.timeslotgrp = '20h45-21h00'
            elif '21:15:00' <= r.timeofdaterd <= '21:30:00':
                r.timeslotgrp = '21h15-21h30'
            elif '21:45:00' <= r.timeofdaterd <= '22:00:00':
                r.timeslotgrp = '21h45-22h00'
            elif '22:15:00' <= r.timeofdaterd <= '22:30:00':
                r.timeslotgrp = '22h15-22h30'
            elif '22:45:00' <= r.timeofdaterd <= '23:00:00':
                r.timeslotgrp = '22h45-23h00'
            elif '23:15:00' <= r.timeofdaterd <= '23:30:00':
                r.timeslotgrp = '23h15-23h30'
            elif '23:45:00' <= r.timeofdaterd <= '00:00:00':
                r.timeslotgrp = '23h45-00h00'
            elif '00:15:00' <= r.timeofdaterd <= '00:30:00':
                r.timeslotgrp = '0h15-0h30'
            elif '00:45:00' <= r.timeofdaterd <= '01:00:00':
                r.timeslotgrp = '0h45-1h00'
            elif '01:15:00' <= r.timeofdaterd <= '01:30:00':
                r.timeslotgrp = '1h15-1h30'
            elif '01:45:00' <= r.timeofdaterd <= '02:00:00':
                r.timeslotgrp = '1h45-2h00'
            elif '02:15:00' <= r.timeofdaterd <= '02:30:00':
                r.timeslotgrp = '2h15-2h30'
            elif '02:45:00' <= r.timeofdaterd <= '03:00:00':
                r.timeslotgrp = '2h45-3h00'
            elif '03:15:00' <= r.timeofdaterd <= '03:30:00':
                r.timeslotgrp = '3h15-3h30'
            elif '03:45:00' <= r.timeofdaterd <= '04:00:00':
                r.timeslotgrp = '3h45-4h00'
            elif '04:15:00' <= r.timeofdaterd <= '04:30:00':
                r.timeslotgrp = '4h15-4h30'
            elif '04:45:00' <= r.timeofdaterd <= '05:00:00':
                r.timeslotgrp = '4h45-5h00'
            else:
                r.timeslotgrp = 'False'


# liste prix radio

class Listeradio(models.Model):
    _name = 'liste.radio' #openacademy.course

    name = fields.Char(string="CHAINE", required=True)
    dureerad1 = fields.Integer(string="Entre")
    dureerad2 = fields.Integer(string="Et")
    emissionrad = fields.Char(string="Emission")
    prixrad = fields.Integer(string="Prix")
    timeslotprixradio = fields.Char(string="Time slot radio", default="0")
    ranglisteradio = fields.Char(string="Rang radio", default="0")
    description = fields.Text()


# modif liste campagne

class Listecampagneradio(models.Model):
    _name = 'listeradio.campagne'

    name = fields.Char()
    secteurlisteradio = fields.Char(string="SECTEUR")
    societelisteradio = fields.Char(string="SOCIETE")
    categorylisteradio = fields.Char(string="CATEGORIE")
    campagnelisteradio = fields.Char(string="SI CAMPAGNE =")
    dureelisteradio = fields.Integer(string="Durée")
    sicampagnebruteradio = fields.Char(string="Si Campagne brute =")
    alorscampagnebruteradio = fields.Char(string="Alor Campagne brute =")

    @api.multi
    @api.depends()
    def campagne_radio_definition(self):
        campagnetele = self.env.cr.execute("UPDATE public.brute_radio SET secteurradio = secteurlisteradio, societeradio = societelisteradio, categoryradio = categorylisteradio FROM public.listeradio_campagne WHERE listeradio_campagne.campagnelisteradio = brute_radio.campagneradio",)

    @api.multi
    @api.depends()
    def dureeliste_radio_definition(self):
        dureetele = self.env.cr.execute("UPDATE public.brute_radio SET dureeradio = dureelisteradio FROM public.listeradio_campagne WHERE listeradio_campagne.campagnelisteradio = brute_radio.campagneradio",)

    @api.multi
    @api.depends()
    def modification_radio_campagne(self):
        dureetele = self.env.cr.execute("UPDATE public.brute_radio SET campagneradio = alorscampagnebruteradio FROM public.listeradio_campagne WHERE listeradio_campagne.sicampagnebruteradio = brute_radio.campagneradio",)


#GRP ENSMEBLE
class MMRDensemble(models.Model):
    _name = 'mmrd.ensemble'

    name = fields.Char(string="Chaine")
    jour = fields.Char(string="Jour")
    slotens = fields.Char(string="Tranche 15Min")
    tauxens = fields.Float(string="Préssion %")
    mois = fields.Char(string="Mois")



#GRP CSP
class MMRDcsp(models.Model):
    _name = 'mmrd.csp'

    name = fields.Char(string="Chaine")
    jour = fields.Char(string="Jour")
    slotens = fields.Char(string="Tranche 15Min")
    tauxens = fields.Float(string="Préssion %")
    mois = fields.Char(string="Mois")



#GRP POP ACT
class MMRDpopact(models.Model):
    _name = 'mmrd.popact'

    name = fields.Char(string="Chaine")
    jour = fields.Char(string="Jour")
    slotens = fields.Char(string="Tranche 15Min")
    tauxens = fields.Float(string="Préssion %")
    mois = fields.Char(string="Mois")

    
#GRP JEUNE
class MMRDjeune(models.Model):
    _name = 'mmrd.jeune'

    name = fields.Char(string="Chaine")
    jour = fields.Char(string="Jour")
    slotens = fields.Char(string="Tranche 15Min")
    tauxens = fields.Float(string="Préssion %")
    mois = fields.Char(string="Mois")

    
#GRP MERE DE FAMILLE = mf
class MMRDmf(models.Model):
    _name = 'mmrd.mf'

    name = fields.Char(string="Chaine")
    jour = fields.Char(string="Jour")
    slotens = fields.Char(string="Tranche 15Min")
    tauxens = fields.Float(string="Préssion %")
    mois = fields.Char(string="Mois")

    
# Partie simulation GRP PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
# Partie simulation GRP PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP

class Simulationradio(models.Model):
    _name = 'simulation.radio'#'openacademy.session'

    name = fields.Char(string="CHAINE")
    date = fields.Datetime(string="DATE", default=fields.Date.today)
    typeradio = fields.Char(string="TYPE", default="SPOT")
    emissionradio = fields.Char(string="EMISSION", default="PLAGE PUBLICITAIRE")
    campagneradio = fields.Char(string="CAMPAGNE") 
    rangradio = fields.Char(string="RANG")
    timeslotradio = fields.Char(string="TRANCHE 3H", compute="_timeslotradio3_definition", store="True")
    dureeradio = fields.Integer (String="Durée")
    prixradio = fields.Integer(string="Valeur insertion", default=0)
    dayofdaterd = fields.Char(string="Jour", compute="_date_definition", store="True")
    grpens = fields.Float(string="GRP ENSEMBLE")
    grpcsp = fields.Float(string="GRP CSP+")
    grppopact = fields.Float(string="GRP POP ACT")
    grpjeune = fields.Float(string="GRP JEUNE")
    grpmf = fields.Float(string="GRP MF")
    timeofdaterd = fields.Char(string="TIME", compute="_time_definition", store="True")
    timeslotgrp = fields.Char(string="Tranche 15Min", compute="_timeslotradio15_definition", store="True")
    dayforgrp = fields.Char(string="Jour GRP", compute="_get_dayforgrp_rd", store="True")
#^^^^^^^pour la semaine dayforgrp

    @api.depends('date')
    def _date_definition(self):
        for r in self:
            dt_obj = datetime.strptime(r.date,'%Y-%m-%d %H:%M:%S')
            if r.dayofdaterd == 0:
                r.dayofdaterd = datetime.strftime(dt_obj,'%A')
            else:
                r.dayofdaterd = 'False'

    @api.depends('date')
    def _time_definition(self):
        for r in self:
            dt_obj2 = datetime.strptime(r.date,'%Y-%m-%d %H:%M:%S')+timedelta(hours=3)
            if r.timeofdaterd == 0:
                r.timeofdaterd = datetime.strftime(dt_obj2,'%H:%M:%S')
            else:
                r.timeofdaterd = 'False'

    @api.multi
    @api.depends()
    def simulation_radio_definition(self):
        prixradio = self.env.cr.execute("UPDATE public.simulation_radio SET prixradio = prixrad FROM public.liste_radio WHERE simulation_radio.dureeradio BETWEEN liste_radio.dureerad1 AND liste_radio.dureerad2 AND simulation_radio.name = liste_radio.name AND simulation_radio.emissionradio = liste_radio.emissionrad AND liste_radio.timeslotprixradio = '0' AND liste_radio.ranglisteradio = '0' AND simulation_radio.typeradio = 'SPOT'",)
        prixradio = self.env.cr.execute("UPDATE public.simulation_radio SET prixradio = prixrad FROM public.liste_radio WHERE simulation_radio.dureeradio BETWEEN liste_radio.dureerad1 AND liste_radio.dureerad2 AND simulation_radio.name = liste_radio.name AND simulation_radio.emissionradio = liste_radio.emissionrad AND liste_radio.timeslotprixradio = '0' AND simulation_radio.rangradio = liste_radio.ranglisteradio AND simulation_radio.typeradio = 'SPOT'",)
        prixradio = self.env.cr.execute("UPDATE public.simulation_radio SET prixradio = prixrad FROM public.liste_radio WHERE simulation_radio.dureeradio BETWEEN liste_radio.dureerad1 AND liste_radio.dureerad2 AND simulation_radio.name = liste_radio.name AND simulation_radio.emissionradio = liste_radio.emissionrad AND simulation_radio.timeslotradio = liste_radio.timeslotprixradio AND liste_radio.ranglisteradio = '0' AND simulation_radio.typeradio = 'SPOT'",)
        prixradio = self.env.cr.execute("UPDATE public.simulation_radio SET prixradio = prixrad FROM public.liste_radio WHERE simulation_radio.dureeradio BETWEEN liste_radio.dureerad1 AND liste_radio.dureerad2 AND simulation_radio.name = liste_radio.name AND simulation_radio.emissionradio = liste_radio.emissionrad AND simulation_radio.timeslotradio = liste_radio.timeslotprixradio AND simulation_radio.rangradio = liste_radio.ranglisteradio AND simulation_radio.typeradio = 'SPOT'",)

        grpens = self.env.cr.execute("UPDATE public.simulation_radio SET grpens = tauxens FROM public.mmrd_ensemble WHERE simulation_radio.name = mmrd_ensemble.name AND simulation_radio.dayforgrp = mmrd_ensemble.jour AND simulation_radio.timeslotgrp = mmrd_ensemble.slotens")

        grpcsp = self.env.cr.execute("UPDATE public.simulation_radio SET grpcsp = tauxens FROM public.mmrd_csp WHERE simulation_radio.name = mmrd_csp.name AND simulation_radio.dayforgrp = mmrd_csp.jour AND simulation_radio.timeslotgrp = mmrd_csp.slotens")

        grppopact = self.env.cr.execute("UPDATE public.simulation_radio SET grppopact = tauxens FROM public.mmrd_popact WHERE simulation_radio.name = mmrd_popact.name AND simulation_radio.dayforgrp = mmrd_popact.jour AND simulation_radio.timeslotgrp = mmrd_popact.slotens")

        grpjeune = self.env.cr.execute("UPDATE public.simulation_radio SET grpjeune = tauxens FROM public.mmrd_jeune WHERE simulation_radio.name = mmrd_jeune.name AND simulation_radio.dayforgrp = mmrd_jeune.jour AND simulation_radio.timeslotgrp = mmrd_jeune.slotens")

        grpmf = self.env.cr.execute("UPDATE public.simulation_radio SET grpmf = tauxens FROM public.mmrd_mf WHERE simulation_radio.name = mmrd_mf.name AND simulation_radio.dayforgrp = mmrd_mf.jour AND simulation_radio.timeslotgrp = mmrd_mf.slotens")



    @api.depends('dayofdaterd')
    def _get_dayforgrp_rd(self):
        for r in self:
            if r.dayofdaterd == 'dimanche':
                r.dayforgrp = 'dimanche'
            elif r.dayofdaterd == 'samedi':
                r.dayforgrp = 'samedi'
            else:
                r.dayforgrp = 'Semaine'

    @api.depends('timeofdaterd')
    def _timeslotradio3_definition(self):
        for r in self:
            if '03:00:00' <= r.timeofdaterd <= '06:00:00':
                r.timeslotradio = '03H-06H'
            elif '06:00:00' <= r.timeofdaterd <= '08:59:59':
                r.timeslotradio = '06H-09H'
            elif '09:00:00' <= r.timeofdaterd <= '11:59:59':
                r.timeslotradio = '09H-12H'
            elif '12:00:00' <= r.timeofdaterd <= '14:59:59':
                r.timeslotradio = '12H-15H'
            elif '15:00:00' <= r.timeofdaterd <= '17:59:59':
                r.timeslotradio = '15H-18H'
            elif '18:00:00' <= r.timeofdaterd <= '20:59:59':
                r.timeslotradio = '18H-21H'
            elif '21:00:00' <= r.timeofdaterd <= '23:59:59':
                r.timeslotradio = '21H-00H'
            elif '00:00:00' <= r.timeofdaterd <= '02:59:59':
                r.timeslotradio = '00H-03H'
            else:
                r.timeslotradio = 'False'

    @api.depends('timeofdaterd')
    def _timeslotradio15_definition(self):
        for r in self:
            if '05:00:00' <= r.timeofdaterd <= '05:15:00':
                r.timeslotgrp = '5h00-5h15'
            elif '05:30:00' <= r.timeofdaterd <= '05:45:00':
                r.timeslotgrp = '5h30-5h45'
            elif '06:00:00' <= r.timeofdaterd <= '06:15:00':
                r.timeslotgrp = '6h00-6h15'
            elif '06:30:00' <= r.timeofdaterd <= '06:45:00':
                r.timeslotgrp = '6h30-6h45'
            elif '07:00:00' <= r.timeofdaterd <= '07:15:00':
                r.timeslotgrp = '7h00-7h15'
            elif '07:30:00' <= r.timeofdaterd <= '07:45:00':
                r.timeslotgrp = '7h30-7h45'
            elif '08:00:00' <= r.timeofdaterd <= '08:15:00':
                r.timeslotgrp = '8h00-8h15'
            elif '08:30:00' <= r.timeofdaterd <= '08:45:00':
                r.timeslotgrp = '8h30-8h45'
            elif '09:00:00' <= r.timeofdaterd <= '09:15:00':
                r.timeslotgrp = '9h00-9h15'
            elif '09:30:00' <= r.timeofdaterd <= '09:45:00':
                r.timeslotgrp = '9h30-9h45'
            elif '10:00:00' <= r.timeofdaterd <= '10:15:00':
                r.timeslotgrp = '10h00-10h15'
            elif '10:30:00' <= r.timeofdaterd <= '10:45:00':
                r.timeslotgrp = '10h30-10h45'
            elif '11:00:00' <= r.timeofdaterd <= '11:15:00':
                r.timeslotgrp = '11h00-11h15'
            elif '11:30:00' <= r.timeofdaterd <= '11:45:00':
                r.timeslotgrp = '11h30-11h45'
            elif '12:00:00' <= r.timeofdaterd <= '12:15:00':
                r.timeslotgrp = '12h00-12h15'
            elif '12:30:00' <= r.timeofdaterd <= '12:45:00':
                r.timeslotgrp = '12h30-12h45'
            elif '13:00:00' <= r.timeofdaterd <= '13:15:00':
                r.timeslotgrp = '13h00-13h15'
            elif '13:30:00' <= r.timeofdaterd <= '13:45:00':
                r.timeslotgrp = '13h30-13h45'
            elif '14:00:00' <= r.timeofdaterd <= '14:15:00':
                r.timeslotgrp = '14h00-14h15'
            elif '14:30:00' <= r.timeofdaterd <= '14:45:00':
                r.timeslotgrp = '14h30-14h45'
            elif '15:00:00' <= r.timeofdaterd <= '15:15:00':
                r.timeslotgrp = '15h00-15h15'
            elif '15:30:00' <= r.timeofdaterd <= '15:45:00':
                r.timeslotgrp = '15h30-15h45'
            elif '16:00:00' <= r.timeofdaterd <= '16:15:00':
                r.timeslotgrp = '16h00-16h15'
            elif '16:30:00' <= r.timeofdaterd <= '16:45:00':
                r.timeslotgrp = '16h30-16h45'
            elif '17:00:00' <= r.timeofdaterd <= '17:15:00':
                r.timeslotgrp = '17h00-17h15'
            elif '17:30:00' <= r.timeofdaterd <= '17:45:00':
                r.timeslotgrp = '17h30-17h45'
            elif '18:00:00' <= r.timeofdaterd <= '18:15:00':
                r.timeslotgrp = '18h00-18h15'
            elif '18:30:00' <= r.timeofdaterd <= '18:45:00':
                r.timeslotgrp = '18h30-18h45'
            elif '19:00:00' <= r.timeofdaterd <= '19:15:00':
                r.timeslotgrp = '19h00-19h15'
            elif '19:30:00' <= r.timeofdaterd <= '19:45:00':
                r.timeslotgrp = '19h30-19h45'
            elif '20:00:00' <= r.timeofdaterd <= '20:15:00':
                r.timeslotgrp = '20h00-20h15'
            elif '20:30:00' <= r.timeofdaterd <= '20:45:00':
                r.timeslotgrp = '20h30-20h45'
            elif '21:00:00' <= r.timeofdaterd <= '21:15:00':
                r.timeslotgrp = '21h00-21h15'
            elif '21:30:00' <= r.timeofdaterd <= '21:45:00':
                r.timeslotgrp = '21h30-21h45'
            elif '22:00:00' <= r.timeofdaterd <= '22:15:00':
                r.timeslotgrp = '22h00-22h15'
            elif '22:30:00' <= r.timeofdaterd <= '22:45:00':
                r.timeslotgrp = '22h30-22h45'
            elif '23:00:00' <= r.timeofdaterd <= '23:15:00':
                r.timeslotgrp = '23h00-23h15'
            elif '23:30:00' <= r.timeofdaterd <= '23:45:00':
                r.timeslotgrp = '23h30-23h45'
            elif '00:00:00' <= r.timeofdaterd <= '00:15:00':
                r.timeslotgrp = '0h00-0h15'
            elif '00:30:00' <= r.timeofdaterd <= '00:45:00':
                r.timeslotgrp = '0h30-0h45'
            elif '01:00:00' <= r.timeofdaterd <= '01:15:00':
                r.timeslotgrp = '1h00-1h15'
            elif '01:30:00' <= r.timeofdaterd <= '01:45:00':
                r.timeslotgrp = '1h30-1h45'
            elif '02:00:00' <= r.timeofdaterd <= '02:15:00':
                r.timeslotgrp = '2h00-2h15'
            elif '02:30:00' <= r.timeofdaterd <= '02:45:00':
                r.timeslotgrp = '2h30-2h45'
            elif '03:00:00' <= r.timeofdaterd <= '03:15:00':
                r.timeslotgrp = '3h00-3h15'
            elif '03:30:00' <= r.timeofdaterd <= '03:45:00':
                r.timeslotgrp = '3h30-3h45'
            elif '04:00:00' <= r.timeofdaterd <= '04:15:00':
                r.timeslotgrp = '4h00-4h15'
            elif '04:30:00' <= r.timeofdaterd <= '04:45:00':
                r.timeslotgrp = '4h30-4h45'
            elif '05:15:00' <= r.timeofdaterd <= '05:30:00':
                r.timeslotgrp = '5h15-5h30'
            elif '05:45:00' <= r.timeofdaterd <= '06:00:00':
                r.timeslotgrp = '5h45-6h00'
            elif '06:15:00' <= r.timeofdaterd <= '06:30:00':
                r.timeslotgrp = '6h15-6h30'
            elif '06:45:00' <= r.timeofdaterd <= '07:00:00':
                r.timeslotgrp = '6h45-7h00'
            elif '07:15:00' <= r.timeofdaterd <= '07:30:00':
                r.timeslotgrp = '7h15-7h30'
            elif '07:45:00' <= r.timeofdaterd <= '08:00:00':
                r.timeslotgrp = '7h45-8h00'
            elif '08:15:00' <= r.timeofdaterd <= '08:30:00':
                r.timeslotgrp = '8h15-8h30'
            elif '08:45:00' <= r.timeofdaterd <= '09:00:00':
                r.timeslotgrp = '8h45-9h00'
            elif '09:15:00' <= r.timeofdaterd <= '09:30:00':
                r.timeslotgrp = '9h15-9h30'
            elif '09:45:00' <= r.timeofdaterd <= '10:00:00':
                r.timeslotgrp = '9h45-10h00'
            elif '10:15:00' <= r.timeofdaterd <= '10:30:00':
                r.timeslotgrp = '10h15-10h30'
            elif '10:45:00' <= r.timeofdaterd <= '11:00:00':
                r.timeslotgrp = '10h45-11h00'
            elif '11:15:00' <= r.timeofdaterd <= '11:30:00':
                r.timeslotgrp = '11h15-11h30'
            elif '11:45:00' <= r.timeofdaterd <= '12:00:00':
                r.timeslotgrp = '11h45-12h00'
            elif '12:15:00' <= r.timeofdaterd <= '12:30:00':
                r.timeslotgrp = '12h15-12h30'
            elif '12:45:00' <= r.timeofdaterd <= '13:00:00':
                r.timeslotgrp = '12h45-13h00'
            elif '13:15:00' <= r.timeofdaterd <= '13:30:00':
                r.timeslotgrp = '13h15-13h30'
            elif '13:45:00' <= r.timeofdaterd <= '14:00:00':
                r.timeslotgrp = '13h45-14h00'
            elif '14:15:00' <= r.timeofdaterd <= '14:30:00':
                r.timeslotgrp = '14h15-14h30'
            elif '14:45:00' <= r.timeofdaterd <= '15:00:00':
                r.timeslotgrp = '14h45-15h00'
            elif '15:15:00' <= r.timeofdaterd <= '15:30:00':
                r.timeslotgrp = '15h15-15h30'
            elif '15:45:00' <= r.timeofdaterd <= '16:00:00':
                r.timeslotgrp = '15h45-16h00'
            elif '16:15:00' <= r.timeofdaterd <= '16:30:00':
                r.timeslotgrp = '16h15-16h30'
            elif '16:45:00' <= r.timeofdaterd <= '17:00:00':
                r.timeslotgrp = '16h45-17h00'
            elif '17:15:00' <= r.timeofdaterd <= '17:30:00':
                r.timeslotgrp = '17h15-17h30'
            elif '17:45:00' <= r.timeofdaterd <= '18:00:00':
                r.timeslotgrp = '17h45-18h00'
            elif '18:15:00' <= r.timeofdaterd <= '18:30:00':
                r.timeslotgrp = '18h15-18h30'
            elif '18:45:00' <= r.timeofdaterd <= '19:00:00':
                r.timeslotgrp = '18h45-19h00'
            elif '19:15:00' <= r.timeofdaterd <= '19:30:00':
                r.timeslotgrp = '19h15-19h30'
            elif '19:45:00' <= r.timeofdaterd <= '20:00:00':
                r.timeslotgrp = '19h45-20h00'
            elif '20:15:00' <= r.timeofdaterd <= '20:30:00':
                r.timeslotgrp = '20h15-20h30'
            elif '20:45:00' <= r.timeofdaterd <= '21:00:00':
                r.timeslotgrp = '20h45-21h00'
            elif '21:15:00' <= r.timeofdaterd <= '21:30:00':
                r.timeslotgrp = '21h15-21h30'
            elif '21:45:00' <= r.timeofdaterd <= '22:00:00':
                r.timeslotgrp = '21h45-22h00'
            elif '22:15:00' <= r.timeofdaterd <= '22:30:00':
                r.timeslotgrp = '22h15-22h30'
            elif '22:45:00' <= r.timeofdaterd <= '23:00:00':
                r.timeslotgrp = '22h45-23h00'
            elif '23:15:00' <= r.timeofdaterd <= '23:30:00':
                r.timeslotgrp = '23h15-23h30'
            elif '23:45:00' <= r.timeofdaterd <= '00:00:00':
                r.timeslotgrp = '23h45-00h00'
            elif '00:15:00' <= r.timeofdaterd <= '00:30:00':
                r.timeslotgrp = '0h15-0h30'
            elif '00:45:00' <= r.timeofdaterd <= '01:00:00':
                r.timeslotgrp = '0h45-1h00'
            elif '01:15:00' <= r.timeofdaterd <= '01:30:00':
                r.timeslotgrp = '1h15-1h30'
            elif '01:45:00' <= r.timeofdaterd <= '02:00:00':
                r.timeslotgrp = '1h45-2h00'
            elif '02:15:00' <= r.timeofdaterd <= '02:30:00':
                r.timeslotgrp = '2h15-2h30'
            elif '02:45:00' <= r.timeofdaterd <= '03:00:00':
                r.timeslotgrp = '2h45-3h00'
            elif '03:15:00' <= r.timeofdaterd <= '03:30:00':
                r.timeslotgrp = '3h15-3h30'
            elif '03:45:00' <= r.timeofdaterd <= '04:00:00':
                r.timeslotgrp = '3h45-4h00'
            elif '04:15:00' <= r.timeofdaterd <= '04:30:00':
                r.timeslotgrp = '4h15-4h30'
            elif '04:45:00' <= r.timeofdaterd <= '05:00:00':
                r.timeslotgrp = '4h45-5h00'
            else:
                r.timeslotgrp = 'False'

#Mise à jour prix grp rehetra
class Miseajour(models.Model):
    _name = 'maj.radio'

    name = fields.Char(string="Fictif")

    @api.multi
    @api.depends()
    def prix_radio_definition(self):
        prixradio = self.env.cr.execute("UPDATE public.brute_radio SET prixradio = prixrad FROM public.liste_radio WHERE brute_radio.dureeradio BETWEEN liste_radio.dureerad1 AND liste_radio.dureerad2 AND brute_radio.name = liste_radio.name AND brute_radio.prixradio = 0 AND brute_radio.emissionradio = liste_radio.emissionrad AND brute_radio.timeslotradio = liste_radio.timeslotprixradio AND brute_radio.rangradio = liste_radio.ranglisteradio AND brute_radio.typeradio = 'SPOT'",)
        prixradio = self.env.cr.execute("UPDATE public.brute_radio SET prixradio = prixrad FROM public.liste_radio WHERE brute_radio.dureeradio BETWEEN liste_radio.dureerad1 AND liste_radio.dureerad2 AND brute_radio.name = liste_radio.name AND brute_radio.prixradio = 0 AND brute_radio.emissionradio = liste_radio.emissionrad AND brute_radio.timeslotradio = liste_radio.timeslotprixradio AND liste_radio.ranglisteradio = '0' AND brute_radio.typeradio = 'SPOT'",)
        prixradio = self.env.cr.execute("UPDATE public.brute_radio SET prixradio = prixrad FROM public.liste_radio WHERE brute_radio.dureeradio BETWEEN liste_radio.dureerad1 AND liste_radio.dureerad2 AND brute_radio.name = liste_radio.name AND brute_radio.prixradio = 0 AND brute_radio.emissionradio = liste_radio.emissionrad AND liste_radio.timeslotprixradio = '0' AND brute_radio.rangradio = liste_radio.ranglisteradio AND brute_radio.typeradio = 'SPOT'",)
        prixradio = self.env.cr.execute("UPDATE public.brute_radio SET prixradio = prixrad FROM public.liste_radio WHERE brute_radio.dureeradio BETWEEN liste_radio.dureerad1 AND liste_radio.dureerad2 AND brute_radio.name = liste_radio.name AND brute_radio.prixradio = 0 AND brute_radio.emissionradio = liste_radio.emissionrad AND liste_radio.timeslotprixradio = '0' AND liste_radio.ranglisteradio = '0' AND brute_radio.typeradio = 'SPOT'",)
       


    @api.multi
    @api.depends()
    def prix_radio_all_definition(self):
        prixradio = self.env.cr.execute("UPDATE public.brute_radio SET prixradio = prixrad FROM public.liste_radio WHERE brute_radio.dureeradio BETWEEN liste_radio.dureerad1 AND liste_radio.dureerad2 AND brute_radio.name = liste_radio.name AND brute_radio.emissionradio = liste_radio.emissionrad AND liste_radio.timeslotprixradio = '0' AND liste_radio.ranglisteradio = '0' AND brute_radio.typeradio = 'SPOT'",)
        prixradio = self.env.cr.execute("UPDATE public.brute_radio SET prixradio = prixrad FROM public.liste_radio WHERE brute_radio.dureeradio BETWEEN liste_radio.dureerad1 AND liste_radio.dureerad2 AND brute_radio.name = liste_radio.name AND brute_radio.emissionradio = liste_radio.emissionrad AND liste_radio.timeslotprixradio = '0' AND brute_radio.rangradio = liste_radio.ranglisteradio AND brute_radio.typeradio = 'SPOT'",)
        prixradio = self.env.cr.execute("UPDATE public.brute_radio SET prixradio = prixrad FROM public.liste_radio WHERE brute_radio.dureeradio BETWEEN liste_radio.dureerad1 AND liste_radio.dureerad2 AND brute_radio.name = liste_radio.name AND brute_radio.emissionradio = liste_radio.emissionrad AND brute_radio.timeslotradio = liste_radio.timeslotprixradio AND liste_radio.ranglisteradio = '0' AND brute_radio.typeradio = 'SPOT'",)
        prixradio = self.env.cr.execute("UPDATE public.brute_radio SET prixradio = prixrad FROM public.liste_radio WHERE brute_radio.dureeradio BETWEEN liste_radio.dureerad1 AND liste_radio.dureerad2 AND brute_radio.name = liste_radio.name AND brute_radio.emissionradio = liste_radio.emissionrad AND brute_radio.timeslotradio = liste_radio.timeslotprixradio AND brute_radio.rangradio = liste_radio.ranglisteradio AND brute_radio.typeradio = 'SPOT'",)

    @api.multi
    @api.depends()
    def get_grp_rd(self):
        grpens = self.env.cr.execute("UPDATE public.brute_radio SET grpens = tauxens FROM public.mmrd_ensemble WHERE brute_radio.name = mmrd_ensemble.name AND brute_radio.grpens = 0 AND brute_radio.dayforgrp = mmrd_ensemble.jour AND brute_radio.timeslotgrp = mmrd_ensemble.slotens AND brute_radio.moisgrp = mmrd_ensemble.mois")

    @api.multi
    @api.depends()
    def get_grp_all_rd(self):
        grpens = self.env.cr.execute("UPDATE public.brute_radio SET grpens = tauxens FROM public.mmrd_ensemble WHERE brute_radio.name = mmrd_ensemble.name AND brute_radio.dayforgrp = mmrd_ensemble.jour AND brute_radio.timeslotgrp = mmrd_ensemble.slotens AND brute_radio.moisgrp = mmrd_ensemble.mois")

    @api.multi
    @api.depends()
    def get_grp_csp_rd(self):
        grpcsp = self.env.cr.execute("UPDATE public.brute_radio SET grpcsp = tauxens FROM public.mmrd_csp WHERE brute_radio.name = mmrd_csp.name AND brute_radio.grpcsp = 0 AND brute_radio.dayforgrp = mmrd_csp.jour AND brute_radio.timeslotgrp = mmrd_csp.slotens AND brute_radio.moisgrp = mmrd_csp.mois")

    @api.multi
    @api.depends()
    def get_grp_all_csp_rd(self):
        grpcsp = self.env.cr.execute("UPDATE public.brute_radio SET grpcsp = tauxens FROM public.mmrd_csp WHERE brute_radio.name = mmrd_csp.name AND brute_radio.dayforgrp = mmrd_csp.jour AND brute_radio.timeslotgrp = mmrd_csp.slotens AND brute_radio.moisgrp = mmrd_csp.mois")



    @api.multi
    @api.depends()
    def get_grp_popact_rd(self):
        grppopact = self.env.cr.execute("UPDATE public.brute_radio SET grppopact = tauxens FROM public.mmrd_popact WHERE brute_radio.name = mmrd_popact.name AND brute_radio.grppopact = 0 AND brute_radio.dayforgrp = mmrd_popact.jour AND brute_radio.timeslotgrp = mmrd_popact.slotens AND brute_radio.moisgrp = mmrd_popact.mois")

    @api.multi
    @api.depends()
    def get_grp_all_popact_rd(self):
        grppopact = self.env.cr.execute("UPDATE public.brute_radio SET grppopact = tauxens FROM public.mmrd_popact WHERE brute_radio.name = mmrd_popact.name AND brute_radio.dayforgrp = mmrd_popact.jour AND brute_radio.timeslotgrp = mmrd_popact.slotens AND brute_radio.moisgrp = mmrd_popact.mois")


    @api.multi
    @api.depends()
    def get_grp_jeune_rd(self):
        grpjeune = self.env.cr.execute("UPDATE public.brute_radio SET grpjeune = tauxens FROM public.mmrd_jeune WHERE brute_radio.name = mmrd_jeune.name AND brute_radio.grpjeune = 0 AND brute_radio.dayforgrp = mmrd_jeune.jour AND brute_radio.timeslotgrp = mmrd_jeune.slotens AND brute_radio.moisgrp = mmrd_jeune.mois")

    @api.multi
    @api.depends()
    def get_grp_all_jeune_rd(self):
        grpjeune = self.env.cr.execute("UPDATE public.brute_radio SET grpjeune = tauxens FROM public.mmrd_jeune WHERE brute_radio.name = mmrd_jeune.name AND brute_radio.dayforgrp = mmrd_jeune.jour AND brute_radio.timeslotgrp = mmrd_jeune.slotens AND brute_radio.moisgrp = mmrd_jeune.mois")

    @api.multi
    @api.depends()
    def get_grp_mf_rd(self):
        grpmf = self.env.cr.execute("UPDATE public.brute_radio SET grpmf = tauxens FROM public.mmrd_mf WHERE brute_radio.name = mmrd_mf.name AND brute_radio.grpmf = 0 AND brute_radio.dayforgrp = mmrd_mf.jour AND brute_radio.timeslotgrp = mmrd_mf.slotens AND brute_radio.moisgrp = mmrd_mf.mois")

    @api.multi
    @api.depends()
    def get_grp_all_mf_rd(self):
        grpmf = self.env.cr.execute("UPDATE public.brute_radio SET grpmf = tauxens FROM public.mmrd_mf WHERE brute_radio.name = mmrd_mf.name AND brute_radio.dayforgrp = mmrd_mf.jour AND brute_radio.timeslotgrp = mmrd_mf.slotens AND brute_radio.moisgrp = mmrd_mf.mois")


    @api.multi
    @api.depends()
    def modif_dayforgrp_rd(self):
        timeslotradio = self.env.cr.execute("UPDATE public.brute_radio SET timeslotradio = '03H-06H' WHERE brute_radio.timeslotradio = '3H-6H'")
        timeslotradio = self.env.cr.execute("UPDATE public.brute_radio SET timeslotradio = '06H-09H' WHERE brute_radio.timeslotradio = '6H-9H'")
        timeslotradio = self.env.cr.execute("UPDATE public.brute_radio SET timeslotradio = '09H-12H' WHERE brute_radio.timeslotradio = '9H-12H'")
        timeslotradio = self.env.cr.execute("UPDATE public.brute_radio SET timeslotradio = '21H-00H' WHERE brute_radio.timeslotradio = '21H-0H'")
        timeslotradio = self.env.cr.execute("UPDATE public.brute_radio SET timeslotradio = '00H-03H' WHERE brute_radio.timeslotradio = '0H-3H'")

        timeslotprixradio = self.env.cr.execute("UPDATE public.liste_radio SET timeslotprixradio = '03H-06H' WHERE liste_radio.timeslotprixradio = '3H-6H'")
        timeslotprixradio = self.env.cr.execute("UPDATE public.liste_radio SET timeslotprixradio = '06H-09H' WHERE liste_radio.timeslotprixradio = '6H-9H'")
        timeslotprixradio = self.env.cr.execute("UPDATE public.liste_radio SET timeslotprixradio = '09H-12H' WHERE liste_radio.timeslotprixradio = '9H-12H'")
        timeslotprixradio = self.env.cr.execute("UPDATE public.liste_radio SET timeslotprixradio = '21H-00H' WHERE liste_radio.timeslotprixradio = '21H-0H'")
        timeslotprixradio = self.env.cr.execute("UPDATE public.liste_radio SET timeslotprixradio = '00H-03H' WHERE liste_radio.timeslotprixradio = '0H-3H'")
        #dayforgrp = self.env.cr.execute("UPDATE public.brute_radio SET dayforgrp = 'Semaine'")
        #dayforgrp = self.env.cr.execute("UPDATE public.brute_radio SET dayforgrp = dayofdaterd WHERE brute_radio.dayofdaterd = 'samedi'")
        #dayforgrp = self.env.cr.execute("UPDATE public.brute_radio SET dayforgrp = dayofdaterd WHERE brute_radio.dayofdaterd = 'dimanche'")