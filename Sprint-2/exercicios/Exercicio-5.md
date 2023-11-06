# E5
### Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.
``` sql
SELECT DISTINCT autor.nome
FROM autor
JOIN livro ON autor.codautor = livro.autor
JOIN editora ON livro.editora = editora.codeditora
LEFT JOIN endereco ON editora.endereco = endereco.codendereco
WHERE UPPER(endereco.estado) NOT IN ('PARANÁ', 'SANTA CATARINA', 'RIO GRANDE DO SUL') OR endereco.estado IS NULL
ORDER BY autor.nome ASC;

```