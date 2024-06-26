#!/bin/bash

# SPDX-FileCopyrightText: Stichting Health-RI 2024
#
# SPDX-License-Identifier: Apache-2.0

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE ROLE "$REMS_DB_USER" NOSUPERUSER CREATEDB CREATEROLE LOGIN PASSWORD '$REMS_DB_PASSWORD';
    CREATE DATABASE "$REMS_DB" OWNER "$REMS_DB_USER" ENCODING 'utf-8';
EOSQL
