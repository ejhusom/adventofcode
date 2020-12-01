// ==================================================================
// File:    expense_report.cpp
// Author:  Erik Johannes Husom
// Created: 2020-12-01
// ------------------------------------------------------------------
// Description: Sovling day 1 of Advent of code 2020.
// ==================================================================
#include <cmath>
#include <iostream>
#include <fstream>
#include "time.h"
#include <vector>
using namespace std;

vector<int> read_file(){

    vector<int> numbers;

    ifstream file("expense-report.txt");

    if (file.is_open()){

        int current_number = 0;

        while (file >> current_number){
            numbers.push_back(current_number);
        }

        file.close();

        /* for (int i = 0; i < numbers.size() ; i++){ */
        /*     cout << numbers[i] << endl; */
        /* } */
        
    } else {
        cout << "Cannot open file." << endl;
    }

    return numbers;

}

int solve_puzzle_1(){

    vector<int> numbers = read_file();

    for (int i = 0; i < numbers.size(); i++){
        int number1 = numbers[i];
        for (int j = i+1; j < numbers.size(); j++){
            int number2 = numbers[j];

            if (number1 + number2 == 2020){
                return number1*number2;
            }
        }
    }

    return 0;
}

int solve_puzzle_2(){

    vector<int> numbers = read_file();

    for (int i = 0; i < numbers.size(); i++){
        int number1 = numbers[i];
        for (int j = i+1; j < numbers.size(); j++){
            int number2 = numbers[j];
            for (int k = j+1; k < numbers.size(); k++){
                int number3 = numbers[k];

                if (number1 + number2 + number3 == 2020){
                    return number1*number2*number3;
                }
            }
        }
    }

    return 0;
}

int main(int argc, char *argv[]){

    int result = solve_puzzle_1();
    cout << "Puzzle 1:" << endl;
    cout << result << endl;

    result = solve_puzzle_2();
    cout << "Puzzle 2:" << endl;
    cout << result << endl;

    return 0;
} // end of main function

