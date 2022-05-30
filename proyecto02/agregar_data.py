from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import enlace

engine = create_engine(enlace)

from app import Docente

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objetos de tipo Docente
docente1 = Docente(nombre="Tony", placa="LBA-120", \
        año="2006",costo="150$")

docente2 = Docente(nombre="Ana", placa="LBA-350", \
        año="2011",costo="150$")

docente3 = Docente(nombre="Luis", placa="LBA-809", \
        año="2013",costo="200$")


# se agrega los objetos
# a la sesión
# a la espera de un commit
# para agregar un registro a la base de
# datos
session.add(docente1)
session.add(docente2)
session.add(docente3)

# se confirma las transacciones
session.commit()
