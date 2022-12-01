<h1>A Simple Template for Running your Code in Parallel using Multiprocessing in Python</h1>

<br>

# ENG

The `main.py` contains an example of using multi-CPU mode for running you code.

We assume that each parallel branch is totally independent. It is better not to return any results from branches to the `main` function, the results can be saved into external files or you need to design the way how to merge the results from branches.

An independent block is defined in `single_CPU_run(arg1, arg2,...)` function.

The template don't use any map function for automated assigning to threads. The number of threads and the assignment are set by a user.

The example of `single_CPU_run` just prints ID for the process used and waits for 5 seconds.

The `main` function demonstrates 3 options:
* The `single_CPU_run` runs 3 times in a loop using a single CPU. Should takes about 15s.
* The `single_CPU_run` runs in parallel using 3 CPUs. Each process is initialized in a separate line of code. Should takes about 5s.
* The same as the previous option, but processes are initialized in a loop. Should takes about 5s.

When one runs the `main.cpp`, the following results are shown in the console.

    Hello from process 17728
    arg1 = 0 arg2 = one cpu
    Hello from process 17728
    arg1 = 0 arg2 = one cpu
    Hello from process 17728
    arg1 = 0 arg2 = one cpu
    # runtime using 1 CPU =  15.029483795166016
    # время работы на 1 CPU =  15.029483795166016

    Hello from process 15976
    Hello from process 4128
    arg1 = 1 arg2 = Hello  
    arg1 = 2 arg2 = Goodbye
    Hello from process 9020
    arg1 = 3 arg2 = Ciao   
    # runtime using 3 CPU =  5.168347120285034
    # время работы на 3 CPU =  5.168347120285034

    Hello from process 18400
    arg1 = 1 arg2 = Hello   
    Hello from process 17036
    arg1 = 2 arg2 = Goodbye 
    Hello from process 4868 
    arg1 = 3 arg2 = Ciao    
    # runtime using 3 CPU =  5.128567218780518
    # время работы на 3 CPU =  5.128567218780518

When using this template for your purposes, replace the body of the `single_CPU_run` function and remove unnecessary code from the `main` function (the option 3 is enough).

<br>

<br>

# РУС

Функция `main.py` содержит пример использования многопроцессорного режима для запуска вашего кода.

Предполагается, что каждая параллельная ветвь полностью независима. Лучше не возвращать какие-либо результаты из веток в функцию `main`, результаты можно сохранить во внешние файлы или нужно разработать способ объединения результатов из веток.

Независимый блок определяется в функции `single_CPU_run(arg1, arg2,...)`.

В шаблоне не используются никакие функции для автоматического назначения потоков (типа `map`). Количество потоков и назначения задаются пользователем.

В данном примере функция `single_CPU_run` просто печатает идентификатор используемого процесса и ждет 5 секунд.

Функция `main` показывает 3 варианта работы:
* `single_CPU_run` запускается 3 раза в цикле с использованием одного процессора. Должно занять около 15 секунд.
* `single_CPU_run` выполняется параллельно с использованием 3 процессоров. Каждый процесс инициализируется отдельной строкой кода. Должно занять около 5 секунд.
* То же, что и предыдущий вариант, но процессы инициализируются в цикле. Должно занять около 5 секунд.

Если запустить `main.cpp`, в консоли отображаются следующие результаты.

    Hello from process 17728
    arg1 = 0 arg2 = one cpu
    Hello from process 17728
    arg1 = 0 arg2 = one cpu
    Hello from process 17728
    arg1 = 0 arg2 = one cpu
    # runtime using 1 CPU =  15.029483795166016
    # время работы на 1 CPU =  15.029483795166016

    Hello from process 15976
    Hello from process 4128
    arg1 = 1 arg2 = Hello  
    arg1 = 2 arg2 = Goodbye
    Hello from process 9020
    arg1 = 3 arg2 = Ciao   
    # runtime using 3 CPU =  5.168347120285034
    # время работы на 3 CPU =  5.168347120285034

    Hello from process 18400
    arg1 = 1 arg2 = Hello   
    Hello from process 17036
    arg1 = 2 arg2 = Goodbye 
    Hello from process 4868 
    arg1 = 3 arg2 = Ciao    
    # runtime using 3 CPU =  5.128567218780518
    # время работы на 3 CPU =  5.128567218780518

При использовании этого шаблона для своих целей замените тело функции `single_CPU_run` и удалите ненужный код из функции `main` (достаточно варианта 3).