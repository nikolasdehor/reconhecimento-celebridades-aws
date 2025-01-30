import boto3
import pandas as pd
import matplotlib.pyplot as plt

def detectar_celebridades(imagem_s3, bucket):
    rekognition_client = boto3.client('rekognition')
    
    response = rekognition_client.recognize_celebrities(
        Image={'S3Object': {'Bucket': bucket, 'Name': imagem_s3}}
    )
    
    celebridades = response.get('CelebrityFaces', [])
    if celebridades:
        dados = []
        for celeb in celebridades:
            dados.append({'Nome': celeb['Name'], 'Confiança': celeb['MatchConfidence']})
        df = pd.DataFrame(dados)
        print(df)
        
        # Visualização de Confiança
        df.plot(x='Nome', y='Confiança', kind='bar', legend=False, color='blue')
        plt.ylabel('Confiança (%)')
        plt.title('Confiança na Identificação de Celebridades')
        plt.show()
    else:
        print("Nenhuma celebridade reconhecida na imagem.")

# Teste com uma imagem no S3
detectar_celebridades('imagem_teste.jpg', 'meu-bucket')
