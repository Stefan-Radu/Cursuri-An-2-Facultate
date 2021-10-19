#functii

f <- function() {
  #optional return()
}

f1 <- function(x) {
  x ^ 2 / 3
}
f1(3)

# fenomen ciudat
f11 <- function(x) {
  x <- x ^ 2 / 3
}

f11(3) #returneaza o atribuire deci nu afisaza
(y <- f11(3)) # aici afisaza

a <- integrate(f1, 0, 1)
a$value

integrate(f1, 0, Inf)

fgama <- function(x, a) {
  x ^ (a - 1) * exp(-x)
}

integrate(fgama, 0, Inf, a=7)

factorial(6)

gama_sor <- function(n) {
  if (n == floor(n)) return(factorial(n - 1))
  if (n == .5) return(sqrt(pi))
  if (n > 1) return ((n - 1) * gama_sor(n - 1))
  return(integrate(fgama, 0, Inf, a = n)$value)
}

gama_sor(9/4)

# TEMA beta(a, b) folosindu-te de proprietati si gama

# Reprezentarea grafica a functiilor
# Discretizarea intervalului pe care vrem sa reprezentam grafic functia

t <- seq(-5, 8, 0.001)
plot(t, f1(t), col="magenta")

# Sa se reprezinte grafic fn(x)=x^n pe [0, 1]

t <- seq(0, 1, 0,001)

lines(t, t, col="green")
for (i in 2:10) lines(t, t^i, col=i)

x <- RV(c(1, 7, 9), c(1/3, 1/2, 1/6))
X1 <- RV(1:100)
P(X1 < 22)
plot(x)

X2 <- RV(c(-10:10, 14, 13, 24, 54, 102))
# P(8<x2<50)
P((X2 > 8)%AND%(X2 < 50))



























