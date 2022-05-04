# Concurrency and Parallelism
It's quite important to understand the concepts of both **`concurrency`** and **`parallelism`**.
- What is **Concurrency**
  - Concurrency enables a computer to do many things seemingly at the same time. For example, the operating
  system rapidly changes which program is running on the single processor. It interleaves the execution of the programs,
  providing the illusion that the programs are running simultaneously.

- What is **Parallelism**
  - Parallelism involves actually doing many things at the same time. A computer with multipe CPU cores can execute
  multiple programs simultaneously.

# Item: use python subprocess to manage a underlying Child Process(in specific OS)
**subprocess** is a builtin module in Python that enable us to start another child process in our operating system.

  
