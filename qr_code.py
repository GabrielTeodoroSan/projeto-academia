from datetime import datetime

import segno


def generate_qr_code(ticket_id: int):
    path = f"./images/{datetime.now().microsecond}.png"
    qr = segno.make_qr(ticket_id)
    qr.save(path)
    return path