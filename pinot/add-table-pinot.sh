#! /usr/bin/env bash


kubectl cp pinot/schema_configuration/customers-schema.json datastorage/pinot-controller-0:/opt/pinot

kubectl cp pinot/schema_configuration/customers-table.json datastorage/pinot-controller-0:/opt/pinot

kubectl exec pinot-controller-0 -n datastorage -it -- bash -c 'bin/pinot-admin.sh AddTable -schemaFile /opt/pinot/customers-schema.json -tableConfigFile /opt/pinot/customers-table.json -exec'
