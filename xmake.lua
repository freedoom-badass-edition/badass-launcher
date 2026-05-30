add_rules("mode.debug", "mode.release")

add_requires("libcurl")

target("badass_launcher")
    set_kind("binary")
    add_files("src/**.cpp")
    add_packages("libcurl")