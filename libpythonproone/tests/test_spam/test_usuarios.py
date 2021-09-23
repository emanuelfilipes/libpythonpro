from libpythonproone.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Emanuel', email='Emanuelfilipess@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='Emanuel', email='Emanuelfilipess@gmail.com'),
        Usuario(nome='Renzo', email='renzo@python.pro.br')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
