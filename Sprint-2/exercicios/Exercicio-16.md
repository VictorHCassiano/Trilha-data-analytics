# E16
## Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).

Obs: Somente vendas concluídas.

```sql
SELECT 
  tbvendas.estado,
  tbvendas.nmpro,
  ROUND(AVG(tbvendas.qtd), 4) AS quantidade_media
FROM 
  tbvendas
JOIN 
  tbestoqueproduto ON tbvendas.cdpro = tbestoqueproduto.cdpro
WHERE 
  tbvendas.status = 'Concluído'
GROUP BY 
  tbvendas.estado, tbvendas.nmpro
ORDER BY 
  tbvendas.estado ASC, tbvendas.nmpro ASC;

```