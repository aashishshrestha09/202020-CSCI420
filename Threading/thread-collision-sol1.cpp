/*                                                                                                                     
  Name: Paul Talaga
  Date: Oct 30, 2017
  Desc: Program to demonstrate the use of pthreads
        This is one way to deal with multiple threads reading/writing a shared variable,
        DONE DO IT!  Each thread keep track of its own work and report back when done.

  To compile this, do: g++ -lpthread thread-collision-sol1.cpp
*/

#include <iostream>
#include <pthread.h>
#include <string>

using namespace std;

const int NUM_THREADS = 10;
const int NUM_LOOPS = 100000;

struct thread_data_t{
  int thread_id;
  int value;
  int ret;
};

//unsigned long temp;

void* doStuff(void* arg){
  thread_data_t* input;
  input = (thread_data_t*)arg;

  int thread_num = input->thread_id;
  int v = input->value;
  int temp = 0;
  for(int i = 0; i < NUM_LOOPS; i++){
    temp = temp + 1;
  }
  input->ret = temp;
  cout << "Thread #: " << thread_num << " value: " << v << " temp " << temp << endl;

  return NULL;
}



int main(){

  //temp = 0;

  thread_data_t passed[NUM_THREADS];
  pthread_t threads[NUM_THREADS];

  pthread_attr_t attr;
  pthread_attr_init(&attr);
  pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

  for(int i = 0; i < NUM_THREADS; i++){
    passed[i].thread_id = i;
    passed[i].value = 55;
    pthread_create(&threads[i], &attr, doStuff, (void*)&passed[i]);
  }

  int total = 0;
  for(int i = 0; i < NUM_THREADS; i++){
    pthread_join(threads[i], NULL);
    cout << "Thread " << i << " done." <<  passed[i].ret << endl;
    total = total + passed[i].ret;
  }

  cout << "temp (should be "<< NUM_THREADS * NUM_LOOPS << "): " << total << endl;
  pthread_attr_destroy(&attr);

  return 0;

}
