def usuario_autenticado(request):
    return {
        'user_authenticated': 'usuario' in request.session
    }