from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))
template = env.get_template(TEMPLATE)

def render_message(ad, slots):
    """Génère un message personnalisé, propose deux créneaux."""
    return template.render(
        title=ad["subject"],
        price=ad["price"],
        url=ad["url"],
        slots=slots
    )
