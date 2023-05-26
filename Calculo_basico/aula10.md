## Disciplina de Cálculo Básico

### Aula 10 - Definição e fórmulas de derivação

#### Definição formal de derivada

- Seja `f: df/dx` = lim (f(x + delta(x))) - f(x) / delta(x) onde delta(x) > 0

- Por exemplo: `f(x) = x^2` -> df/dx = lim (f(x + delta(x))) - f(x) / delta(x) = lim (x + delta(x))^2 - x^2 / delta(x) = lim (x^2 + 2x * delta(x) + delta(x)^2 - x^2) / delta(x) = lim (2x * delta(x) + delta(x)^2) / delta(x) = lim 2x + delta(x) = 2x


#### Fórmulas de derivação

- Seja `f(x) = k` -> df/dx = 0 (derivada de uma constante é zero)

- Seja `f(x) = x^n` -> df/dx = n * x^(n-1) (derivada de uma potência é a potência menos um)

- Seja `f(x) = k * x^n` -> df/dx = k * n * x^(n-1) (derivada de uma constante vezes uma potência é a constante vezes a potência menos um)

- Seja a função exponencial `f(x) = e^x` -> df/dx = e^x (derivada da função exponencial é a própria função exponencial)

- Seja a função logarítmica `f(x) = log(x)` -> df/dx = 1/x (derivada da função logarítmica é 1 dividido pelo valor da função)

- Seja a função trigonométrica `f(x) = sen(x)` -> df/dx = cos(x) (derivada da função seno é a função cosseno). Já `f(x) = cos(x)` -> df/dx = -sen(x) (derivada da função cosseno é a função seno negativa), e `f(x) = tg(x)` -> df/dx = sec^2(x) (derivada da função tangente é a secante ao quadrado)