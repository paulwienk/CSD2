
#if defined(__MINGW32__) || defined(__MINGW64__)
  #define _WIN32_WINNT 0x0501
  #include "mingw-std-threads/mingw.thread.h"
#else
  #include <thread>
#endif