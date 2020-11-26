#include <iostream>
#include <string>

class Person
{

public:
    Person(std::string newname);

    std::string getName();

private:
    std::string name;
};

Person::Person(std::string newname)
{
    name = newname;
}

std::string Person::getName()  
{
    return name;
}

class Adress {
public:
    Adress(std::string street, int nummer, int zipcode, std::string city);
    Adress() = default;

    std::string getAsString();

private: 
    int nummer;
    int zipcode;
    std::string city;
    std::string street; 
};

Adress::Adress(std::string street_, int nummer_, int zipcode_, std::string city_)
{
    street = street_;
    nummer = nummer_;
    zipcode = zipcode_;
    city = city_;
}

std::string Adress::getAsString()
{
    return street + " " + std::to_string(nummer) + "\n" + std::to_string(zipcode) + " " + city;
}

class Jumbo {
public:
    Jumbo(Adress newAdress);

    void visit(Person& person)
    {
        std::cout << "hello " << person.getName() << '\n' << "in Jumbo te \n" << adress.getAsString();
    }

private:
    Adress adress;
};

Jumbo::Jumbo(Adress newAdress)
{ 
    adress = newAdress;
}



int main()
{
    auto person = Person("Paul Wienk");
    auto adress = Adress("Poeplaan", 6, 4573, "UTRECHT");
    auto jumbo = Jumbo(adress);
    

    jumbo.visit(person);

    return 0;
}
