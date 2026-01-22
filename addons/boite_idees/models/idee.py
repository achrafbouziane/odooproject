from odoo import models, fields

class Idee(models.Model):
    _name = "boite.idee"
    _description = "Idée proposée"

    name = fields.Char(string="Titre de l'idée", required=True)
    auteur = fields.Char(string="Auteur", default="Anonyme")
    description = fields.Text(string="Description détaillée")
    date_creation = fields.Date(string="Date de proposition", default=fields.Date.context_today)
    
    categorie = fields.Selection([
        ('amelioration', 'Amélioration Continue'),
        ('nouveau_produit', 'Nouveau Produit'),
        ('bien_etre', 'Bien-être au travail'),
        ('autre', 'Autre'),
    ], string="Catégorie", default='autre')

    statut = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('soumise', 'Soumise'),
        ('approuvee', 'Approuvée'),
        ('refusee', 'Refusée'),
        ('realisee', 'Réalisée'),
    ], string="Statut", default='brouillon')
    
    vote_count = fields.Integer(string="Nombre de votes", default=0)