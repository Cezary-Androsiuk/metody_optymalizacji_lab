#ifndef DEFINITIONS_HPP
#define DEFINITIONS_HPP

enum Comparison{
    Equal,
    LessOrEqual,
    GreaterOrEqual
};

enum Target{
    MAXIMUM,
    MINIMUM
};


struct NumM{
    double number;
    double m;
};

#define T_SIZE VAR_COUNT + LIMITS_COUNT *2
#define G(x) ((x) == DBL_MAX || (x) == DBL_MIN ? INFINITY : (x))

struct Function{
    double coefficients[VAR_COUNT]; // [0]x_1 + [1]x_1 + ... + [n]x_n 
};
struct FunctionT{
    // [0]x_1 + [1]x_1 + ... + [n]x_n + [n+1]x_{n+1} + ... + + [n+m]x_{n+m} + [n+m+1]s_{n+1} + ... + [n+m+m]s_{n+m}
    NumM coefficients[T_SIZE];
};

struct Limit{
    double coefficients[VAR_COUNT]; // [0]x_1 + [1]x_1 + ... + [n]x_n 
    Comparison comparison;
    double comparisonTo;
};
struct LimitT{ // Limit Transformed
    NumM lValue;
    int lValueIndex;
    // [0]x_1 + [1]x_1 + ... + [n]x_n + [n+1]x_{n+1} + ... + + [n+m]x_{n+m} + [n+m+1]s_{n+1} + ... + [n+m+m]s_{n+m}
    double coefficients[T_SIZE]; 
    double rValue;
};


#endif