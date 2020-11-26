#include <iostream>

//void = niks. de functie doet niks en geeft niks terug
//void is een type

//constructor en destructor. hebben zelfde naam als de class, hoofdlettergevoelig
//alles is bij default private. als je wilt dat je ze van buiten kan benaderen dan moett je public erin zetten
class World
{
public:
  World(int newyear); //constructor
  ~World(); //destructor
  void hello();
private:
  int year;
};

//World::hello zegt dat hij specifiek moet kijken naar hello binnen class World
void World::hello()
{
  std::cout << "Hello World, in the year " << year << std::endl;
}

World::World(int newyear)
{
  std::cout << "this world begins\n";
  year = newyear;
}

World::~World()
{
  std::cout << "this world ends\n";
}

//world maakt een object en die wordt weer aangeroepen met hello
int main ()
{
World myWorld(2020);
  myWorld.hello();

}