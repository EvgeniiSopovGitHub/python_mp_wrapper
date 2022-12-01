import multiprocessing as mp
import time

def single_CPU_run(arg1, arg2):
    '''
        ENG
            Change the body of the function. The function can get any number of arguments.
            Design your own return data or save the results to some external storage (e.g., file).
            The following example takes 20s for running (just sleep) and demonstrates:
                - process ID
                - arguments of the current process
        РУС
            Измените код функции, функция может принимать любое число аргументов.
            Спроектируйте свои возвращаемые значения или сохраните результаты во 
            внешнее хранилище (например, файл).
            Данный пример вычисляется 20сек (обычная пауза) и выводит:
                - номер процесса
                - аргументы данного процесса
    '''

    print("Hello from process", mp.current_process().pid)
    print("arg1 =", arg1, "arg2 =", arg2)
    # do something independent
    # сделайте независимую ветвь программы
    time.sleep(5)
    return 0 # OK


if __name__ == "__main__":
    '''
        The main contains an example that show 3 times acceleration of runtime.
        Write your on code for multi-CPU runs.
        Функция main содержит пример ускорения в 3 раза времени выполнения.
        Напишите свой код для многопроцессорного выполнения.
    '''


    # check how many threads are available in your system
    # проверим сколько процессов доступно в системе
    cpu_num = mp.cpu_count()
    print()
    print("# the number of CPUs =", cpu_num)
    print("# число процессоров CPUs =", cpu_num)
    print()


    # evaluate runtime for a single-CPU mode.
    # run single_CPU_run 3 times in a loop
    # оценим время работы на 1 CPU
    # запустим single_CPU_run 3 раза в цикле
    start = time.time()
    for i in range(3):
        single_CPU_run(0, "one cpu")
    stop = time.time()
    print("# runtime using 1 CPU = ", (stop-start))
    print("# время работы на 1 CPU = ", (stop-start))
    print()

    
    # evaluate runtime for a multi-CPU mode.
    # run single_CPU_run in 3 parallel threads
    # оценим время работы на нескольких CPU
    # запустим single_CPU_run в 3х параллельных потоках   
    arg1 = [1, 2, 3]
    arg2 = ['Hello', 'Goodbye', 'Ciao']
        
    # as example, set 3 process
    # для примера, зададим 3 процесса
    p1 = mp.Process(target=single_CPU_run, args=(arg1[0], arg2[0]))
    p2 = mp.Process(target=single_CPU_run, args=(arg1[1], arg2[1]))
    p3 = mp.Process(target=single_CPU_run, args=(arg1[2], arg2[2]))
    start = time.time()
    # start all process
    # запустить все процессы
    p1.start()
    p2.start()
    p3.start()
    # wait until all process are finished
    # ожидание окончания всех процессов
    p1.join()
    p2.join()
    p3.join()
    # close processes
    # закрыть процессы
    p1.close()
    p2.close()
    p3.close()
    stop = time.time()
    print("# runtime using 3 CPU = ", (stop-start))
    print("# время работы на 3 CPU = ", (stop-start))
    print()


    # the same 3 threads, but using loop for initialization
    # тот же пример с 3 потоками, но с инициализацией в цикле
    num_process = 3 # use any number or mp.cpu_count()
    pool = []
    for i in range(num_process):
        pool.append(mp.Process(target=single_CPU_run, args=(arg1[i], arg2[i])))
    start = time.time()
    for i in range(3):
        pool[i].start()
    for i in range(3):
        pool[i].join()
    for i in range(3):
        pool[i].close()        
    stop = time.time()
    print("# runtime using 3 CPU = ", (stop-start))
    print("# время работы на 3 CPU = ", (stop-start))