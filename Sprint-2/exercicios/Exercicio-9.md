# E9
## Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.

```sql
SELECT 
  tbvendas.cdpro, 
  tbvendas.nmpro
FROM 
  tbvendas
JOIN 
  tbestoqueproduto ON tbvendas.cdpro = tbestoqueproduto.cdpro
WHERE 
  tbvendas.dtven BETWEEN '2014-02-03' AND '2018-02-02'
GROUP BY 
  tbvendas.cdpro, tbvendas.nmpro
ORDER BY 
  SUM(tbvendas.qtd) DESC
LIMIT 1;

```