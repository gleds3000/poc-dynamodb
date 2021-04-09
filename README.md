# poc-dynamodb

essa poc constiste em teste via CLI 

no arquivo de readme deve conter commandos usados no CLI devidamente documentados 

Incluindo  tabela -- sua massa -- e as acoes que serão validas como GET ITEM PUT ITEM - QUERY  - Scan 


Bem como na reducao de custo toda infra aqui validada sera usando um docker do DynamoDB local 

Como subir um docker do Dynamodb tbm estará aqui 



---- FOCO ERRAR ERRAR novamente  E Validar o conceito


---- TABLE Movies 

COMAMNDO create table 


----MASSA FILMES IMDB 

--- movieload.json


---- TEM uma poc em python  e uma em nodejs para ajudar alguns conceitos 
----Python 
---valida conexao local 

---NoDE
valida leitura de dados e importcao de massa para tabela especifica. 


---- E tambem em JAVA. 
CRUD foco na validacao de QUERY e GetItem





---  Caso queira contribuir só mandar sua issue.


Att GLEDS3000



---------------

aws dynamodb query  \
     --endpoint-url http://localhost:8000 \
     --table-name Movies    \
    --key-condition-expression "#yr = :yyyy"     \
    --expression-attribute-names '{"#yr": "year"}'     \
   --expression-attribute-values  '{ ":yyyy":{"N":"2010"}}' \
 --filter-expression 'info.rating > :rating' \
--expression-attribute-values '{
   ":yyyy":{"N":"2010"},
    ":rating": { "N": "8.5" }
}'

---Motivo 
info.rating --- usado/chamado da mesma forma em qq json.  



===============
# 8001 aws dynamodb query
--endpoint-url http://localhost:8001
--table-name Movies
--key-condition-expression "#yr = :yyyy"
--expression-attribute-names '{"#yr": "year"}'
--expression-attribute-values '{ ":yyyy":{"N":"2010"}}'
--filter-expression 'info.rating > :rating'
--expression-attribute-values '{ ":yyyy":{"N":"2010"}, ":rating": { "N": "8.5" } }'

#PADRAO

aws dynamodb query
--endpoint-url http://localhost:8000
--table-name Movies
--key-condition-expression "#yr = :yyyy"
--expression-attribute-names '{"#yr": "year"}'
--expression-attribute-values '{ ":yyyy":{"N":"2010"}}'
--filter-expression 'info.rating > :rating'
--expression-attribute-values '{ ":yyyy":{"N":"2010"}, ":rating": { "N": "8.5" } }'


