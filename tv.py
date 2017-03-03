# -*- coding: utf-8 -*-

from datetime import timedelta, datetime
from odoo import models, fields, api

class Brutetele(models.Model):
    _name = 'brute.tele'#'openacademy.session'

    name = fields.Char(string="CHAINE")
    date = fields.Datetime(string="Date", default=fields.Date.today)
    datesearch = fields.Date(string=" Date Recherche", compute="_date_definition", store="True")
    secteurtele = fields.Char(string="SECTEUR")
    societetele = fields.Char(string="SOCIETE")
    typetele = fields.Char(string="TYPE")
    emissiontele = fields.Char(string="EMISSION")
    campagnetele = fields.Char(string="CAMPAGNE")
    versiontele = fields.Char(string="VERSION")
    rangtele = fields.Char(string="RANG")
    timeslottele = fields.Char(string="TRANCHE 3H", compute="_timeslot3_definition", store="True")
    dureetele = fields.Integer (string="Durée")
    prixtele = fields.Integer(string="Valeur insertion", default=0)
    dayofdatetv = fields.Char(string="Jour", compute="_date_definition", store="True")
    grpens = fields.Float(string="GRP ENSEMBLE", default=0)
    grpcsp = fields.Float(string="GRP CSP+", default=0)
    grppopact = fields.Float(string="GRP POP ACT", default=0)
    grpjeune = fields.Float(string="GRP JEUNE", default=0)
    grpmf = fields.Float(string="GRP MF", default=0)
    timeofdatetv = fields.Char(string="TIME", compute="_time_definition", store="True")
    timeslotgrp = fields.Char(string="Tranche 15Min", compute="_timeslot15_definition", store="True")
    dayforgrp = fields.Char(string="Jour GRP", compute="_get_dayforgrp", store="True")
    moisgrp = fields.Char(string="Mois", compute="_get_moisgrp_tv", store="True")
#^^^^^^^pour la semaine dayforgrp


    @api.depends('date')
    def _date_definition(self):
        for r in self:
            dt_obj = datetime.strptime(r.date,'%Y-%m-%d %H:%M:%S')+timedelta(hours=3)
            if r.dayofdatetv == 0:
                r.dayofdatetv = datetime.strftime(dt_obj,'%A')
                r.datesearch = datetime.strftime(dt_obj,'%Y-%m-%d')
            else:
                r.dayofdatetv = 'False'

    @api.depends('date')
    def _get_moisgrp_tv(self):
        for r in self:
            dt_obj = datetime.strptime(r.date,'%Y-%m-%d %H:%M:%S')+timedelta(hours=3)
            if r.moisgrp == 0:
                r.moisgrp = datetime.strftime(dt_obj,'%B')
            else:
                r.moisgrp = 'False'


    @api.depends('date')
    def _time_definition(self):
        for r in self:
            dt_obj2 = datetime.strptime(r.date,'%Y-%m-%d %H:%M:%S')+timedelta(hours=3)
            if r.timeofdatetv == 0:
                r.timeofdatetv = datetime.strftime(dt_obj2,'%H:%M:%S')
            else:
                r.timeofdatetv = 'False'


    @api.depends('dayofdatetv')
    def _get_dayforgrp(self):
        for r in self:
            if r.dayofdatetv == 'dimanche':
                r.dayforgrp = 'dimanche'
            elif r.dayofdatetv == 'samedi':
                r.dayforgrp = 'samedi'
            else:
                r.dayforgrp = 'Semaine'


    @api.depends('timeofdatetv')
    def _timeslot3_definition(self):
        for r in self:
            if '03:00:00' <= r.timeofdatetv <= '06:00:00':
                r.timeslottele = '03H-06H'
            elif '06:00:00' <= r.timeofdatetv <= '08:59:59':
                r.timeslottele = '06H-09H'
            elif '09:00:00' <= r.timeofdatetv <= '11:59:59':
                r.timeslottele = '09H-12H'
            elif '12:00:00' <= r.timeofdatetv <= '14:59:59':
                r.timeslottele = '12H-15H'
            elif '15:00:00' <= r.timeofdatetv <= '17:59:59':
                r.timeslottele = '15H-18H'
            elif '18:00:00' <= r.timeofdatetv <= '20:59:59':
                r.timeslottele = '18H-21H'
            elif '21:00:00' <= r.timeofdatetv <= '23:59:59':
                r.timeslottele = '21H-00H'
            elif '00:00:00' <= r.timeofdatetv <= '02:59:59':
                r.timeslottele = '00H-03H'
            else:
                r.timeslottele = 'False'

    @api.depends('timeofdatetv')
    def _timeslot15_definition(self):
        for r in self:
            if '05:00:00' <= r.timeofdatetv <= '05:15:00':
                r.timeslotgrp = '5h00-5h15'
            elif '05:30:00' <= r.timeofdatetv <= '05:45:00':
                r.timeslotgrp = '5h30-5h45'
            elif '06:00:00' <= r.timeofdatetv <= '06:15:00':
                r.timeslotgrp = '6h00-6h15'
            elif '06:30:00' <= r.timeofdatetv <= '06:45:00':
                r.timeslotgrp = '6h30-6h45'
            elif '07:00:00' <= r.timeofdatetv <= '07:15:00':
                r.timeslotgrp = '7h00-7h15'
            elif '07:30:00' <= r.timeofdatetv <= '07:45:00':
                r.timeslotgrp = '7h30-7h45'
            elif '08:00:00' <= r.timeofdatetv <= '08:15:00':
                r.timeslotgrp = '8h00-8h15'
            elif '08:30:00' <= r.timeofdatetv <= '08:45:00':
                r.timeslotgrp = '8h30-8h45'
            elif '09:00:00' <= r.timeofdatetv <= '09:15:00':
                r.timeslotgrp = '9h00-9h15'
            elif '09:30:00' <= r.timeofdatetv <= '09:45:00':
                r.timeslotgrp = '9h30-9h45'
            elif '10:00:00' <= r.timeofdatetv <= '10:15:00':
                r.timeslotgrp = '10h00-10h15'
            elif '10:30:00' <= r.timeofdatetv <= '10:45:00':
                r.timeslotgrp = '10h30-10h45'
            elif '11:00:00' <= r.timeofdatetv <= '11:15:00':
                r.timeslotgrp = '11h00-11h15'
            elif '11:30:00' <= r.timeofdatetv <= '11:45:00':
                r.timeslotgrp = '11h30-11h45'
            elif '12:00:00' <= r.timeofdatetv <= '12:15:00':
                r.timeslotgrp = '12h00-12h15'
            elif '12:30:00' <= r.timeofdatetv <= '12:45:00':
                r.timeslotgrp = '12h30-12h45'
            elif '13:00:00' <= r.timeofdatetv <= '13:15:00':
                r.timeslotgrp = '13h00-13h15'
            elif '13:30:00' <= r.timeofdatetv <= '13:45:00':
                r.timeslotgrp = '13h30-13h45'
            elif '14:00:00' <= r.timeofdatetv <= '14:15:00':
                r.timeslotgrp = '14h00-14h15'
            elif '14:30:00' <= r.timeofdatetv <= '14:45:00':
                r.timeslotgrp = '14h30-14h45'
            elif '15:00:00' <= r.timeofdatetv <= '15:15:00':
                r.timeslotgrp = '15h00-15h15'
            elif '15:30:00' <= r.timeofdatetv <= '15:45:00':
                r.timeslotgrp = '15h30-15h45'
            elif '16:00:00' <= r.timeofdatetv <= '16:15:00':
                r.timeslotgrp = '16h00-16h15'
            elif '16:30:00' <= r.timeofdatetv <= '16:45:00':
                r.timeslotgrp = '16h30-16h45'
            elif '17:00:00' <= r.timeofdatetv <= '17:15:00':
                r.timeslotgrp = '17h00-17h15'
            elif '17:30:00' <= r.timeofdatetv <= '17:45:00':
                r.timeslotgrp = '17h30-17h45'
            elif '18:00:00' <= r.timeofdatetv <= '18:15:00':
                r.timeslotgrp = '18h00-18h15'
            elif '18:30:00' <= r.timeofdatetv <= '18:45:00':
                r.timeslotgrp = '18h30-18h45'
            elif '19:00:00' <= r.timeofdatetv <= '19:15:00':
                r.timeslotgrp = '19h00-19h15'
            elif '19:30:00' <= r.timeofdatetv <= '19:45:00':
                r.timeslotgrp = '19h30-19h45'
            elif '20:00:00' <= r.timeofdatetv <= '20:15:00':
                r.timeslotgrp = '20h00-20h15'
            elif '20:30:00' <= r.timeofdatetv <= '20:45:00':
                r.timeslotgrp = '20h30-20h45'
            elif '21:00:00' <= r.timeofdatetv <= '21:15:00':
                r.timeslotgrp = '21h00-21h15'
            elif '21:30:00' <= r.timeofdatetv <= '21:45:00':
                r.timeslotgrp = '21h30-21h45'
            elif '22:00:00' <= r.timeofdatetv <= '22:15:00':
                r.timeslotgrp = '22h00-22h15'
            elif '22:30:00' <= r.timeofdatetv <= '22:45:00':
                r.timeslotgrp = '22h30-22h45'
            elif '23:00:00' <= r.timeofdatetv <= '23:15:00':
                r.timeslotgrp = '23h00-23h15'
            elif '23:30:00' <= r.timeofdatetv <= '23:45:00':
                r.timeslotgrp = '23h30-23h45'
            elif '00:00:00' <= r.timeofdatetv <= '00:15:00':
                r.timeslotgrp = '0h00-0h15'
            elif '00:30:00' <= r.timeofdatetv <= '00:45:00':
                r.timeslotgrp = '0h30-0h45'
            elif '01:00:00' <= r.timeofdatetv <= '01:15:00':
                r.timeslotgrp = '1h00-1h15'
            elif '01:30:00' <= r.timeofdatetv <= '01:45:00':
                r.timeslotgrp = '1h30-1h45'
            elif '02:00:00' <= r.timeofdatetv <= '02:15:00':
                r.timeslotgrp = '2h00-2h15'
            elif '02:30:00' <= r.timeofdatetv <= '02:45:00':
                r.timeslotgrp = '2h30-2h45'
            elif '03:00:00' <= r.timeofdatetv <= '03:15:00':
                r.timeslotgrp = '3h00-3h15'
            elif '03:30:00' <= r.timeofdatetv <= '03:45:00':
                r.timeslotgrp = '3h30-3h45'
            elif '04:00:00' <= r.timeofdatetv <= '04:15:00':
                r.timeslotgrp = '4h00-4h15'
            elif '04:30:00' <= r.timeofdatetv <= '04:45:00':
                r.timeslotgrp = '4h30-4h45'
            elif '05:15:00' <= r.timeofdatetv <= '05:30:00':
                r.timeslotgrp = '5h15-5h30'
            elif '05:45:00' <= r.timeofdatetv <= '06:00:00':
                r.timeslotgrp = '5h45-6h00'
            elif '06:15:00' <= r.timeofdatetv <= '06:30:00':
                r.timeslotgrp = '6h15-6h30'
            elif '06:45:00' <= r.timeofdatetv <= '07:00:00':
                r.timeslotgrp = '6h45-7h00'
            elif '07:15:00' <= r.timeofdatetv <= '07:30:00':
                r.timeslotgrp = '7h15-7h30'
            elif '07:45:00' <= r.timeofdatetv <= '08:00:00':
                r.timeslotgrp = '7h45-8h00'
            elif '08:15:00' <= r.timeofdatetv <= '08:30:00':
                r.timeslotgrp = '8h15-8h30'
            elif '08:45:00' <= r.timeofdatetv <= '09:00:00':
                r.timeslotgrp = '8h45-9h00'
            elif '09:15:00' <= r.timeofdatetv <= '09:30:00':
                r.timeslotgrp = '9h15-9h30'
            elif '09:45:00' <= r.timeofdatetv <= '10:00:00':
                r.timeslotgrp = '9h45-10h00'
            elif '10:15:00' <= r.timeofdatetv <= '10:30:00':
                r.timeslotgrp = '10h15-10h30'
            elif '10:45:00' <= r.timeofdatetv <= '11:00:00':
                r.timeslotgrp = '10h45-11h00'
            elif '11:15:00' <= r.timeofdatetv <= '11:30:00':
                r.timeslotgrp = '11h15-11h30'
            elif '11:45:00' <= r.timeofdatetv <= '12:00:00':
                r.timeslotgrp = '11h45-12h00'
            elif '12:15:00' <= r.timeofdatetv <= '12:30:00':
                r.timeslotgrp = '12h15-12h30'
            elif '12:45:00' <= r.timeofdatetv <= '13:00:00':
                r.timeslotgrp = '12h45-13h00'
            elif '13:15:00' <= r.timeofdatetv <= '13:30:00':
                r.timeslotgrp = '13h15-13h30'
            elif '13:45:00' <= r.timeofdatetv <= '14:00:00':
                r.timeslotgrp = '13h45-14h00'
            elif '14:15:00' <= r.timeofdatetv <= '14:30:00':
                r.timeslotgrp = '14h15-14h30'
            elif '14:45:00' <= r.timeofdatetv <= '15:00:00':
                r.timeslotgrp = '14h45-15h00'
            elif '15:15:00' <= r.timeofdatetv <= '15:30:00':
                r.timeslotgrp = '15h15-15h30'
            elif '15:45:00' <= r.timeofdatetv <= '16:00:00':
                r.timeslotgrp = '15h45-16h00'
            elif '16:15:00' <= r.timeofdatetv <= '16:30:00':
                r.timeslotgrp = '16h15-16h30'
            elif '16:45:00' <= r.timeofdatetv <= '17:00:00':
                r.timeslotgrp = '16h45-17h00'
            elif '17:15:00' <= r.timeofdatetv <= '17:30:00':
                r.timeslotgrp = '17h15-17h30'
            elif '17:45:00' <= r.timeofdatetv <= '18:00:00':
                r.timeslotgrp = '17h45-18h00'
            elif '18:15:00' <= r.timeofdatetv <= '18:30:00':
                r.timeslotgrp = '18h15-18h30'
            elif '18:45:00' <= r.timeofdatetv <= '19:00:00':
                r.timeslotgrp = '18h45-19h00'
            elif '19:15:00' <= r.timeofdatetv <= '19:30:00':
                r.timeslotgrp = '19h15-19h30'
            elif '19:45:00' <= r.timeofdatetv <= '20:00:00':
                r.timeslotgrp = '19h45-20h00'
            elif '20:15:00' <= r.timeofdatetv <= '20:30:00':
                r.timeslotgrp = '20h15-20h30'
            elif '20:45:00' <= r.timeofdatetv <= '21:00:00':
                r.timeslotgrp = '20h45-21h00'
            elif '21:15:00' <= r.timeofdatetv <= '21:30:00':
                r.timeslotgrp = '21h15-21h30'
            elif '21:45:00' <= r.timeofdatetv <= '22:00:00':
                r.timeslotgrp = '21h45-22h00'
            elif '22:15:00' <= r.timeofdatetv <= '22:30:00':
                r.timeslotgrp = '22h15-22h30'
            elif '22:45:00' <= r.timeofdatetv <= '23:00:00':
                r.timeslotgrp = '22h45-23h00'
            elif '23:15:00' <= r.timeofdatetv <= '23:30:00':
                r.timeslotgrp = '23h15-23h30'
            elif '23:45:00' <= r.timeofdatetv <= '23:59:59':
                r.timeslotgrp = '23h45-00h00'
            elif '00:15:00' <= r.timeofdatetv <= '00:30:00':
                r.timeslotgrp = '0h15-0h30'
            elif '00:45:00' <= r.timeofdatetv <= '01:00:00':
                r.timeslotgrp = '0h45-1h00'
            elif '01:15:00' <= r.timeofdatetv <= '01:30:00':
                r.timeslotgrp = '1h15-1h30'
            elif '01:45:00' <= r.timeofdatetv <= '02:00:00':
                r.timeslotgrp = '1h45-2h00'
            elif '02:15:00' <= r.timeofdatetv <= '02:30:00':
                r.timeslotgrp = '2h15-2h30'
            elif '02:45:00' <= r.timeofdatetv <= '03:00:00':
                r.timeslotgrp = '2h45-3h00'
            elif '03:15:00' <= r.timeofdatetv <= '03:30:00':
                r.timeslotgrp = '3h15-3h30'
            elif '03:45:00' <= r.timeofdatetv <= '04:00:00':
                r.timeslotgrp = '3h45-4h00'
            elif '04:15:00' <= r.timeofdatetv <= '04:30:00':
                r.timeslotgrp = '4h15-4h30'
            elif '04:45:00' <= r.timeofdatetv <= '05:00:00':
                r.timeslotgrp = '4h45-5h00'
            else:
                r.timeslotgrp = 'False'



#liste PIRX TV 
class Listetv(models.Model):
    _name = 'liste.tv' #openacademy.course

    name = fields.Char(string="CHAINE", required=True)
    dureetv1 = fields.Integer(string="Entre")
    dureetv2 = fields.Integer(string="Et")
    emissiontv = fields.Char(string="Emission")
    prixtv = fields.Integer(string="Prix")
    timeslotprixtele =fields.Char(string="Time slot Tele", default="0")
    ranglistetele = fields.Char(string="Rang Tele", default="0")
    description = fields.Text()


#Manipulation Campagne donnée
class Listecampagne(models.Model):
    _name = 'liste.campagne'

    name = fields.Char()
    secteurliste = fields.Char(string="SECTEUR")
    societeliste = fields.Char(string="SOCIETE")
    campagneliste = fields.Char(string="SI CAMPAGNE =")
    dureeliste = fields.Integer(string="Durée")
    sicampagnebrute = fields.Char(string="Si Campagne brute =")
    alorscampagnebrute = fields.Char(string="Alors Campagne brute =")

    @api.multi
    @api.depends()
    def campagne_definition(self):
        campagnetele = self.env.cr.execute("UPDATE public.brute_tele SET secteurtele = secteurliste, societetele = societeliste FROM public.liste_campagne WHERE liste_campagne.campagneliste = brute_tele.campagnetele",)

    @api.multi
    @api.depends()
    def dureeliste_definition(self):
        dureetele = self.env.cr.execute("UPDATE public.brute_tele SET dureetele = dureeliste FROM public.liste_campagne WHERE liste_campagne.campagneliste = brute_tele.campagnetele",)

    @api.multi
    @api.depends()
    def modification_campagne(self):
        dureetele = self.env.cr.execute("UPDATE public.brute_tele SET campagnetele = alorscampagnebrute FROM public.liste_campagne WHERE liste_campagne.sicampagnebrute = brute_tele.campagnetele",)


#GRP ENSMEBLE
class MMensemble(models.Model):
    _name = 'mm.ensemble'

    name = fields.Char(string="Chaine")
    jour = fields.Char(string="Jour")
    slotens = fields.Char(string="Tranche Horaire")
    tauxens = fields.Float(string="Préssion %")
    mois = fields.Char(string="Mois")

    
#GRP CSP
class MMcsp(models.Model):
    _name = 'mm.csp'

    name = fields.Char(string="Chaine")
    jour = fields.Char(string="Jour")
    slotens = fields.Char(string="Tranche Horaire")
    tauxens = fields.Float(string="Préssion %")
    mois = fields.Char(string="Mois")

    
#GRP Population active = popact
class MMpopact(models.Model):
    _name = 'mm.popact'

    name = fields.Char(string="Chaine")
    jour = fields.Char(string="Jour")
    slotens = fields.Char(string="Tranche Horaire")
    tauxens = fields.Float(string="Préssion %")
    mois = fields.Char(string="Mois")

    
#GRP Jeune
class MMjeune(models.Model):
    _name = 'mm.jeune'

    name = fields.Char(string="Chaine")
    jour = fields.Char(string="Jour")
    slotens = fields.Char(string="Tranche Horaire")
    tauxens = fields.Float(string="Préssion %")
    mois = fields.Char(string="Mois")

    
#GRP Mère de famille = mf
class MMmf(models.Model):
    _name = 'mm.mf'

    name = fields.Char(string="Chaine")
    jour = fields.Char(string="Jour")
    slotens = fields.Char(string="Tranche Horaire")
    tauxens = fields.Float(string="Préssion %")
    mois = fields.Char(string="Mois")

    

#Partie Simulation GRP pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
#Partie Simulation GRP pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp


class simulationtele(models.Model):
    _name = 'simulation.tele'#'openacademy.session'

    name = fields.Char(string="CHAINE")
    date = fields.Datetime(string="Date", default=fields.Date.today)
    typetele = fields.Char(string="TYPE", default="SPOT")
    emissiontele = fields.Char(string="EMISSION", default="PLAGE PUBLICITAIRE")
    campagnetele = fields.Char(string="CAMPAGNE")
    rangtele = fields.Char(string="RANG")
    timeslottele = fields.Char(string="TRANCHE 3H", compute="_timeslot3_definition", store="True")
    dureetele = fields.Integer (string="Durée")
    prixtele = fields.Integer(string="Valeur insertion", default=0)
    dayofdatetv = fields.Char(string="Jour", compute="_date_definition", store="True")
    grpens = fields.Float(string="GRP ENSEMBLE")
    grpcsp = fields.Float(string="GRP CSP+")
    grppopact = fields.Float(string="GRP POP ACT")
    grpjeune = fields.Float(string="GRP JEUNE")
    grpmf = fields.Float(string="GRP MF")
    timeofdatetv = fields.Char(string="TIME", compute="_time_definition", store="True")
    timeslotgrp = fields.Char(string="Tranche 15Min", compute="_timeslot15_definition", store="True")
    dayforgrp = fields.Char(string="Jour GRP", compute="_get_dayforgrp", store="True")
    moisgrp = fields.Char(string="Mois", compute="_get_moisgrp_tv", store="True")
#^^^^^^^pour la semaine dayforgrp


    @api.depends('date')
    def _date_definition(self):
        for r in self:
            dt_obj = datetime.strptime(r.date,'%Y-%m-%d %H:%M:%S')+timedelta(hours=3)
            if r.dayofdatetv == 0:
                r.dayofdatetv = datetime.strftime(dt_obj,'%A')
            else:
                r.dayofdatetv = 'False'

    @api.depends('date')
    def _get_moisgrp_tv(self):
        for r in self:
            dt_obj = datetime.strptime(r.date,'%Y-%m-%d %H:%M:%S')+timedelta(hours=3)
            if r.moisgrp == 0:
                r.moisgrp = datetime.strftime(dt_obj,'%B')
            else:
                r.moisgrp = 'False'


    @api.depends('date')
    def _time_definition(self):
        for r in self:
            dt_obj2 = datetime.strptime(r.date,'%Y-%m-%d %H:%M:%S')+timedelta(hours=3)
            if r.timeofdatetv == 0:
                r.timeofdatetv = datetime.strftime(dt_obj2,'%H:%M:%S')
            else:
                r.timeofdatetv = 'False'

    @api.multi
    @api.depends()
    def simulation_tv_definition(self):
        prixtele = self.env.cr.execute("UPDATE public.simulation_tele SET prixtele = prixtv FROM public.liste_tv WHERE simulation_tele.dureetele BETWEEN liste_tv.dureetv1 AND liste_tv.dureetv2 AND simulation_tele.name = liste_tv.name AND simulation_tele.emissiontele = liste_tv.emissiontv AND liste_tv.timeslotprixtele = '0' AND liste_tv.ranglistetele = '0' AND simulation_tele.typetele = 'SPOT'",)
        prixtele = self.env.cr.execute("UPDATE public.simulation_tele SET prixtele = prixtv FROM public.liste_tv WHERE simulation_tele.dureetele BETWEEN liste_tv.dureetv1 AND liste_tv.dureetv2 AND simulation_tele.name = liste_tv.name AND simulation_tele.emissiontele = liste_tv.emissiontv AND liste_tv.timeslotprixtele = '0' AND simulation_tele.rangtele = liste_tv.ranglistetele AND simulation_tele.typetele = 'SPOT'",)
        prixtele = self.env.cr.execute("UPDATE public.simulation_tele SET prixtele = prixtv FROM public.liste_tv WHERE simulation_tele.dureetele BETWEEN liste_tv.dureetv1 AND liste_tv.dureetv2 AND simulation_tele.name = liste_tv.name AND simulation_tele.emissiontele = liste_tv.emissiontv AND simulation_tele.timeslottele = liste_tv.timeslotprixtele AND liste_tv.ranglistetele = '0' AND simulation_tele.typetele = 'SPOT'",)
        prixtele = self.env.cr.execute("UPDATE public.simulation_tele SET prixtele = prixtv FROM public.liste_tv WHERE simulation_tele.dureetele BETWEEN liste_tv.dureetv1 AND liste_tv.dureetv2 AND simulation_tele.name = liste_tv.name AND simulation_tele.emissiontele = liste_tv.emissiontv AND simulation_tele.timeslottele = liste_tv.timeslotprixtele AND simulation_tele.rangtele = liste_tv.ranglistetele AND simulation_tele.typetele = 'SPOT'",)

        grpens = self.env.cr.execute("UPDATE public.simulation_tele SET grpens = tauxens FROM public.mm_ensemble WHERE simulation_tele.name = mm_ensemble.name AND simulation_tele.dayforgrp = mm_ensemble.jour AND simulation_tele.timeslotgrp = mm_ensemble.slotens")

        grpcsp = self.env.cr.execute("UPDATE public.simulation_tele SET grpcsp = tauxens FROM public.mm_csp WHERE simulation_tele.name = mm_csp.name AND simulation_tele.dayforgrp = mm_csp.jour AND simulation_tele.timeslotgrp = mm_csp.slotens")

        grppopact = self.env.cr.execute("UPDATE public.simulation_tele SET grppopact = tauxens FROM public.mm_popact WHERE simulation_tele.name = mm_popact.name AND simulation_tele.dayforgrp = mm_popact.jour AND simulation_tele.timeslotgrp = mm_popact.slotens")

        grpjeune = self.env.cr.execute("UPDATE public.simulation_tele SET grpjeune = tauxens FROM public.mm_jeune WHERE simulation_tele.name = mm_jeune.name AND simulation_tele.dayforgrp = mm_jeune.jour AND simulation_tele.timeslotgrp = mm_jeune.slotens")

        grpmf = self.env.cr.execute("UPDATE public.simulation_tele SET grpmf = tauxens FROM public.mm_mf WHERE simulation_tele.name = mm_mf.name AND simulation_tele.dayforgrp = mm_mf.jour AND simulation_tele.timeslotgrp = mm_mf.slotens")




    @api.depends('dayofdatetv')
    def _get_dayforgrp(self):
        for r in self:
            if r.dayofdatetv == 'dimanche':
                r.dayforgrp = 'dimanche'
            elif r.dayofdatetv == 'samedi':
                r.dayforgrp = 'samedi'
            else:
                r.dayforgrp = 'Semaine'


    @api.depends('timeofdatetv')
    def _timeslot3_definition(self):
        for r in self:
            if '03:00:00' <= r.timeofdatetv <= '06:00:00':
                r.timeslottele = '03H-06H'
            elif '06:00:00' <= r.timeofdatetv <= '08:59:59':
                r.timeslottele = '06H-09H'
            elif '09:00:00' <= r.timeofdatetv <= '11:59:59':
                r.timeslottele = '09H-12H'
            elif '12:00:00' <= r.timeofdatetv <= '14:59:59':
                r.timeslottele = '12H-15H'
            elif '15:00:00' <= r.timeofdatetv <= '17:59:59':
                r.timeslottele = '15H-18H'
            elif '18:00:00' <= r.timeofdatetv <= '20:59:59':
                r.timeslottele = '18H-21H'
            elif '21:00:00' <= r.timeofdatetv <= '23:59:59':
                r.timeslottele = '21H-00H'
            elif '00:00:00' <= r.timeofdatetv <= '02:59:59':
                r.timeslottele = '00H-03H'
            else:
                r.timeslottele = 'False'

    @api.depends('timeofdatetv')
    def _timeslot15_definition(self):
        for r in self:
            if '05:00:00' <= r.timeofdatetv <= '05:15:00':
                r.timeslotgrp = '5h00-5h15'
            elif '05:30:00' <= r.timeofdatetv <= '05:45:00':
                r.timeslotgrp = '5h30-5h45'
            elif '06:00:00' <= r.timeofdatetv <= '06:15:00':
                r.timeslotgrp = '6h00-6h15'
            elif '06:30:00' <= r.timeofdatetv <= '06:45:00':
                r.timeslotgrp = '6h30-6h45'
            elif '07:00:00' <= r.timeofdatetv <= '07:15:00':
                r.timeslotgrp = '7h00-7h15'
            elif '07:30:00' <= r.timeofdatetv <= '07:45:00':
                r.timeslotgrp = '7h30-7h45'
            elif '08:00:00' <= r.timeofdatetv <= '08:15:00':
                r.timeslotgrp = '8h00-8h15'
            elif '08:30:00' <= r.timeofdatetv <= '08:45:00':
                r.timeslotgrp = '8h30-8h45'
            elif '09:00:00' <= r.timeofdatetv <= '09:15:00':
                r.timeslotgrp = '9h00-9h15'
            elif '09:30:00' <= r.timeofdatetv <= '09:45:00':
                r.timeslotgrp = '9h30-9h45'
            elif '10:00:00' <= r.timeofdatetv <= '10:15:00':
                r.timeslotgrp = '10h00-10h15'
            elif '10:30:00' <= r.timeofdatetv <= '10:45:00':
                r.timeslotgrp = '10h30-10h45'
            elif '11:00:00' <= r.timeofdatetv <= '11:15:00':
                r.timeslotgrp = '11h00-11h15'
            elif '11:30:00' <= r.timeofdatetv <= '11:45:00':
                r.timeslotgrp = '11h30-11h45'
            elif '12:00:00' <= r.timeofdatetv <= '12:15:00':
                r.timeslotgrp = '12h00-12h15'
            elif '12:30:00' <= r.timeofdatetv <= '12:45:00':
                r.timeslotgrp = '12h30-12h45'
            elif '13:00:00' <= r.timeofdatetv <= '13:15:00':
                r.timeslotgrp = '13h00-13h15'
            elif '13:30:00' <= r.timeofdatetv <= '13:45:00':
                r.timeslotgrp = '13h30-13h45'
            elif '14:00:00' <= r.timeofdatetv <= '14:15:00':
                r.timeslotgrp = '14h00-14h15'
            elif '14:30:00' <= r.timeofdatetv <= '14:45:00':
                r.timeslotgrp = '14h30-14h45'
            elif '15:00:00' <= r.timeofdatetv <= '15:15:00':
                r.timeslotgrp = '15h00-15h15'
            elif '15:30:00' <= r.timeofdatetv <= '15:45:00':
                r.timeslotgrp = '15h30-15h45'
            elif '16:00:00' <= r.timeofdatetv <= '16:15:00':
                r.timeslotgrp = '16h00-16h15'
            elif '16:30:00' <= r.timeofdatetv <= '16:45:00':
                r.timeslotgrp = '16h30-16h45'
            elif '17:00:00' <= r.timeofdatetv <= '17:15:00':
                r.timeslotgrp = '17h00-17h15'
            elif '17:30:00' <= r.timeofdatetv <= '17:45:00':
                r.timeslotgrp = '17h30-17h45'
            elif '18:00:00' <= r.timeofdatetv <= '18:15:00':
                r.timeslotgrp = '18h00-18h15'
            elif '18:30:00' <= r.timeofdatetv <= '18:45:00':
                r.timeslotgrp = '18h30-18h45'
            elif '19:00:00' <= r.timeofdatetv <= '19:15:00':
                r.timeslotgrp = '19h00-19h15'
            elif '19:30:00' <= r.timeofdatetv <= '19:45:00':
                r.timeslotgrp = '19h30-19h45'
            elif '20:00:00' <= r.timeofdatetv <= '20:15:00':
                r.timeslotgrp = '20h00-20h15'
            elif '20:30:00' <= r.timeofdatetv <= '20:45:00':
                r.timeslotgrp = '20h30-20h45'
            elif '21:00:00' <= r.timeofdatetv <= '21:15:00':
                r.timeslotgrp = '21h00-21h15'
            elif '21:30:00' <= r.timeofdatetv <= '21:45:00':
                r.timeslotgrp = '21h30-21h45'
            elif '22:00:00' <= r.timeofdatetv <= '22:15:00':
                r.timeslotgrp = '22h00-22h15'
            elif '22:30:00' <= r.timeofdatetv <= '22:45:00':
                r.timeslotgrp = '22h30-22h45'
            elif '23:00:00' <= r.timeofdatetv <= '23:15:00':
                r.timeslotgrp = '23h00-23h15'
            elif '23:30:00' <= r.timeofdatetv <= '23:45:00':
                r.timeslotgrp = '23h30-23h45'
            elif '00:00:00' <= r.timeofdatetv <= '00:15:00':
                r.timeslotgrp = '0h00-0h15'
            elif '00:30:00' <= r.timeofdatetv <= '00:45:00':
                r.timeslotgrp = '0h30-0h45'
            elif '01:00:00' <= r.timeofdatetv <= '01:15:00':
                r.timeslotgrp = '1h00-1h15'
            elif '01:30:00' <= r.timeofdatetv <= '01:45:00':
                r.timeslotgrp = '1h30-1h45'
            elif '02:00:00' <= r.timeofdatetv <= '02:15:00':
                r.timeslotgrp = '2h00-2h15'
            elif '02:30:00' <= r.timeofdatetv <= '02:45:00':
                r.timeslotgrp = '2h30-2h45'
            elif '03:00:00' <= r.timeofdatetv <= '03:15:00':
                r.timeslotgrp = '3h00-3h15'
            elif '03:30:00' <= r.timeofdatetv <= '03:45:00':
                r.timeslotgrp = '3h30-3h45'
            elif '04:00:00' <= r.timeofdatetv <= '04:15:00':
                r.timeslotgrp = '4h00-4h15'
            elif '04:30:00' <= r.timeofdatetv <= '04:45:00':
                r.timeslotgrp = '4h30-4h45'
            elif '05:15:00' <= r.timeofdatetv <= '05:30:00':
                r.timeslotgrp = '5h15-5h30'
            elif '05:45:00' <= r.timeofdatetv <= '06:00:00':
                r.timeslotgrp = '5h45-6h00'
            elif '06:15:00' <= r.timeofdatetv <= '06:30:00':
                r.timeslotgrp = '6h15-6h30'
            elif '06:45:00' <= r.timeofdatetv <= '07:00:00':
                r.timeslotgrp = '6h45-7h00'
            elif '07:15:00' <= r.timeofdatetv <= '07:30:00':
                r.timeslotgrp = '7h15-7h30'
            elif '07:45:00' <= r.timeofdatetv <= '08:00:00':
                r.timeslotgrp = '7h45-8h00'
            elif '08:15:00' <= r.timeofdatetv <= '08:30:00':
                r.timeslotgrp = '8h15-8h30'
            elif '08:45:00' <= r.timeofdatetv <= '09:00:00':
                r.timeslotgrp = '8h45-9h00'
            elif '09:15:00' <= r.timeofdatetv <= '09:30:00':
                r.timeslotgrp = '9h15-9h30'
            elif '09:45:00' <= r.timeofdatetv <= '10:00:00':
                r.timeslotgrp = '9h45-10h00'
            elif '10:15:00' <= r.timeofdatetv <= '10:30:00':
                r.timeslotgrp = '10h15-10h30'
            elif '10:45:00' <= r.timeofdatetv <= '11:00:00':
                r.timeslotgrp = '10h45-11h00'
            elif '11:15:00' <= r.timeofdatetv <= '11:30:00':
                r.timeslotgrp = '11h15-11h30'
            elif '11:45:00' <= r.timeofdatetv <= '12:00:00':
                r.timeslotgrp = '11h45-12h00'
            elif '12:15:00' <= r.timeofdatetv <= '12:30:00':
                r.timeslotgrp = '12h15-12h30'
            elif '12:45:00' <= r.timeofdatetv <= '13:00:00':
                r.timeslotgrp = '12h45-13h00'
            elif '13:15:00' <= r.timeofdatetv <= '13:30:00':
                r.timeslotgrp = '13h15-13h30'
            elif '13:45:00' <= r.timeofdatetv <= '14:00:00':
                r.timeslotgrp = '13h45-14h00'
            elif '14:15:00' <= r.timeofdatetv <= '14:30:00':
                r.timeslotgrp = '14h15-14h30'
            elif '14:45:00' <= r.timeofdatetv <= '15:00:00':
                r.timeslotgrp = '14h45-15h00'
            elif '15:15:00' <= r.timeofdatetv <= '15:30:00':
                r.timeslotgrp = '15h15-15h30'
            elif '15:45:00' <= r.timeofdatetv <= '16:00:00':
                r.timeslotgrp = '15h45-16h00'
            elif '16:15:00' <= r.timeofdatetv <= '16:30:00':
                r.timeslotgrp = '16h15-16h30'
            elif '16:45:00' <= r.timeofdatetv <= '17:00:00':
                r.timeslotgrp = '16h45-17h00'
            elif '17:15:00' <= r.timeofdatetv <= '17:30:00':
                r.timeslotgrp = '17h15-17h30'
            elif '17:45:00' <= r.timeofdatetv <= '18:00:00':
                r.timeslotgrp = '17h45-18h00'
            elif '18:15:00' <= r.timeofdatetv <= '18:30:00':
                r.timeslotgrp = '18h15-18h30'
            elif '18:45:00' <= r.timeofdatetv <= '19:00:00':
                r.timeslotgrp = '18h45-19h00'
            elif '19:15:00' <= r.timeofdatetv <= '19:30:00':
                r.timeslotgrp = '19h15-19h30'
            elif '19:45:00' <= r.timeofdatetv <= '20:00:00':
                r.timeslotgrp = '19h45-20h00'
            elif '20:15:00' <= r.timeofdatetv <= '20:30:00':
                r.timeslotgrp = '20h15-20h30'
            elif '20:45:00' <= r.timeofdatetv <= '21:00:00':
                r.timeslotgrp = '20h45-21h00'
            elif '21:15:00' <= r.timeofdatetv <= '21:30:00':
                r.timeslotgrp = '21h15-21h30'
            elif '21:45:00' <= r.timeofdatetv <= '22:00:00':
                r.timeslotgrp = '21h45-22h00'
            elif '22:15:00' <= r.timeofdatetv <= '22:30:00':
                r.timeslotgrp = '22h15-22h30'
            elif '22:45:00' <= r.timeofdatetv <= '23:00:00':
                r.timeslotgrp = '22h45-23h00'
            elif '23:15:00' <= r.timeofdatetv <= '23:30:00':
                r.timeslotgrp = '23h15-23h30'
            elif '23:45:00' <= r.timeofdatetv <= '23:59:59':
                r.timeslotgrp = '23h45-00h00'
            elif '00:15:00' <= r.timeofdatetv <= '00:30:00':
                r.timeslotgrp = '0h15-0h30'
            elif '00:45:00' <= r.timeofdatetv <= '01:00:00':
                r.timeslotgrp = '0h45-1h00'
            elif '01:15:00' <= r.timeofdatetv <= '01:30:00':
                r.timeslotgrp = '1h15-1h30'
            elif '01:45:00' <= r.timeofdatetv <= '02:00:00':
                r.timeslotgrp = '1h45-2h00'
            elif '02:15:00' <= r.timeofdatetv <= '02:30:00':
                r.timeslotgrp = '2h15-2h30'
            elif '02:45:00' <= r.timeofdatetv <= '03:00:00':
                r.timeslotgrp = '2h45-3h00'
            elif '03:15:00' <= r.timeofdatetv <= '03:30:00':
                r.timeslotgrp = '3h15-3h30'
            elif '03:45:00' <= r.timeofdatetv <= '04:00:00':
                r.timeslotgrp = '3h45-4h00'
            elif '04:15:00' <= r.timeofdatetv <= '04:30:00':
                r.timeslotgrp = '4h15-4h30'
            elif '04:45:00' <= r.timeofdatetv <= '05:00:00':
                r.timeslotgrp = '4h45-5h00'
            else:
                r.timeslotgrp = 'False'

#Mise à jour prix grp rehetra
class Miseajourtv(models.Model):
    _name = 'maj.tele'

    name = fields.Char(string="Fictif")

    @api.multi
    @api.depends()
    def prix_tv_definition(self):
        prixtele = self.env.cr.execute("UPDATE public.brute_tele SET prixtele = prixtv FROM public.liste_tv WHERE brute_tele.dureetele BETWEEN liste_tv.dureetv1 AND liste_tv.dureetv2 AND brute_tele.name = liste_tv.name AND brute_tele.prixtele = 0 AND brute_tele.emissiontele = liste_tv.emissiontv AND brute_tele.timeslottele = liste_tv.timeslotprixtele AND brute_tele.rangtele = liste_tv.ranglistetele AND brute_tele.typetele = 'SPOT'",)
        prixtele = self.env.cr.execute("UPDATE public.brute_tele SET prixtele = prixtv FROM public.liste_tv WHERE brute_tele.dureetele BETWEEN liste_tv.dureetv1 AND liste_tv.dureetv2 AND brute_tele.name = liste_tv.name AND brute_tele.prixtele = 0 AND brute_tele.emissiontele = liste_tv.emissiontv AND brute_tele.timeslottele = liste_tv.timeslotprixtele AND liste_tv.ranglistetele = '0' AND brute_tele.typetele = 'SPOT'",)
        prixtele = self.env.cr.execute("UPDATE public.brute_tele SET prixtele = prixtv FROM public.liste_tv WHERE brute_tele.dureetele BETWEEN liste_tv.dureetv1 AND liste_tv.dureetv2 AND brute_tele.name = liste_tv.name AND brute_tele.prixtele = 0 AND brute_tele.emissiontele = liste_tv.emissiontv AND liste_tv.timeslotprixtele = '0' AND brute_tele.rangtele = liste_tv.ranglistetele AND brute_tele.typetele = 'SPOT'",)
        prixtele = self.env.cr.execute("UPDATE public.brute_tele SET prixtele = prixtv FROM public.liste_tv WHERE brute_tele.dureetele BETWEEN liste_tv.dureetv1 AND liste_tv.dureetv2 AND brute_tele.name = liste_tv.name AND brute_tele.prixtele = 0 AND brute_tele.emissiontele = liste_tv.emissiontv AND liste_tv.timeslotprixtele = '0' AND liste_tv.ranglistetele = '0' AND brute_tele.typetele = 'SPOT'",)

    @api.multi
    @api.depends()
    def prix_tv_all_definition(self):
        prixtele = self.env.cr.execute("UPDATE public.brute_tele SET prixtele = prixtv FROM public.liste_tv WHERE brute_tele.dureetele BETWEEN liste_tv.dureetv1 AND liste_tv.dureetv2 AND brute_tele.name = liste_tv.name AND brute_tele.emissiontele = liste_tv.emissiontv AND liste_tv.timeslotprixtele = '0' AND liste_tv.ranglistetele = '0' AND brute_tele.typetele = 'SPOT'",)
        prixtele = self.env.cr.execute("UPDATE public.brute_tele SET prixtele = prixtv FROM public.liste_tv WHERE brute_tele.dureetele BETWEEN liste_tv.dureetv1 AND liste_tv.dureetv2 AND brute_tele.name = liste_tv.name AND brute_tele.emissiontele = liste_tv.emissiontv AND liste_tv.timeslotprixtele = '0' AND brute_tele.rangtele = liste_tv.ranglistetele AND brute_tele.typetele = 'SPOT'",)
        prixtele = self.env.cr.execute("UPDATE public.brute_tele SET prixtele = prixtv FROM public.liste_tv WHERE brute_tele.dureetele BETWEEN liste_tv.dureetv1 AND liste_tv.dureetv2 AND brute_tele.name = liste_tv.name AND brute_tele.emissiontele = liste_tv.emissiontv AND brute_tele.timeslottele = liste_tv.timeslotprixtele AND liste_tv.ranglistetele = '0' AND brute_tele.typetele = 'SPOT'",)
        prixtele = self.env.cr.execute("UPDATE public.brute_tele SET prixtele = prixtv FROM public.liste_tv WHERE brute_tele.dureetele BETWEEN liste_tv.dureetv1 AND liste_tv.dureetv2 AND brute_tele.name = liste_tv.name AND brute_tele.emissiontele = liste_tv.emissiontv AND brute_tele.timeslottele = liste_tv.timeslotprixtele AND brute_tele.rangtele = liste_tv.ranglistetele AND brute_tele.typetele = 'SPOT'",)

    @api.multi
    @api.depends()
    def get_grp(self):
        grpens = self.env.cr.execute("UPDATE public.brute_tele SET grpens = tauxens FROM public.mm_ensemble WHERE brute_tele.name = mm_ensemble.name AND brute_tele.grpens = 0 AND brute_tele.dayforgrp = mm_ensemble.jour AND brute_tele.timeslotgrp = mm_ensemble.slotens AND brute_tele.moisgrp = mm_ensemble.mois")

    @api.multi
    @api.depends()
    def get_grp_all(self):
        grpens = self.env.cr.execute("UPDATE public.brute_tele SET grpens = tauxens FROM public.mm_ensemble WHERE brute_tele.name = mm_ensemble.name AND brute_tele.dayforgrp = mm_ensemble.jour AND brute_tele.timeslotgrp = mm_ensemble.slotens AND brute_tele.moisgrp = mm_ensemble.mois")

    @api.multi
    @api.depends()
    def get_grp_csp(self):
        grpcsp = self.env.cr.execute("UPDATE public.brute_tele SET grpcsp = tauxens FROM public.mm_csp WHERE brute_tele.name = mm_csp.name AND brute_tele.grpcsp = 0 AND brute_tele.dayforgrp = mm_csp.jour AND brute_tele.timeslotgrp = mm_csp.slotens AND brute_tele.moisgrp = mm_csp.mois")

    @api.multi
    @api.depends()
    def get_grp_all_csp(self):
        grpcsp = self.env.cr.execute("UPDATE public.brute_tele SET grpcsp = tauxens FROM public.mm_csp WHERE brute_tele.name = mm_csp.name AND brute_tele.dayforgrp = mm_csp.jour AND brute_tele.timeslotgrp = mm_csp.slotens AND brute_tele.moisgrp = mm_csp.mois")

    @api.multi
    @api.depends()
    def get_grp_popact(self):
        grppopact = self.env.cr.execute("UPDATE public.brute_tele SET grppopact = tauxens FROM public.mm_popact WHERE brute_tele.name = mm_popact.name AND brute_tele.grppopact = 0 AND brute_tele.dayforgrp = mm_popact.jour AND brute_tele.timeslotgrp = mm_popact.slotens AND brute_tele.moisgrp = mm_popact.mois")

    @api.multi
    @api.depends()
    def get_grp_all_popact(self):
        grppopact = self.env.cr.execute("UPDATE public.brute_tele SET grppopact = tauxens FROM public.mm_popact WHERE brute_tele.name = mm_popact.name AND brute_tele.dayforgrp = mm_popact.jour AND brute_tele.timeslotgrp = mm_popact.slotens AND brute_tele.moisgrp = mm_popact.mois")


    @api.multi
    @api.depends()
    def get_grp_jeune(self):
        grpjeune = self.env.cr.execute("UPDATE public.brute_tele SET grpjeune = tauxens FROM public.mm_jeune WHERE brute_tele.name = mm_jeune.name AND brute_tele.grpjeune = 0 AND brute_tele.dayforgrp = mm_jeune.jour AND brute_tele.timeslotgrp = mm_jeune.slotens AND brute_tele.moisgrp = mm_jeune.mois")

    @api.multi
    @api.depends()
    def get_grp_all_jeune(self):
        grpjeune = self.env.cr.execute("UPDATE public.brute_tele SET grpjeune = tauxens FROM public.mm_jeune WHERE brute_tele.name = mm_jeune.name AND brute_tele.dayforgrp = mm_jeune.jour AND brute_tele.timeslotgrp = mm_jeune.slotens AND brute_tele.moisgrp = mm_jeune.mois")


    @api.multi
    @api.depends()
    def get_grp_mf(self):
        grpmf = self.env.cr.execute("UPDATE public.brute_tele SET grpmf = tauxens FROM public.mm_mf WHERE brute_tele.name = mm_mf.name AND brute_tele.grpmf = 0 AND brute_tele.dayforgrp = mm_mf.jour AND brute_tele.timeslotgrp = mm_mf.slotens AND brute_tele.moisgrp = mm_mf.mois")

    @api.multi
    @api.depends()
    def get_grp_all_mf(self):
        grpmf = self.env.cr.execute("UPDATE public.brute_tele SET grpmf = tauxens FROM public.mm_mf WHERE brute_tele.name = mm_mf.name AND brute_tele.dayforgrp = mm_mf.jour AND brute_tele.timeslotgrp = mm_mf.slotens AND brute_tele.moisgrp = mm_mf.mois")

    @api.multi
    @api.depends()
    def modif_dayforgrp(self):
        timeslottele = self.env.cr.execute("UPDATE public.brute_tele SET timeslottele = '03H-06H' WHERE brute_tele.timeslottele = '3H-6H'")
        timeslottele = self.env.cr.execute("UPDATE public.brute_tele SET timeslottele = '06H-09H' WHERE brute_tele.timeslottele = '6H-9H'")
        timeslottele = self.env.cr.execute("UPDATE public.brute_tele SET timeslottele = '09H-12H' WHERE brute_tele.timeslottele = '9H-12H'")
        timeslottele = self.env.cr.execute("UPDATE public.brute_tele SET timeslottele = '21H-00H' WHERE brute_tele.timeslottele = '21H-0H'")
        timeslottele = self.env.cr.execute("UPDATE public.brute_tele SET timeslottele = '00H-03H' WHERE brute_tele.timeslottele = '0H-3H'")

        timeslotprixtele = self.env.cr.execute("UPDATE public.liste_tv SET timeslotprixtele = '03H-06H' WHERE liste_tv.timeslotprixtele = '3H-6H'")
        timeslotprixtele = self.env.cr.execute("UPDATE public.liste_tv SET timeslotprixtele = '06H-09H' WHERE liste_tv.timeslotprixtele = '6H-9H'")
        timeslotprixtele = self.env.cr.execute("UPDATE public.liste_tv SET timeslotprixtele = '09H-12H' WHERE liste_tv.timeslotprixtele = '9H-12H'")
        timeslotprixtele = self.env.cr.execute("UPDATE public.liste_tv SET timeslotprixtele = '21H-00H' WHERE liste_tv.timeslotprixtele = '21H-0H'")
        timeslotprixtele = self.env.cr.execute("UPDATE public.liste_tv SET timeslotprixtele = '00H-03H' WHERE liste_tv.timeslotprixtele = '0H-3H'")

        #dayforgrp = self.env.cr.execute("UPDATE public.brute_tele SET dayforgrp = 'Semaine'")
        #dayforgrp = self.env.cr.execute("UPDATE public.brute_tele SET dayforgrp = dayofdatetv WHERE brute_tele.dayofdatetv = 'samedi'")
        #dayforgrp = self.env.cr.execute("UPDATE public.brute_tele SET dayforgrp = dayofdatetv WHERE brute_tele.dayofdatetv = 'dimanche'")