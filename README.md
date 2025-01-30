# Reconhecimento de Celebridades com AWS Rekognition

Este projeto demonstra como utilizar o **Amazon Rekognition** para reconhecer celebridades em imagens e vídeos, aplicando técnicas de **machine learning** para análise avançada de imagens na AWS.

## Objetivo do Projeto
- Implementar um sistema de reconhecimento de celebridades utilizando **Amazon Rekognition**.
- Processar imagens e vídeos para detectar rostos conhecidos.
- Documentar o processo, insights e melhorias possíveis.

## Tecnologias Utilizadas
- **Python** 3.x
- **Boto3** (SDK AWS para Python)
- **Amazon Rekognition**
- **Amazon S3** (para armazenamento de imagens e vídeos)

## Configuração do Ambiente
1. Instale as dependências necessárias:
   ```bash
   pip install boto3
   ```
2. Configure suas credenciais AWS:
   ```bash
   aws configure
   ```
   - Insira sua `AWS Access Key ID` e `AWS Secret Access Key`.
   - Defina a região padrão de uso, como `us-east-1`.

## Implementação do Código
Abaixo está o código para detectar celebridades em uma imagem utilizando **Amazon Rekognition**:

```python
import boto3

def detectar_celebridades(imagem_s3):
    rekognition_client = boto3.client('rekognition')
    
    response = rekognition_client.recognize_celebrities(
        Image={'S3Object': {'Bucket': 'meu-bucket', 'Name': imagem_s3}}
    )
    
    celebridades = response.get('CelebrityFaces', [])
    if celebridades:
        for celeb in celebridades:
            print(f"Nome: {celeb['Name']}, Confiança: {celeb['MatchConfidence']:.2f}%")
    else:
        print("Nenhuma celebridade reconhecida na imagem.")

# Teste com uma imagem no S3
detectar_celebridades('imagem_teste.jpg')
```

## Como Executar
1. Envie uma imagem para um bucket no **Amazon S3**.
2. Atualize o nome do bucket no código.
3. Execute o script Python:
   ```bash
   python reconhecimento.py
   ```

## Aprendizados e Possíveis Melhorias
- **Aprendizados**
  - Uso do **Amazon Rekognition** para reconhecimento facial.
  - Processamento de imagens armazenadas no **Amazon S3**.
  - Interpretação de respostas JSON para extração de dados relevantes.

- **Possíveis Melhorias**
  - Integração com **Lambda** para processamento automático de novas imagens.
  - Implementação de um dashboard para exibição dos resultados.
  - Extensão do projeto para reconhecimento de emoções e análise de características faciais.

---

Este repositório faz parte do curso **"Reconhecimento de Celebridades com IA na AWS"** da **DIO**. Bons estudos! 🚀
