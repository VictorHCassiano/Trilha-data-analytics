# E12
## Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.


Observação: Apenas vendas com status concluído.

```sql
SELECT 
  tbdependente.cddep,
  tbdependente.nmdep,
  tbdependente.dtnasc,
  ROUND(SUM(tbvendas.qtd * tbvendas.vrunt), 2) AS valor_total_vendas
FROM 
  tbdependente
JOIN 
  tbvendedor ON tbdependente.cdvdd = tbvendedor.cdvdd
JOIN 
  tbvendas ON tbvendedor.cdvdd = tbvendas.cdvdd
WHERE 
  tbvendas.status = 'Concluído'
GROUP BY 
  tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc
HAVING 
  valor_total_vendas > 0
ORDER BY 
  valor_total_vendas ASC
LIMIT 1;

```