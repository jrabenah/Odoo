# -*- coding: utf-8 -*-
from odoo import models, fields


class HelloRecord(models.Model):
    """
    Modèle de démonstration : un enregistrement "Hello".

    Convention Odoo : _name est un identifiant unique en minuscules avec des points.
    Ex: 'hello.record' -> table PostgreSQL 'hello_record' (les points deviennent des underscores).
    """
    _name = 'hello.record'
    _description = "Hello Record"

    # Champ texte court, obligatoire (required=True).
    # index=True ajoute un index PostgreSQL (utile si on filtre/regroupe souvent dessus).
    name = fields.Char(
        string="Titre",
        required=True,
        index=True,
    )

    # Champ texte long, optionnel.
    description = fields.Text(
        string="Description",
    )

    # Champ booléen, avec valeur par défaut.
    active = fields.Boolean(
        string="Actif",
        default=True,
    )