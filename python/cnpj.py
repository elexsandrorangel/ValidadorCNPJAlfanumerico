from math import ceil


class CNPJ:
    def is_valid(self, in_cnpj: str) -> bool:
        if not in_cnpj:
            return False

        cnpj_invalidos = ["00000000000000"]

        try:
            self.cnpj = self.__remove_pontuacao(in_cnpj)

            if self.cnpj in cnpj_invalidos:
                return False

            # Remove os dígitos verificadores do CNPJ
            cnpj_sem_dv = self.__remove_dv_cnpj()
            # Calcula os dígitos verficadores
            dv = self.__gera_dv()
            return "%s%s" % (cnpj_sem_dv, dv) == self.cnpj
        except ValueError:
            return False


    def __gera_dv(self) -> str:
        cnpj_sem_dv = self.__remove_dv_cnpj()
        dv = DigitoVerificadorCNPJ(cnpj_sem_dv)
        return dv.calcula_dv()

    def __remove_dv_cnpj(self) -> str:
        if len(self.cnpj) == 14:
            return self.cnpj[0:-2]
        elif len(self.cnpj) == 12:
            return self.cnpj
        else:
            raise ValueError("CNPJ com tamanho inválido!")

    @staticmethod
    def __remove_pontuacao(in_cnpj: str) -> str:
        return ''.join(x for x in in_cnpj if x not in "./-")


class DigitoVerificadorCNPJ:
    def __init__(self, input: str):
        self._cnpj = input.upper()
        self._cnpj_dv = input.upper()

    def calcula_dv(self) -> str:
        dv1 = self.__calcula_dv1()
        dv2 = self.__calcula_dv2()
        return f"{dv1}{dv2}"

    def __calcula_dv1(self) -> int:
        dv = self.__calcula_soma_dv()
        self._cnpj_dv = f"{self._cnpj_dv}{dv}"
        return dv

    def __calcula_dv2(self) -> int:
        dv = self.__calcula_soma_dv()
        self._cnpj_dv = f"{self._cnpj_dv}{dv}"
        return dv

    def calcula_ascii(self, caracter: str):
        return ord(caracter) - 48

    def __calcula_soma_dv(self) -> int:
        tamanho_range = len(self._cnpj_dv)
        num_range = ceil(tamanho_range / 8)

        pesos = list()
        for i in range(num_range):
            pesos.extend(range(2, 10))

        pesos = pesos[0:tamanho_range]
        pesos.reverse()
        soma_produto = sum(a * b for a, b in zip(map(self.calcula_ascii, self._cnpj_dv), pesos))

        mod_soma = soma_produto % 11
        if mod_soma < 2:
            return 0
        else:
            return 11 - mod_soma

