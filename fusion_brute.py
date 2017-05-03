# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools

class Fusion(models.Model):
    _name = "fusion.brute"

    dispo = fields.Char(string="Dispositif")
    id2 = fields.Integer (string="ID2")
    datefusion = fields.Datetime(string="Date")
    namefusion = fields.Char(string="Chaine")
    category = fields.Char(string="Catégorie")
    secteur = fields.Char(string="Secteur")
    societe = fields.Char(string="SOCIETE")
    type = fields.Char(string="TYPE")
    emission = fields.Char(string="EMISSION")
    campagne = fields.Char(string="CAMPAGNE")
    version = fields.Char(string="VERSION")
    rang = fields.Char(string="RANG")
    duree = fields.Char (string="Format")
    timeslot = fields.Char(string="TRANCHE 3H")
    grpensfusion = fields.Float(string="GRP ENSEMBLE")
    prix = fields.Integer(string="Dépense")
    datesearch = fields.Date(string=" Date Recherche", compute="_date_definition")

    @api.depends('datefusion')
    def _date_definition(self):
        for r in self:
            dt_obj = datetime.strptime(r.datefusion,'%Y-%m-%d %H:%M:%S')
            if r.datesearch == 0:
                r.datesearch = datetime.strftime(dt_obj,'%Y-%m-%d')
            else:
                r.datesearch = 'False'

    


class Fusionner(models.Model):
    _name = "fusion.fusionner"

    name = fields.Char(string="Fictif")

    def fusion(self):
        self.env.cr.execute("""
            DELETE FROM public.fusion_brute;

            INSERT INTO fusion_brute 
                (id,dispo,category,namefusion,secteur,prix)
                SELECT
                    id,
                    'TV',
                    categorytele,
                    name,
                    secteurtele,
                    prixtele
                FROM 
                    brute_tele
            ON CONFLICT (id) DO UPDATE 
                SET dispo = 'TV';

            INSERT INTO fusion_brute 
                (id,id2,dispo,category,namefusion,secteur,prix)
                SELECT
                    (id+400000000),
                    id,
                    'RADIO',
                    categoryradio,
                    name,
                    secteurradio,
                    prixradio
                FROM 
                    brute_radio
            ON CONFLICT (id) DO UPDATE 
                SET dispo = 'RADIO';

            INSERT INTO fusion_brute 
                (id,dispo,category,namefusion,campagne,secteur,societe,version,type,duree,rang,datefusion,prix)
                SELECT
                    (id+900000000),
                    'PRESSE',
                    categorypr,
                    name,
                    campagnepr,
                    secteurpr,
                    societepr,
                    versionpr,
                    type,
                    format,
                    page,
                    datepr,
                    prix
                FROM 
                    brute_presse
            ON CONFLICT (id) DO UPDATE 
                SET dispo = 'PRESSE';

            UPDATE fusion_brute 
            SET 
            datefusion = date,
            namefusion = brute_tele.name,
            secteur = secteurtele,
            societe = societetele,
            type = typetele,
            emission = emissiontele,
            campagne = campagnetele,
            version = versiontele,
            rang = rangtele,
            duree = dureetele,
            timeslot = timeslottele,
            grpensfusion = brute_tele.grpens,
            prix = prixtele 
            FROM public.brute_tele 
            WHERE fusion_brute.id = brute_tele.id;

            UPDATE fusion_brute 
            SET 
            datefusion = brute_radio.date,
            namefusion = brute_radio.name,
            secteur = secteurradio,
            societe = societeradio,
            type = typeradio,
            emission = emissionradio,
            campagne = campagneradio,
            version = versionradio,
            rang = rangradio,
            duree = dureeradio,
            timeslot = timeslotradio,
            grpensfusion = brute_radio.grpens,
            prix = prixradio 
            FROM public.brute_radio 
            WHERE fusion_brute.id2 = brute_radio.id;
        """)