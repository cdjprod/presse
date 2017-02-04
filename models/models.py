# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta, datetime

class brutepresse(models.Model):
	_name ='brute.presse'

	name = fields.Char(string="Titre", index=True)
	datepr = fields.Date(string="Date", default=fields.Date.today)
	dayofdatepr = fields.Char(string="Jour", compute="_date_definition_pr", store="True")
	secteurpr = fields.Char(string="Secteur")
	societepr = fields.Char(string="Societe")
	campagnepr = fields.Char(string="Campagne")
	versionpr = fields.Char(string="Version")
	format = fields.Char(string="Format")
	type = fields.Char(string="Type")
	page = fields.Char(string="N° Page")
	prix = fields.Integer(string="Valeur insertion", default=0)
	dayforprice = fields.Char(string="Jour PRIX", compute="_get_dayforprice_pr", store="True")

	@api.depends('datepr')
	def _date_definition_pr(self):
		for r in self:
			dt_obj = datetime.strptime(r.datepr,'%Y-%m-%d')
			if r.dayofdatepr == 0:
				r.dayofdatepr = datetime.strftime(dt_obj,'%A')
			else:
				r.dayofdatepr = 'False'

	@api.depends('dayofdatepr')
	def _get_dayforprice_pr(self):
		for r in self:
			if r.dayofdatepr == 'dimanche':
				r.dayforprice = 'dimanche'
			elif r.dayofdatepr == 'samedi':
				r.dayforprice = 'samedi'
			else:
				r.dayforprice = 'semaine'


class listepresse(models.Model):
	_name ='liste.presse'

	name = fields.Char(string="Titre")
	jourpr = fields.Char(string="Jour")
	format = fields.Char(string="Format")
	type = fields.Char(string="Type")
	prixpage = fields.Char(string="Prix Page")
	prixform = fields.Integer(string="Prix format")


class Miseajour(models.Model):

	_name ='maj.presse'

	name = fields.Char(string="Fictif")

	@api.multi
	@api.depends()
	def prix_definition(self):
		prix = self.env.cr.execute("UPDATE public.brute_presse SET prix = prixform FROM public.liste_presse WHERE brute_presse.prix = 0 AND liste_presse.format = brute_presse.format AND brute_presse.page = liste_presse.prixpage AND brute_presse.dayforprice = liste_presse.jourpr AND brute_presse.name = liste_presse.name AND brute_presse.type = liste_presse.type",)
		prix = self.env.cr.execute("UPDATE public.brute_presse SET prix = prixform FROM public.liste_presse WHERE brute_presse.prix = 0 AND liste_presse.format = brute_presse.format AND liste_presse.prixpage ='0' AND brute_presse.dayforprice = liste_presse.jourpr AND brute_presse.name = liste_presse.name AND brute_presse.type = liste_presse.type",)

	@api.multi
	@api.depends()
	def prixall_definition(self):
		prix = self.env.cr.execute("UPDATE public.brute_presse SET prix = prixform FROM public.liste_presse WHERE liste_presse.format = brute_presse.format AND liste_presse.prixpage ='0' AND brute_presse.dayforprice = liste_presse.jourpr AND brute_presse.name = liste_presse.name AND brute_presse.type = liste_presse.type",)
		prix = self.env.cr.execute("UPDATE public.brute_presse SET prix = prixform FROM public.liste_presse WHERE liste_presse.format = brute_presse.format AND brute_presse.page = liste_presse.prixpage AND brute_presse.dayforprice = liste_presse.jourpr AND brute_presse.name = liste_presse.name AND brute_presse.type = liste_presse.type",)


# class presse(models.Model):
#     _name = 'presse.presse'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100