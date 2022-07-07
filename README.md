//C++ Program to implement Queue using Array

#include <iostream.h>

#include <cstdlib.h>

using namespace std;
 
 
#define SIZE 1000
 

class Queue
{
    int *Arr;       
    int Capa;   
    int Front;      
    int Rear;       
    int Count;      
 
public:
    Queue(int size = SIZE);     
    ~Queue();                  
 
    int dequeue();
    void enqueue(int y);
    int peek();
    int size();
    bool isEmpty();
    bool isFull();
};
 

Queue::Queue(int size)
{
    Arr = new int[size];
    Capa = size;
    Front = 0;
    Rear = -1;
    Count = 0;
}
 

Queue::~Queue() {
    delete[] Arr;
}
 

int Queue::dequeue()
{
    
    if (isEmpty())
    {
        cout << "Underflow\nProgram Terminated\n";
        exit(EXIT_FAILURE);
    }
 
    int y = Arr[Front];
    cout << "Removing " << y << endl;
 
    Front = (Front + 1) % Capa;
    Count--;
 
    return y;
}



void Queue::enqueue(int item)
{
    
    if (isFull())
    {
        cout << "Overflow\nProgram Terminated\n";
        exit(EXIT_FAILURE);
    }
 
    cout << "Inserting " << item << endl;
 
    Rear = (Rear + 1) % Capa;
    Arr[Rear] = item;
    Count++;
}
 

int Queue::peek()
{
    if (isEmpty())
    {
        cout << "Underflow\nProgram Terminated\n";
        exit(EXIT_FAILURE);
    }
    return Arr[Front];
}
 

int Queue::size() {
    return Count;
}
 

bool Queue::isEmpty() {
    return (size() == 0);
}
 

bool Queue::isFull() {
    return (size() == Capa);
}
 
int main()
{

    Queue Q(5);
 
    Q.enqueue(1);
    Q.enqueue(2);
    Q.enqueue(3);
 
    cout << "The front element is " << Q.peek() << endl;
    Q.dequeue();
 
    Q.enqueue(4);
 
    cout << "The queue size is " << Q.size() << endl;
 
    Q.dequeue();
    Q.dequeue();
    Q.dequeue();
 
    if (Q.isEmpty()) {
        cout << "The queue is empty\n";
    }
    else {
        cout << "The queue is not empty\n";
    }
 
    return 0;
}


