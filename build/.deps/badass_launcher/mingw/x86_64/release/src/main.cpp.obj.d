{
    depfiles = "main.o: src\\main.cpp\
",
    depfiles_format = "gcc",
    files = {
        [[src\main.cpp]]
    },
    values = {
        [[D:\Programs\mingw64\bin\x86_64-w64-mingw32-g++]],
        {
            "-m64",
            "-fvisibility=hidden",
            "-fvisibility-inlines-hidden",
            "-O3",
            "-DCURL_STATICLIB",
            "-isystem",
            [[C:\Users\rostuhan\AppData\Local\.xmake\packages\l\libcurl\8.11.0\1e611aab4448493782718961880b5f44\include]],
            "-DNDEBUG"
        }
    }
}