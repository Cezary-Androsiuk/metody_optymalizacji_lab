#include <stdio.h>
#include <float.h>
#include <math.h>

#define MAX_ITERATIONS 10

#define I 4

#if I == 0 
#define VAR_COUNT 2
#define LIMITS_COUNT 2
#elif I == 1
#define VAR_COUNT 2
#define LIMITS_COUNT 3
#elif I == 2
#define VAR_COUNT 3
#define LIMITS_COUNT 3
#elif I == 3
#define VAR_COUNT 2
#define LIMITS_COUNT 3 
#elif I == 4
#define VAR_COUNT 2
#define LIMITS_COUNT 3
#endif

#include "definitions.hpp"


#if I == 0 
constexpr Target target = Target::MAXIMUM;
Function function = { {1, 2} };

Limit limits[LIMITS_COUNT] = {
    Limit({
        {1, 1},
        Comparison::LessOrEqual,
        10
        }),
    Limit({
        {-2, 1},
        Comparison::LessOrEqual,
        4
        }),
};
#elif I == 1
constexpr Target target = Target::MINIMUM;
Function function = { {2, 18} };

Limit limits[LIMITS_COUNT] = {
    Limit({
        {80, 100},
        Comparison::GreaterOrEqual,
        100
        }),
    Limit({
        {20, 200},
        Comparison::LessOrEqual,
        300
        }),
    Limit({
        {1, 0},
        Comparison::LessOrEqual,
        1.5
        }),
};
#elif I == 2
// Find solution using Simplex method
// MAX Z = 3x1 + 5x2 + 4x3
// subject to
// 2x1 + 3x2 <= 8
// 2x2 + 5x3 <= 10
// 3x1 + 2x2 + 4x3 <= 15
// and x1,x2,x3 >= 0
constexpr Target target = Target::MAXIMUM;
Function function = { {3, 5, 4} };

Limit limits[LIMITS_COUNT] = {
    Limit({
        {2, 3, 0},
        Comparison::LessOrEqual,
        8
        }),
    Limit({
        {0, 2, 5},
        Comparison::LessOrEqual,
        10
        }),
    Limit({
        {3, 2, 4},
        Comparison::LessOrEqual,
        15
        }),
};
#elif I == 3
// Find solution using Simplex method
// MAX Z = 30x1 + 40x2
// subject to
// 3x1 + 2x2 <= 600
// 3x1 + 5x2 <= 800
// 5x1 + 6x2 <= 1100
// and x1,x2 >= 0
constexpr Target target = Target::MAXIMUM;
Function function = { {30, 40} };

Limit limits[LIMITS_COUNT] = {
    Limit({
        {3, 2},
        Comparison::LessOrEqual,
        600
        }),
    Limit({
        {3, 5},
        Comparison::LessOrEqual,
        800
        }),
    Limit({
        {5, 6},
        Comparison::LessOrEqual,
        1100
        }),
};
#elif I == 4
// Find solution using Simplex method (BigM method)
// MIN Z = 2000x1 + 1500x2
// subject to
// 6x1 + 2x2 >= 8
// 2x1 + 4x2 >= 12
// 4x1 + 12x2 >= 24
constexpr Target target = Target::MINIMUM;
Function function = { {2000, 1500} };

Limit limits[LIMITS_COUNT] = {
    Limit({
        {6, 2},
        Comparison::GreaterOrEqual,
        8
        }),
    Limit({
        {2, 4},
        Comparison::GreaterOrEqual,
        12
        }),
    Limit({
        {4, 12},
        Comparison::GreaterOrEqual,
        24
        }),
};
#endif



void printFunction()
{
    printf("f()");
    for(int i=0; i<VAR_COUNT; ++i)
    {
        if(i == 0) printf(" = ");
        else printf(" + ");
        printf("%g*x_%d", G(function.coefficients[i]), i);
    }
    printf(" -> %s\n", target == Target::MAXIMUM ? "max" : "min");
}

void printLimits()
{
    for(int j=0; j<LIMITS_COUNT; ++j)
    {
        Limit *limit = (limits + j);
        for(int i=0; i<VAR_COUNT; ++i)
        {
            if(i != 0) printf(" + ");
            printf("%g*x_%d", G(limit->coefficients[i]), i);
        }
        const char *comp;
        if(limit->comparison == Comparison::Equal)
            comp = "=";
        else if(limit->comparison == Comparison::LessOrEqual)
            comp = "<=";
        else if(limit->comparison == Comparison::GreaterOrEqual)
            comp = ">=";

        printf(" %s %g", comp, limit->comparisonTo);
        printf("\n");

    }
}

void printFunctionT(FunctionT *functionT)
{
    printf("    f()");
    for(int i=0; i<T_SIZE; ++i)
    {
        if(i == 0) printf(" = ");
        else printf(" + ");

        const char *sign = "x";
        int index = i;
        if(i >= VAR_COUNT)
        {
            if((i-VAR_COUNT) % 2)
                sign = "s";
            index = (i-VAR_COUNT) /2 + VAR_COUNT;
        }

        printf("(%g + %gm)*%s_%d", functionT->coefficients[i].number, functionT->coefficients[i].m, sign, index);
    }
    printf("\n");
}

void printLimitsT(LimitT *limitsT)
{
    for(int j=0; j<LIMITS_COUNT; ++j)
    {
        LimitT *limitT = (limitsT + j);
        printf("(% 5.1g + % 5.1gm) | ", limitT->lValue.number, limitT->lValue.m);
        for(int i=0; i<T_SIZE; ++i)
        {
            // const char *sign = "x";
            // int index = i;
            // if(i >= VAR_COUNT)
            // {
            //     if((i-VAR_COUNT) % 2)
            //         sign = "s";
            //     index = (i-VAR_COUNT) /2 + VAR_COUNT;
            // }
            
            // // not first
            // if(i != 0) 
            //     printf(" + ");

            // printf("%g*%s_%d", limitT->coefficients[i], sign, index);
            printf(" % 15g  ", limitT->coefficients[i], 0.0);
        }
        printf(" | %g", limitT->rValue);
        printf("\n");

    }
}

void printZorD(NumM *a, const char *prefix = "                   ")
{
    printf("%s", prefix);
    for(int i=0; i<T_SIZE; ++i)
        printf("(% 5.1f + % 5.1fm) ", a[i].number, a[i].m);
    printf("\n");
    
}


void transformFunction(FunctionT *functionT)
{
    // multiply each coefficient by -1 if looking for a minimum (to change into looking for maximum)
    int inverseMinimum = 1;//function.target == Target::MAXIMUM ? 1 : -1;

    // rewrite function
    for (int i=0; i<T_SIZE; ++i)
    {
        functionT->coefficients[i].number = 
            i < VAR_COUNT ? (function.coefficients[i] * inverseMinimum) : 0;
        functionT->coefficients[i].m = 0;
    }

    // set "m" value there, where Comparison is GreaterOrEqual or Equal
    // but instead of "m" use real MAXIMUM :)
    for (int i=0; i<LIMITS_COUNT; ++i)
    {
        Comparison c = limits[i].comparison;
        if(c == Comparison::GreaterOrEqual || c == Comparison::Equal)
        {
            // add VAR_COUNT to jump over all declared variables
            functionT->coefficients[VAR_COUNT +i +1].m = 1;
        }
    }
    
}

void _transformConstraint(double *coefficientsT, double *coefficients)
{
    // rewrite values
    for (int i=0; i<T_SIZE; ++i)
    {
        coefficientsT[i] = i < VAR_COUNT ? coefficients[i] : 0;
    }
}

void transformConstraints(LimitT *limitsT)
{
    for (int i=0; i<LIMITS_COUNT; ++i) 
    {
        _transformConstraint(
            limitsT[i].coefficients, 
            limits[i].coefficients);

        limitsT[i].rValue = limits[i].comparisonTo;

        // add new x_i and s_i 
        switch (limits[i].comparison)
        {
        case Comparison::LessOrEqual:
            // add VAR_COUNT to jump over all declared variables, then depends on current row set column
            limitsT[i].coefficients[VAR_COUNT + i*2] = 1;
            limitsT[i].coefficients[VAR_COUNT + i*2 +1] = 0;
            break;
        case Comparison::GreaterOrEqual:
            // add VAR_COUNT to jump over all declared variables, then depends on current row set column
            limitsT[i].coefficients[VAR_COUNT + i*2] = -1;
            limitsT[i].coefficients[VAR_COUNT + i*2 +1] = 1;
            break;
        case Comparison::Equal:
            // add VAR_COUNT to jump over all declared variables, then depends on current row set column
            limitsT[i].coefficients[VAR_COUNT + i*2] = 0;
            limitsT[i].coefficients[VAR_COUNT + i*2 +1] = 1;
            break;
        }
    }
}


void initializeLeftValues(FunctionT *functionT, LimitT *limitsT)
{
    for(int i=0; i<LIMITS_COUNT; ++i)
    {
        // assign s_i (instead of x_i) only when s_i is not 0 (when is not 0 + 0m)
        NumM x_i, s_i;

        x_i.number = functionT->coefficients[VAR_COUNT + i*2].number;
        x_i.m = functionT->coefficients[VAR_COUNT + i*2].m;
        
        s_i.number = functionT->coefficients[VAR_COUNT + i*2 +1].number;
        s_i.m = functionT->coefficients[VAR_COUNT + i*2 +1].m;
        
        if(s_i.number != 0 || s_i.m != 0)
            limitsT[i].lValue = s_i;
        else
            limitsT[i].lValue = x_i;

        limitsT[i].lValueIndex; i;
    }
}

void computeZ(LimitT *limitsT, NumM *z)
{
    for(int j=0; j<T_SIZE; ++j)
    {
        NumM sum = {0,0};
        for(int i=0; i<LIMITS_COUNT; ++i)
        {
            sum.number += limitsT[i].coefficients[j] * limitsT[i].lValue.number;
            sum.m += limitsT[i].coefficients[j] * limitsT[i].lValue.m;
        }
        z[j].number = sum.number;
        z[j].m = sum.m;
    }
}

void computeD(FunctionT *functionT, NumM *z, NumM *d)
{
    for(int i=0; i<T_SIZE; ++i)
    {
        d[i].number = functionT->coefficients[i].number - z[i].number;
        d[i].m = functionT->coefficients[i].m - z[i].m;
    }
}

int findLargestD(NumM *d)
{
    // find largest (but not look below 0)
    int index=-1;
    NumM max;
    max.m = 0;
    max.number = 0;
    for(int i=0; i<T_SIZE; ++i)
    {
        if(d[i].m > max.m)
        {
            index = i;
            max.m = d[i].m;
            max.number = d[i].number;
        }
        else if(d[i].m == max.m)
        {
            if(d[i].number > max.number)
            {
                index = i;
                max.number = d[i].number;
            }
        }
    }
    return index;
}

int findSmallestD(NumM *d)
{
    // find smallest (but not look below 0)
    int index=-1;
    NumM max;
    max.m = 0;
    max.number = 0;
    for(int i=0; i<T_SIZE; ++i)
    {
        if(d[i].m < max.m)
        {
            index = i;
            max.m = d[i].m;
            max.number = d[i].number;
        }
        else if(d[i].m == max.m)
        {
            if(d[i].number < max.number)
            {
                index = i;
                max.number = d[i].number;
            }
        }
    }
    
    printf("index: %d\n", index);
    return index;
}

int findSmallestBA(LimitT *limitsT, int column)
{
    double ba[LIMITS_COUNT]; // b_i / a_i
    for(int i=0; i<LIMITS_COUNT; ++i)
    {
        // test if not 0, if so set as -1 and ignore
        if(limitsT[i].coefficients[column] == 0)
        {
            ba[i] = -1;
            continue;
        }

        ba[i] = limitsT[i].rValue / limitsT[i].coefficients[column];
    }
    

    // find minimum, but without negative values 
    int index=0;
    double min=DBL_MAX;
    for(int i=0; i<LIMITS_COUNT; ++i)
    {
        if(ba[i] < min && ba[i] >= 0)
        {
            index = i;
            min = ba[i];
        }
    }
    return index;
}


void _updateLeftValue(FunctionT *functionT, LimitT *limitsT, int column, int row)
{
    
    limitsT[row].lValue.m = functionT->coefficients[column].m;
    limitsT[row].lValue.number = functionT->coefficients[column].number;
    limitsT[row].lValueIndex = column;
}

void _rewriteLimitsTToNewOne(LimitT *oldLimitsT, LimitT *newLimitsT)
{
    for(int j=0; j<LIMITS_COUNT; ++j)
    {
        newLimitsT[j].lValue.m = oldLimitsT[j].lValue.m;
        newLimitsT[j].lValue.number = oldLimitsT[j].lValue.number;
        newLimitsT[j].rValue = oldLimitsT[j].rValue;
        for(int i=0; i<T_SIZE; ++i)
            newLimitsT[j].coefficients[i] = oldLimitsT[j].coefficients[i];
    }
}

void _updateRightValue(LimitT *limitsT, LimitT *oldLimitsT, int column, int row, double a)
{
    // through that one row that contains 'a'
    limitsT[row].rValue = oldLimitsT[row].rValue / a;
    
    // through the rest rows
    for(int i=0; i<LIMITS_COUNT; ++i) // rows
    {
        if(i == row)
            continue;

        limitsT[i].rValue = oldLimitsT[i].rValue - 
            (oldLimitsT[i].coefficients[column] * oldLimitsT[row].rValue)/ a;
    }
}

void updateTable(FunctionT *functionT, LimitT *limitsT, int column, int row, double a)
{
    _updateLeftValue(functionT, limitsT, column, row);

    LimitT oldLimitsT[LIMITS_COUNT];
    _rewriteLimitsTToNewOne(limitsT, oldLimitsT); // updating limitsT then oldLimitsT will be old :P
    
    // through that one row that contains 'a'
    for(int i=0; i<T_SIZE; ++i) // columns
    {
        limitsT[row].coefficients[i] = oldLimitsT[row].coefficients[i] / a;
    }

    // through the rest rows
    for(int j=0; j<LIMITS_COUNT; ++j) // rows
    {
        if(j == row)
            continue;

        for(int i=0; i<T_SIZE; ++i) // columns
        {
            limitsT[j].coefficients[i] = oldLimitsT[j].coefficients[i]  -
                (oldLimitsT[row].coefficients[i] * oldLimitsT[j].coefficients[column]) / a;
        }
    }

    _updateRightValue(limitsT, oldLimitsT, column, row, a);
}

void interpretResult(FunctionT *functionT, LimitT *limitsT)
{
    printf("\nSummary:\n");
    for(int i=0; i<LIMITS_COUNT; i++)
    {
        if(limitsT[i].lValueIndex < VAR_COUNT)
            printf("x_%d -> % 5g\n", limitsT[i].lValueIndex, limitsT[i].rValue);

    }
}

int main()
{
    printFunction();
    printLimits();

    printf("\n");

    FunctionT functionT;
    transformFunction(&functionT);

    LimitT limitsT[LIMITS_COUNT];
    transformConstraints(limitsT);

    initializeLeftValues(&functionT, limitsT);

    printFunctionT(&functionT);
    printLimitsT(limitsT);

    for(int i=0; i<MAX_ITERATIONS; ++i)
    {
        NumM z[T_SIZE]; // z_j
        computeZ(limitsT, z);
        printZorD(z, "  z_j              ");

        NumM d[T_SIZE]; // c_j - z_j
        
        computeD(&functionT, z, d);
        printZorD(d, "  c_j - z_j        ");

        printf("\n");

        int column = -1;
        if(target == Target::MAXIMUM)
        {
            printf("Find largest D\n");
            column = findLargestD(d);
        }
        else
        {
            printf("Find smallest D\n");
            column = findSmallestD(d);
        }
        printf("column: %d\n", column);
        
        if(column == -1)
        {
            interpretResult(&functionT, limitsT);

            printf("\nend\n");
            return 0;
        }
        int row = findSmallestBA(limitsT, column);
        printf("row: %d\n", row);
        
        double a = limitsT[row].coefficients[column];
        printf("a: %g\n", a);

        for(int i=0; i<181; ++i) printf("%c", i==180 ? '\n' : '=');

        updateTable(&functionT, limitsT, column, row, a);

        printFunctionT(&functionT);
        printLimitsT(limitsT);
    }
}
