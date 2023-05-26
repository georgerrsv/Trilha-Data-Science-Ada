## Disciplina de Cálculo Básico

### Aula 7 - Aplicações de limites

#### Primeira aplicação.

- Considere a função f(x) = (x^2 - 1) / (2x^2 - x - 1). Para que o denominador não seja 0, temos que 2x^2 - x - 1 != 0. Resolvendo a equação do segundo grau, temos que x != 1 e x != -1/2. Logo, o domínio de f é Df = R \ {1, -1/2}.

- Nesse caso, quando x for qualquer valor diferente de 1 e -1/2, a função f(x) estará definida. Mas, e quando x = 1 ou x = -1/2? O que acontece com a função f(x)? Para responder a essa pergunta, vamos calcular os limites laterais de f(x) quando x tende a 1 e quando x tende a -1/2.

- Limite lateral de f(x) quando x tende a 1:

```
lim f(x) = lim (x^2 - 1) / (2x^2 - x - 1)

x->1+   x->1+ (x^2 - 1) / (2x^2 - x - 1)

lim f(x) = lim (x^2 - 1) / (2x^2 - x - 1)

x->1-   x->1- (x^2 - 1) / (2x^2 - x - 1)
```

- Limite lateral de f(x) quando x tende a -1/2:

```
lim f(x) = lim (x^2 - 1) / (2x^2 - x - 1)

x->-1/2+   x->-1/2+ (x^2 - 1) / (2x^2 - x - 1)

lim f(x) = lim (x^2 - 1) / (2x^2 - x - 1)

x->-1/2-   x->-1/2- (x^2 - 1) / (2x^2 - x - 1)
```

- Como o limite lateral de f(x) quando x tende a 1 é diferente do limite lateral de f(x) quando x tende a -1/2, então o limite de f(x) quando x tende a 1 ou -1/2 não existe.

- Para o valor de x = 1, temos que o limite da função é 2/3.

- Já para o valor de x = -1/2, temos duas situações: quando x tende a -1/2 pela direita, o valor cresce positivamente, já quando x tende a -1/2 pela esquerda, o valor cresce negativamente. Ou seja, quando aproxima-se pela direita tende a +infinito e quando aproxima-se pela esquerda tende a -infinito. Logo, o limite não existe.