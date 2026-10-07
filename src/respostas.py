# =====================================================================
# SUAS RESPOSTAS
# =====================================================================
# Escreva cada consulta SQL entre as aspas triplas, assim:
#
#   Q1 = """
#   SELECT ...
#   FROM ...
#   """
#
# Depois salve o arquivo (Ctrl+S) e veja o resultado no painel.
# Mexa só no que está ENTRE as aspas triplas.
# =====================================================================

# ---------------------------------------------------------------------
# NÍVEL 1 - AQUECIMENTO
# ---------------------------------------------------------------------

# Q1. Clientes no Centro
# Colunas do resultado: ClientesNoCentro
Q1 = """
SELECT COUNT(*) AS ClientesNoCentro
FROM Clientes
WHERE Bairro = 'Centro';
"""

# Q2. Hambúrgueres acima de R$ 30
# Colunas do resultado: NomeProduto, Preco
Q2 = """
SELECT NomeProduto, Preco
FROM Produtos
WHERE Categoria = 'Hambúrguer' AND Preco > 30.00
ORDER BY Preco DESC;

"""

# Q3. Pedidos por status
# Colunas do resultado: Status, QuantidadePedidos
Q3 = """

SELECT Status, COUNT(*) AS QuantidadePedidos
FROM Pedidos
WHERE Status IN ('Entregue', 'Cancelado')
GROUP BY Status;

"""

# Q4. Nota média e pedidos sem avaliação
# Colunas do resultado: PedidosEntregues, PedidosAvaliados, PedidosSemAvaliacao, NotaMedia
Q4 = """
SELECT COUNT(*) AS PedidosEntregues,
COUNT(Avaliacao) AS PedidosAvaliados,
COUNT(*) - COUNT(Avaliacao) AS  PedidosSemAvaliacao,
CAST(AVG(CAST(Avaliacao AS DECIMAL(10,2))) AS DECIMAL(10,2)) AS NotaMedia
FROM Pedidos
WHERE Status = 'Entregue';
"""

# Q5. Delivery x Retirada por mês
# Colunas do resultado: Mes, TipoEntrega, QuantidadePedidos
Q5 = """
SELECT YEAR(DataPedido) AS AnoPedido,
MONTH(DataPedido) AS Mes, TipoEntrega,
COUNT(*) AS QuantidadePedidos
FROM Pedidos
WHERE Status = 'Entregue' AND TipoEntrega IN ('Delivery', 'Retirada')
GROUP BY YEAR(DataPedido), MONTH(DataPedido), TipoEntrega
ORDER BY YEAR(DataPedido), MONTH(DataPedido), TipoEntrega;

"""

# ---------------------------------------------------------------------
# NÍVEL 2 - CRUZANDO TABELAS
# ---------------------------------------------------------------------

# Q6. Pedidos de janeiro com cliente
# Colunas do resultado: IdPedido, DataPedido, Nome, Bairro, Status
Q6 = """
SELECT Pedidos.IdPedido, Pedidos.DataPedido, Clientes.Nome, Clientes.Bairro, Pedidos.Status
FROM Pedidos
INNER JOIN Clientes
ON Pedidos.IdCliente = Clientes.IdCliente
WHERE Pedidos.DataPedido >= '2026-01-01' AND Pedidos.DataPedido < '2026-02-01'
ORDER BY Pedidos.DataPedido ASC;
"""

# Q7. Entregas por entregador
# Colunas do resultado: Nome, Entregas
Q7 = """

 SELECT Entregadores.Nome,
COUNT(Pedidos.IdPedido) AS Entregas
FROM Entregadores
INNER JOIN Pedidos ON Pedidos.IdEntregador = Entregadores.IdEntregador
WHERE Pedidos.Status = 'Entregue'
GROUP BY Entregadores.Nome
ORDER BY Entregas DESC;

"""

# Q8. Unidades e faturamento por produto
# Colunas do resultado: NomeProduto, UnidadesVendidas, Faturamento
Q8 = """SELECT Produtos.NomeProduto,
SUM(ItensPedido.Quantidade) AS UnidadesVendidas,
SUM(ItensPedido.Quantidade * ItensPedido.PrecoUnitario) AS TotalFaturado
FROM Pedidos
INNER JOIN ItensPedido ON Pedidos.IdPedido = ItensPedido.IdPedido
INNER JOIN Produtos ON ItensPedido.IdProduto = Produtos.IdProduto
WHERE Pedidos.Status = 'Entregue'
GROUP BY Produtos.NomeProduto
ORDER BY UnidadesVendidas DESC;

"""

# Q9. Faturamento por categoria
# Colunas do resultado: Categoria, Faturamento
Q9 = """
SELECT Produtos.Categoria,
SUM(ItensPedido.Quantidade * ItensPedido.PrecoUnitario) AS TotalFaturado
FROM Pedidos
INNER JOIN ItensPedido ON Pedidos.IdPedido = ItensPedido.IdPedido
INNER JOIN Produtos ON ItensPedido.IdProduto = Produtos.IdProduto
WHERE Pedidos.Status = 'Entregue'
GROUP BY Produtos.Categoria
ORDER BY TotalFaturado DESC;

"""

# Q10. Bairros com 7+ pedidos entregues
# Colunas do resultado: Bairro, PedidosEntregues
Q10 = """
SELECT Clientes.Bairro,
COUNT(*) AS EntregasPorBairro
FROM Pedidos
INNER JOIN Clientes ON Clientes.IdCliente = Pedidos.IdCliente
WHERE Pedidos.Status = 'Entregue'
GROUP BY Clientes.Bairro
HAVING COUNT(*) >= 7;

"""

# Q11. Preços praticados do X-Bacon
# Colunas do resultado: PrecoUnitario, Unidades, Faturamento
Q11 = """

"""

# ---------------------------------------------------------------------
# NÍVEL 3 - DESAFIO
# ---------------------------------------------------------------------

# Q12. Top 3 clientes (fidelidade)
# Colunas do resultado: Nome, Pedidos, TotalGasto
Q12 = """

"""

# Q13. Faturamento mês a mês
# Colunas do resultado: Mes, PedidosEntregues, Faturamento
Q13 = """

"""

# Q14. Entregador do trimestre
# Colunas do resultado: Nome, Entregas, NotaMedia
Q14 = """

"""

# Q15. Valor total dos pedidos de março
# Colunas do resultado: IdPedido, Nome, ValorProdutos, TaxaEntrega, ValorTotal
Q15 = """

"""

# Q16. Clientes sem nenhum pedido
# Colunas do resultado: Nome, Bairro, DataCadastro
Q16 = """

"""

# Q17. Produto que nunca foi vendido
# Colunas do resultado: NomeProduto, Categoria, Preco
Q17 = """

"""

