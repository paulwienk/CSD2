#include <iostream>

class Dog {
  public:
    int age;

    int age_in_human_years() {
        return age * 7;
    }

};

int main() {

    Dog dog1;

    dog1.age = 5;

    std::cout << "Age in human years =  " << dog1.age_in_human_years() << std::endl;

    return 0;


}






  
