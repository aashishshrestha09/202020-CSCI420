/*                                                                                                                     
  Name: Paul Talaga
  Date: Oct 30, 2017
  Desc: Program to demonstrate the use of pthreads
        This is another solution to the shared variable access issue.
        All threads still update a single global variable, but they are forced to take
        turns via a mutex.  A mutex is a type of lock where only one thread can have the
        lock at a time, which forces all others to wait (block) until the lock is released.

  To compile this, do: g++ -lpthread thread-collision-sol2.cpp
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
};

pthread_mutex_t lock;   // mutexes come in the pthread library since they're used with threads
    // This MUST be global so all threads have access to it.

unsigned long temp;

void* doStuff(void* arg){
  thread_data_t* input;
  input = (thread_data_t*)arg;

  int thread_num = input->thread_id;
  int v = input->value;

  for(int i = 0; i < NUM_LOOPS; i++){
    // This locking/unlocking makes sure only one thread is dong the code between, thus the incorrect math can't occur
    pthread_mutex_lock(&lock);
    temp = temp + 1;
    pthread_mutex_unlock(&lock);
    //temp++;
  }
  cout << "Thread #: " << thread_num << " value: " << v << " temp " << temp << endl;

  return NULL;
}



int main(){

  temp = 0;

  pthread_mutex_init(&lock, NULL); 

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


  for(int i = 0; i < NUM_THREADS; i++){
    pthread_join(threads[i], NULL);
    cout << "Thread " << i << " done." << endl;
  }

  cout << "temp (should be "<< NUM_THREADS * NUM_LOOPS << "): " << temp << endl;
  pthread_attr_destroy(&attr);
  pthread_mutex_destroy(&lock);

  return 0;

}
