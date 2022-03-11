from kim import Mapper, field

from example.models import PromoSale, Prize, Participant, Result


class PromoSaleMapper(Mapper):
    __type__ = PromoSale

    id = field.Integer(read_only=True)
    name = field.String()
    description = field.String()
    prizes = field.Field()


class CharacterMapper(Mapper):
    __type__ = Prize

    id = field.Integer(read_only=True)
    description = field.String()


class ParticipantMapper(Mapper):
    __type__ = Participant

    id = field.Integer(read_only=True)
    name = field.String()
    promosale_id = field.Field()


class ResultMapper(Mapper):
    __type__ = Result

    winner = field.Integer(read_only=True)
    prize = field.String()
