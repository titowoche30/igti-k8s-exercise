import os
import time
import argparse
import pandas   as pd
import numpy    as np
from faker      import Faker
from sqlalchemy import create_engine
from datetime   import datetime
from dotenv     import load_dotenv

load_dotenv()

username = os.environ.get("POSTGRES_DATABASE_USER")
password = os.environ.get("POSTGRES_PASSWORD")
host     = os.environ.get("POSTGRES_HOST")
port     = os.environ.get("POSTGRES_PORT")
database = os.environ.get("POSTGRES_DATABASE")

# função para parsear a saída do parâmetro SILENT
def str2bool(v):
    if isinstance(v, bool):
       return v

    bool_dict = {'yes': True, 'true': True, 't': True ,'y': True, '1': True,
                 'no': False, 'false': False, 'f': False, 'n': False, '0': False}

    return bool_dict[v.lower()]

# Instancia a classe Faker
faker = Faker()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Generate fake data to customers table')

    parser.add_argument('--interval', type=int, default=0.005,
                        help='Interval of generating fake data in seconds')

    parser.add_argument('-n', type=int, default=1,
                        help='Sample size')

    parser.add_argument('--num-samples', '-ns', dest="num_samples", 
                        type=int, default=5,
                        help='Number of samples')
                        
    parser.add_argument('--connection-string', '-cs', dest="connection_string", 
                        type=str, default=f'postgresql://{username}:{password}@{host}:{port}/{database}',
                        help='Connection string to the database')

    parser.add_argument('--silent', type=str2bool, nargs='?',
                        const=True, default=False,
                        help="Print fake data")

    args = parser.parse_args()

    print(f"Args parsed:")
    print(f"Interval: {args.interval}")
    print(f"Sample size: {args.n}")
    print(f"Number of Samples: {args.num_samples}")
    print(f"Connection string: {args.connection_string}", end='\n\n')
    
    #-----------------------------------------------------------------

    engine = create_engine(args.connection_string)

    print("Iniciando a simulacao...", end="\n\n")

    # Gera dados fake a faz ingestão
    for _ in range(args.num_samples):
        nome       = [faker.name() for i in range(args.n)]
        gender     = [np.random.choice(["M", "F"], p=[0.5, 0.5]) for i in range(args.n)]
        endereco   = [faker.address() for i in range(args.n)]
        telefone   = [faker.phone_number() for i in range(args.n)]
        email      = [faker.safe_email() for i in range(args.n)]
        foto       = [faker.image_url() for i in range(args.n)]
        nascimento = [faker.date_of_birth() for i in range(args.n)]
        profissao  = [faker.job() for i in range(args.n)]
        dt_update  = [datetime.now() for i in range(args.n)]

        df = pd.DataFrame({
            "nome": nome,
            "sexo": gender,
            "endereco": endereco,
            "telefone": telefone,
            "email": email,
            "foto": foto,
            "nascimento": nascimento,
            "profissao": profissao,
            "dt_update": dt_update
        })

        df.to_sql('customers', con=engine, if_exists="append", index=False)

        if not args.silent:
            print(df, end="\n\n")

        time.sleep(args.interval)
        
    print("Fim da simulacao...")
