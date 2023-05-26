## Disciplina de Cálculo Básico

### Aula 11 - Regras de derivação

#### 1. regra de derivação

- Soma ou subtração de função:
    
- Seja `f(x) = u(x) + v(x)` -> df/dx = du/dx + dv/dx
    
- Seja `f(x) = u(x) - v(x)` -> df/dx = du/dx - dv/dx

- Exemplo: `f(x) = x^2 + sen(x) + 12` -> df/dx = 2x + cos(x)

#### 2. regra de derivação

- Multiplicação de função por uma constante:

- Seja `f(x) = k * u(x)` -> df/dx = k * du/dx

- Exemplo: `f(x) = 3x^2` -> df/dx = 3 * 2x = 6x

#### 3. regra do produto

- Produto de função:

- Seja `f(x) = u(x) * v(x)` -> df/dx = u(x) * dv/dx + v(x) * du/dx

- Exemplo: `f(x) = x^2 * sen(x)` -> df/dx = x^2 * cos(x) + sen(x) * 2x = x^2 * cos(x) + 2x * sen(x)

#### 4. regra do quociente

- Quociente de função:

- Seja `f(x) = u(x) / v(x)` -> df/dx = (v(x) * du/dx - u(x) * dv/dx) / v(x)^2

- Exemplo: `f(x) = x^2 / sen(x)` -> df/dx = (sen(x) * 2x - x^2 * cos(x)) / sen(x)^2

#### 5. regra da cadeia

- Composição de função:

- Seja `f(x) = u(v(x))` -> df/dx = du/dv * dv/dx

- Exemplo: `f(x) = (x^2 + 1)^3` -> df/dx = 3 * (x^2 + 1)^2 * 2x = 6x * (x^2 + 1)^2