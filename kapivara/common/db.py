from main import db
from sqlalchemy.sql import func


class Descricao:
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text)


class Cor(db.Model, Descricao):
    pass


class Combustivel(db.Model, Descricao):
    pass


class Fabricante(db.Model, Descricao):
    pass


class Modelo(db.Model, Descricao):
    fabricante_id = db.Column(db.Integer, db.ForeignKey('fabricante.id'), nullable=False)
    fabricante = db.relationship('Fabricante', backref=db.backref('modelo', lazy=True))


class Veiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String)
    cor_id = db.Column(db.Integer, db.ForeignKey('cor.id'), nullable=False)
    cor = db.relationship('Cor', backref=db.backref('veiculo', lazy=True))
    combustivel_id = db.Column(db.Integer, db.ForeignKey('combustivel.id'), nullable=False)
    combustivel = db.relationship('Combustivel', backref=db.backref('veiculo', lazy=True))
    fabricante_id = db.Column(db.Integer, db.ForeignKey('fabricante.id'), nullable=False)
    fabricante = db.relationship('Fabricante', backref=db.backref('veiculo', lazy=True))
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)
    modelo = db.relationship('Modelo', backref=db.backref('veiculo', lazy=True))


class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime(timezone=True), default=func.now())
    observacao = db.Column(db.Text)
    veiculo_id = db.Column(db.Integer, db.ForeignKey('veiculo.id'), nullable=False)
    veiculo = db.relationship('Veiculo', backref=db.backref('historico', lazy=True))


class HistoricoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text)
    observacao = db.Column(db.Text)
    historico_id = db.Column(db.Integer, db.ForeignKey('historico.id'), nullable=False)
    historico = db.relationship('historico', backref=db.backref('historico_item', lazy=True))


class Orcamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime(timezone=True), default=func.now())
    status = db.Column(db.String)


class OrcamentoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text)
    valor = db.Column(db.Numeric(precision=2))
    quantidade = db.Column(db.Integer)
    orcamento_id = db.Column(db.Integer, db.ForeignKey('orcamento.id'), nullable=False)
    orcamento = db.relationship('veiculo', backref=db.backref('orcamento_item', lazy=True))


class CupomNaoFiscal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime(timezone=True), default=func.now())
    valor_total = db.Column(db.Numeric(precision=2))


class CupomItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cupom_nao_fiscal_id = db.Column(db.Integer, db.ForeignKey('cupom_nao_fiscal.id'), nullable=False)
    cupom_nao_fiscal = db.relationship('cupom_item', backref=db.backref('cupom_item', lazy=True))
