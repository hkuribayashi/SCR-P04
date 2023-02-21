import sys

alfabeto = 'abcdefghijklmnopqrstuvwxyz'


def criptografar(mensagem_plana, chave_c):
    msg_criptografada = ""
    return msg_criptografada


def decriptografar(mensagem_criptografada, chave):
    msg_plana = ""
    return msg_plana


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(criptografar("zhugo", 3))
        print(decriptografar("ckxjr", 3))
        # modo = sys.argv[1]
        # chave = int(sys.argv[2])
        # msg = sys.argv[3]
        # if modo == "crypt":
        #     print(criptografar(msg, chave))
        # elif modo == "decrypt":
        #     print(decriptografar(msg, chave))
    else:
        print("Uso: $ python main.py [crypt|decrypt] <chave> <mensagem>")
