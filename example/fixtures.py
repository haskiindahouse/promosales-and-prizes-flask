def run():
    from example.app import app
    from example.models import db, PromoSale

    with app.test_request_context():
        db.drop_all()
        db.create_all()
        db.session.add(PromoSale(id=1, name='Тестовая акция 1', description="Описание 1"))
        db.session.add(PromoSale(id=2,  name='Тестовая акция 2', description="Описание 2"))
        db.session.add(PromoSale(id=2,  name='Тестовая акция 3', description="Описание 3"))
        db.session.add(PromoSale(id=2,  name='Тестовая акция 4', description="Описание 4"))
        db.session.add(PromoSale(id=2,  name='Тестовая акция 5', description="Описание 5"))

        db.session.commit()


if __name__ == "__main__":

    run()
