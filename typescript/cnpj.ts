
class CNPJ {
    private cnpj: string;

    private cnpjDV: string;

    isValid(inCNPJ: string): boolean {
        if (!inCNPJ) {
            return false;
        }

        const cnpjInvalidos = ["00000000000000"];

        try {
            this.cnpj = CNPJ.removePontuacao(inCNPJ);

            if (cnpjInvalidos.includes(this.cnpj)) {
                return false;
            }

            // Remove os dígitos verificadores do CNPJ
            const cnpjSemDV = this.removeDVCNPJ();
            // Calcula os dígitos verificadores
            const dv = this.geraDV();
            return `${cnpjSemDV}${dv}` === this.cnpj;
        } catch (error) {
            return false;
        }
    }

    private geraDV(): string {
        this.cnpjDV = this.removeDVCNPJ();
        return this.calculaDV();
    }

    private removeDVCNPJ(): string {
        if (this.cnpj.length === 14) {
            return this.cnpj.slice(0, -2);
        } else if (this.cnpj.length === 12) {
            return this.cnpj;
        } else {
            throw new Error("CNPJ com tamanho inválido!");
        }
    }

    calculaDV(): string {
        const dv1 = this.calculaDV1();
        const dv2 = this.calculaDV2();
        return `${dv1}${dv2}`;
    }

    private calculaDV1(): number {
        const dv = this.calculaSomaDV();
        this.cnpjDV = `${this.cnpjDV}${dv}`;
        return dv;
    }

    private calculaDV2(): number {
        const dv = this.calculaSomaDV();
        this.cnpjDV = `${this.cnpjDV}${dv}`;
        return dv;
    }

    private calculaAscii(caracter: string): number {
        return caracter.charCodeAt(0) - 48;
    }

    private calculaSomaDV(): number {
        const tamanhoRange = this.cnpjDV.length;
        const numRange = Math.ceil(tamanhoRange / 8);

        let pesos: number[] = [];
        for (let i = 0; i < numRange; i++) {
            pesos = pesos.concat([2, 3, 4, 5, 6, 7, 8, 9]);
        }

        pesos = pesos.slice(0, tamanhoRange).reverse();
        const somaProduto = Array.from(this.cnpjDV).reduce(
            (acc, char, index) => acc + this.calculaAscii(char) * pesos[index],
            0
        );

        const modSoma = somaProduto % 11;
        return modSoma < 2 ? 0 : 11 - modSoma;
    }

    private static removePontuacao(inCNPJ: string): string {
        return inCNPJ.replace(/[.\-/]/g, '');
    }
}

