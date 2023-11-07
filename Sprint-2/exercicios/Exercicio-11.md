# E11
## Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.

```sql
SELECT 
  tbvendas.cdcli,
  tbvendas.nmcli,
  ROUND(SUM(tbvendas.qtd * tbvendas.vrunt), 2) AS gasto
FROM 
  tbvendas
WHERE 
  tbvendas.status = 'Concluído'
GROUP BY 
  tbvendas.cdcli, tbvendas.nmcli
ORDER BY 
  gasto DESC
LIMIT 1;
```
