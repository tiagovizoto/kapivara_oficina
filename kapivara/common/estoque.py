from main import db


class Fornecedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String)
    telefone = db.Column(db.String)
    ramo_social = db.Column(db.String)


class Estoque(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Numeric(precision=2))
    lucro = db.Column(db.Float)
    km_validade = db.Column(db.Float)
    data_validade = db.Column(db.DateTime)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id'), nullable=False)
    fornecedor = db.relationship('Fornecedor', backref=db.backref('veiculo', lazy=True))
