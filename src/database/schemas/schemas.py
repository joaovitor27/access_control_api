from src.database.schemas import schema_address, schema_establishment, schema_tag


def update_forward_refs():
    schema_address.update_forward_refs_address()
    schema_establishment.update_forward_refs_establishment()
    schema_tag.update_forward_refs_tag()
