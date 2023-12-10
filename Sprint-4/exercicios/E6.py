def maiores_que_media(conteudo: dict) -> list:
    media = sum(conteudo.values()) / len(conteudo)
    return sorted([(key, value) for key, value in conteudo.items() if value > media], key=lambda x: x[1])
