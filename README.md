# pdf_parser

To run project execute commands (docker required)
```shell script
cd {path/to/project/root}
docker-compose up pdf_parser
make migrate
```

Available urls:


POST http://localhost:8080/documents - link to upload pdf document

`curl -F "document=@{full/path/to/file}" http://localhost:8080/documents`

GET http://localhost:8080/links - return list of links

`curl http://localhost:8080/links`

GET http://localhost:8080/documents - return list of uploaded documents

`curl http://localhost:8080/documents`

GET http://localhost:8080/documents/{document_id}/links - return list of links founded in document

`curl http://localhost:8080/documents/{document_id}/links`
```

