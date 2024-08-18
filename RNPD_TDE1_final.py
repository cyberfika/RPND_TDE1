# Aluno: Jafte Carneiro Fagundes da Silva
'''
ENUNCIADO
Este programa, quando executado, irá ler um arquivo .txt que contém conjuntos e irá apresentar os resultados de operações
U, I, D, C que serão realizadas entre dois conjuntos de dados. O arquivo de entrada principal se chama "data1.txt" e os
3 arquivos de entrada de testes se chamam "random_test_*.txt", todos presentes no diretório "data".
'''

# Função que realiza a operação especificada entre dois conjuntos

def calculateOperation(opCode, set1, set2):
    # Converte as strings recebidas em conjuntos, separando os elementos por ', '
    set1 = set(set1.split(', '))
    set2 = set(set2.split(', '))

    # Verifica qual é o código da operação e realiza a operação correspondente
    if opCode == 'U':
        result = set1.union(set2)  # União dos conjuntos
        operation = "\nUnião sendo A ∪ B = {x| x ∈ A ∨ x ∈ B}"
    elif opCode == 'I':
        result = set1.intersection(set2)  # Interseção dos conjuntos
        operation = "\nInterseção sendo A ∩ B = {x| x ∈ A ∧ x ∈ B}"
    elif opCode == 'D':
        result = set1.difference(set2)  # Diferença entre os conjuntos
        operation = "\nDiferença sendo A – B = {x|x ∈ A ^ x ∉ B}"
    elif opCode == 'C':
        # Produto cartesiano entre os conjuntos, criando pares (x, y)
        result = {(x, y) for x in set1 for y in set2}
        operation = "\nProduto Cartesiano sendo A ⨯ B = {(x,y) | x ∈ A e y ∈ B}"
        # Converte cada par do produto cartesiano em uma string "(x, y)"
        resultStr = ', '.join([f"({x}, {y})" for x, y in result])
    else:
        # Se o código da operação não for reconhecido, levanta um erro
        raise ValueError("Operação inválida!")

    # Para operações que não sejam produto cartesiano, converte o resultado em string
    if opCode != 'C':
        resultStr = ', '.join(sorted(result))

    # Exibe o resultado da operação com os conjuntos e a descrição
    print(f"{operation}: \nconjunto 1: {{{', '.join(set1)}}}, \nconjunto 2: {{{', '.join(set2)}}}. \nResultado: {{{resultStr}}}")

# Função principal que lê o arquivo e executa as operações
def main(file_path):
    # Abre o arquivo especificado no caminho e lê todas as linhas
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # A primeira linha contém o número de operações que serão realizadas
        numOperations = int(lines[0].strip())
        lineIndex = 1

        # Para cada operação, lê o código da operação e os dois conjuntos
        for _ in range(numOperations):
            opCode = lines[lineIndex].strip()  # Lê o código da operação
            set1 = lines[lineIndex + 1].strip()  # Lê o primeiro conjunto
            set2 = lines[lineIndex + 2].strip()  # Lê o segundo conjunto
            # Realiza a operação especificada com os conjuntos lidos
            calculateOperation(opCode, set1, set2)
            # Incrementa o índice da linha para processar a próxima operação
            lineIndex += 3

# Ponto de entrada do programa: executa a função main com o arquivo de entrada 'data/data1.txt'

main('data/data1.txt')
