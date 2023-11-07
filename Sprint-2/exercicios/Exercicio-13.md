# E13
## Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

```sql
SELECT 
  tbvendas.cdpro,
  tbvendas.nmcanalvendas,
  tbvendas.nmpro,
  SUM(tbvendas.qtd) AS quantidade_vendas
FROM 
  tbvendas
JOIN 
  tbestoqueproduto ON tbvendas.cdpro = tbestoqueproduto.cdpro
WHERE 
  tbvendas.status = 'Concluído'
  AND (tbvendas.nmcanalvendas = 'Ecommerce' OR tbvendas.nmcanalvendas = 'Matriz')
GROUP BY 
  tbvendas.cdpro, tbvendas.nmcanalvendas, tbvendas.nmpro
ORDER BY 
  quantidade_vendas ASC
LIMIT 10;

```