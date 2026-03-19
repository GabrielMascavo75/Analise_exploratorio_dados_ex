import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Usar backend não-interativo
import matplotlib.pyplot as plt


def carregar_dados(caminho):
    """Carrega o dataset."""
    df = pd.read_csv(caminho, encoding='ISO-8859-1', sep=';')
    return df


def verificacao_dados(df):
    """Verificação de valores nulos e duplicados."""
    print("\n=== Verificação de Valores Nulos ===")
    print(df.isnull().sum())

    print("\n=== Verificação de Valores Duplicados ===")
    print("Total:", df.duplicated().sum())

    print("\nPercentual de nulos:")
    print((df.isnull().sum() / len(df)) * 100)


def tabela_frequencia(df):
    """Frequência absoluta e relativa das espécies."""
    print("\n=== Frequência Absoluta ===")
    print(df['Species'].value_counts())

    print("\n=== Frequência Relativa ===")
    print(df['Species'].value_counts(normalize=True))


def estatisticas(df):
    """Medidas estatísticas."""
    print("\n=== MÉDIA ===")
    print(df.mean(numeric_only=True))

    print("\n=== MEDIANA ===")
    print(df.median(numeric_only=True))

    print("\n=== DESVIO PADRÃO ===")
    print(df.std(numeric_only=True))

    print("\n=== VARIÂNCIA ===")
    print(df.var(numeric_only=True))

    print("\n=== Média da pétala por espécie ===")
    print(df.groupby('Species')['Petal.Length'].mean())


def graficos(df, output_dir= os.path.join(os.path.dirname(__file__), "meus_plots")):
    """Visualizações gráficas.

    Args:
        df: DataFrame com os dados.
        output_dir: Diretório onde os arquivos PNG serão salvos.
    """

    # garante que o diretório exista
    os.makedirs(output_dir, exist_ok=True)

    # Barras
    df['Species'].value_counts().plot(kind='bar')
    plt.title("Quantidade de cada espécie")
    plt.xlabel("Espécie")
    plt.ylabel("Quantidade")
    plt.savefig(os.path.join(output_dir, 'barras.png'))
    plt.close()

    # Pizza
    df['Species'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title("Proporção das espécies")
    plt.ylabel("")
    plt.savefig(os.path.join(output_dir, 'pizza.png'))
    plt.close()

    # Histograma
    plt.hist(df['Petal.Length'], bins=20)
    plt.title("Distribuição do comprimento da pétala")
    plt.xlabel("Petal Length")
    plt.ylabel("Frequência")
    plt.savefig(os.path.join(output_dir, 'histograma.png'))
    plt.close()

    # Boxplot
    df.boxplot(column='Sepal.Width', by='Species')
    plt.title("Largura da sépala por espécie")
    plt.suptitle("")
    plt.xlabel("Espécie")
    plt.ylabel("Sepal Width")
    plt.savefig(os.path.join(output_dir, 'boxplot.png'))
    plt.close()


def main():
    caminho = os.path.join(os.path.dirname(__file__), "iris.csv")

    df = carregar_dados(caminho)

    verificacao_dados(df)
    tabela_frequencia(df)
    estatisticas(df)
    graficos(df, output_dir=os.path.join(os.path.dirname(__file__), "plots"))

if __name__ == "__main__":
    main()
