email_template = """
    Olá, %(nomes)s
    
    Tem interesse em comprar %(item)s?
    
    Este produto é capaz de %(solucao)s
    
    Clique agora em %(link)s
    
    Lembre-se, estamos com baixo estoque temos apenas %(unidades)i!
    
    Preço promocional de %(preco).2f
"""



for cliente in clientes:
    print(
        email_template
        % {
            "nomes" : cliente,
            "item" : "batata",
            "solucao" : "matar a larica da madruga",
            "link" : "batatinhaazul.com",
            "unidades" : 1,
            "preco" : 40.40,
        }
    )
    