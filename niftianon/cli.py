from __future__ import absolute_import
import click
import niftianon.anonymiser


@click.command()
@click.argument('identifiable_image', type=click.Path(exists=True))
@click.argument('anonymised_image', type=click.Path(exists=False))
def anonymise(identifiable_image, anonymised_image):
    niftianon.anonymiser.anonymise(identifiable_image, anonymised_image)
