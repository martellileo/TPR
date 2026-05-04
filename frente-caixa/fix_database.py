from database import Session, engine
from sqlalchemy import text

db = Session()

try:
    # Remover a chave estrangeira
    print("Removendo chave estrangeira...")
    db.execute(text("ALTER TABLE itemvenda DROP FOREIGN KEY itemvenda_ibfk_2"))
    db.commit()
    print("✓ Chave estrangeira removida")
    
    # Alterar a coluna
    print("Alterando coluna idItem...")
    db.execute(text("ALTER TABLE item MODIFY COLUMN idItem INT AUTO_INCREMENT"))
    db.commit()
    print("✓ Coluna alterada")
    
    # Alterar a coluna em itemvenda também
    print("Alterando coluna idItem na tabela itemvenda...")
    db.execute(text("ALTER TABLE itemvenda MODIFY COLUMN idItem INT"))
    db.commit()
    print("✓ Coluna itemvenda alterada")
    
    # Recriar a chave estrangeira
    print("Recriando chave estrangeira...")
    db.execute(text("ALTER TABLE itemvenda ADD CONSTRAINT itemvenda_ibfk_2 FOREIGN KEY (idItem) REFERENCES item(idItem)"))
    db.commit()
    print("✓ Chave estrangeira recriada")
    
    print("\n✅ Banco de dados corrigido com sucesso!")
    
except Exception as e:
    print(f"❌ Erro: {e}")
    db.rollback()
finally:
    db.close()
