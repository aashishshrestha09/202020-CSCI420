/*                                                                                                                     
  Name: Paul Talaga
  Date: Oct 30, 2017
  Desc: Program to demonstrate the use of pthreads
        It prints various strings to the screen.

  To compile this, do: g++ -lpthread thread-helloWorld.cpp
*/

#include <iostream>
#include <pthread.h>
#include <string>

using namespace std;

const int NUM_THREADS = 3;
const int NUM_LOOPS = 100000;

struct thread_data_t{
  int thread_id;
  string name;
};

unsigned long temp;

void* doStuff(void* arg){
  thread_data_t* input;
  input = (thread_data_t*)arg;

  int thread_num = input->thread_id;
  string name = input->name;
  
  cout << "Hello " << name << endl;
  return NULL;
}



int main(){

  temp = 0;

  thread_data_t passed[NUM_THREADS];
  pthread_t threads[NUM_THREADS];

  pthread_attr_t attr;
  pthread_attr_init(&attr);
  pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

  passed[0].thread_id = 0;
  passed[0].name = "Bob";
  //doStuff(&passed);
  pthread_create(&threads[0], &attr, doStuff, (void*)&passed[0]);

  passed[1].thread_id = 1;
  passed[1].name = "Billy";
  //doStuff(&passed);
  pthread_create(&threads[1], &attr, doStuff, (void*)&passed[1]);

  passed[2].thread_id = 2;
  passed[2].name = "Greg";
  //doStuff(&passed);
  pthread_create(&threads[2], &attr, doStuff, (void*)&passed[2]);
  
  cout << "All threads started." << endl;

  for(int i = 0; i < NUM_THREADS; i++){
    pthread_join(threads[i], NULL);
    cout << "Thread " << i << " done." << endl;
  }

  pthread_attr_destroy(&attr);

  return 0;

}
